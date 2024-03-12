from typing import Any, Literal, ClassVar
from typing_extensions import override
from dataclasses import dataclass
from serde import serde
import cv2
import numpy as np

from lle import World, Action, EventType, WorldState
from rlenv import RLEnv, DiscreteActionSpace, Observation
from .observations import ObservationType, StateGenerator


@serde
@dataclass
class LLE(RLEnv[DiscreteActionSpace]):
    """Laser Learning Environment (LLE)"""

    obs_type: str
    state_type: str

    REWARD_DEATH: ClassVar[float] = -1.0
    REWARD_GEM: ClassVar[float] = 1.0
    REWARD_EXIT: ClassVar[float] = 1.0
    REWARD_DONE: ClassVar[float] = 1.0

    def __init__(
        self,
        world: World,
        obs_type: ObservationType = ObservationType.STATE,
        state_type: ObservationType = ObservationType.STATE,
    ):
        self.world = world
        self.obs_type = obs_type.name
        self.state_type = state_type.name
        self.observation_generator = obs_type.get_observation_generator(world)
        self.state_generator = state_type.get_observation_generator(world)
        super().__init__(
            DiscreteActionSpace(world.n_agents, Action.N, [a.name for a in Action.ALL]),
            observation_shape=self.observation_generator.shape,
            state_shape=self.get_state().shape,
        )
        self.done = False
        self.n_arrived = 0

    @property
    def width(self) -> int:
        return self.world.width

    @property
    def height(self) -> int:
        return self.world.height

    @property
    def unit_state_size(self):
        match self.state_generator:
            case StateGenerator():
                return self.state_generator.unit_size
            case other:
                raise ValueError(f"State type {other} does not support `unit_state_size`.")

    @override
    def available_actions(self) -> np.ndarray[np.int32, Any]:
        available_actions = np.zeros((self.n_agents, self.n_actions), dtype=np.int64)
        for agent, actions in enumerate(self.world.available_actions()):
            for action in actions:
                available_actions[agent, action.value] = 1
        return available_actions

    @override
    def step(self, actions: np.ndarray[np.int32, Any]):
        assert not self.done, "Can not play when the game is done !"
        events = self.world.step([Action(a) for a in actions])
        reward = 0.0
        death_reward = 0.0
        for event in events:
            match event.event_type:
                case EventType.AGENT_DIED:
                    death_reward += LLE.REWARD_DEATH
                    self.done = True
                case EventType.GEM_COLLECTED:
                    reward += LLE.REWARD_GEM
                case EventType.AGENT_EXIT:
                    reward += LLE.REWARD_EXIT
                    self.n_arrived += 1
        if death_reward != 0:
            reward = death_reward
        elif self.n_arrived == self.n_agents:
            reward += LLE.REWARD_DONE
            self.done = True

        obs_data = self.observation_generator.observe()
        obs = Observation(obs_data, self.available_actions(), self.get_state())
        info = {"gems_collected": self.world.gems_collected, "exit_rate": self.n_arrived / self.n_agents}
        return obs, reward, self.done, False, info

    @override
    def reset(self):
        self.world.reset()
        self.done = False
        self.n_arrived = 0
        obs = self.observation_generator.observe()
        return Observation(obs, self.available_actions(), self.get_state())

    @override
    def get_state(self) -> np.ndarray[np.float32, Any]:
        # We assume that the state is the same as the observation of the first agent
        # of the observation generator.
        return self.state_generator.observe()[0]
        state = self.world.get_state()
        gems_collected = np.array(state.gems_collected, dtype=np.float32)
        agents_positions = np.array(state.agents_positions, dtype=np.float32).reshape(-1)
        return np.concatenate([gems_collected, agents_positions])

    @override
    def render(self, mode: Literal["human", "rgb_array"] = "human"):
        image = self.world.get_image()
        match mode:
            case "human":
                cv2.imshow("LLE", image)
                cv2.waitKey(1)
            case "rgb_array":
                return image
            case other:
                raise NotImplementedError(f"Rendering mode not implemented: {other}")

    @staticmethod
    def from_str(
        world_string: str,
        obs_type: ObservationType = ObservationType.FLATTENED,
        state_type: ObservationType = ObservationType.STATE,
    ):
        return LLE(World(world_string), obs_type, state_type)

    @staticmethod
    def from_file(
        path: str,
        obs_type: ObservationType = ObservationType.FLATTENED,
        state_type: ObservationType = ObservationType.STATE,
    ):
        import os

        env = LLE(World.from_file(path), obs_type, state_type)
        filename = os.path.basename(path)
        env.name = f"{env.name}-{filename}"
        return env

    @staticmethod
    def level(
        level: int,
        obs_type: ObservationType = ObservationType.FLATTENED,
        state_type: ObservationType = ObservationType.STATE,
    ):
        """Load a level from the levels folder"""
        env = LLE(World.level(level), obs_type, state_type)
        env.name = f"{env.name}-lvl{level}"
        return env

    def seed(self, _seed_value: int):
        # There is nothing random in the world to seed.
        return

    def set_state(self, state: WorldState):
        self.world.set_state(state)
        agents = self.world.agents
        self.done = any(agent.is_dead for agent in agents) or all(agent.has_arrived for agent in agents)
        self.n_arrived = sum(agent.has_arrived for agent in agents)
