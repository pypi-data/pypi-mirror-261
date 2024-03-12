from threading import Thread
import pytest
from copy import deepcopy

from lle import World, WorldState, Action


def test_available_actions():
    world = World(
        """
@ @ L0S @  @
@ .  .  .  @
@ X  .  S0 @
@ X  .  S1 @
@ @  @  @  @
"""
    )
    world.reset()
    available_actions = world.available_actions()
    # Agent 0
    expected = [[Action.NORTH, Action.WEST, Action.STAY], [Action.WEST, Action.STAY]]
    for e, available in zip(expected, available_actions):
        for a in available:
            assert a in e, f"Action {a} not in {e}"


def test_parse_wrong_worlds():
    # Not enough finish tiles for all the agents
    with pytest.raises(ValueError):
        World(
            """
            @ @  @ @
            @ S0 . @
            @ .  . @
            @ @  @ @"""
        )

    # Zero agent in the environment
    with pytest.raises(ValueError):
        World("X G")


def test_world_move():
    world = World(
        """S0 X . .
.  . . .
.  . . ."""
    )
    world.reset()
    world.step([Action.SOUTH])
    world.step([Action.EAST])
    world.step([Action.NORTH])


def test_world_agents():
    world = World(
        """
                  S0 S1 S2
                  X  X  X"""
    )
    world.reset()
    assert not any(a.is_dead for a in world.agents)
    assert all(a.is_alive for a in world.agents)


def test_walk_into_wall():
    world = World(
        """@ @ @  @ @ @
@ . .  . . @
@ . S0 . . @
@ . .  X . @
@ @ @  @ @ @"""
    )
    world.reset()
    world.step([Action.SOUTH])
    with pytest.raises(ValueError):
        world.step([Action.SOUTH])


def test_world_gem_collected_and_agent_has_arrived():
    world = World(
        """
S0 X . .
.  . . .
G  . . ."""
    )
    # Do not collect the gem
    world.reset()

    # Collect the gem
    world.reset()
    world.step([Action.SOUTH])
    world.step([Action.SOUTH])
    assert world.gems_collected == 1

    # Exit the game
    world.step([Action.NORTH])
    world.step([Action.NORTH])
    world.step([Action.EAST])
    assert world.agents[0].has_arrived


def test_vertex_conflict():
    world = World(
        """
        S0 X  .  .
        .  .  S1  .
        .  X  .  ."""
    )
    world.reset()
    world.step([Action.SOUTH, Action.WEST])
    # Move to provoke a vertex conflict -> observations should remain identical
    with pytest.raises(ValueError) as _:
        world.step([Action.STAY, Action.WEST])


def test_swapping_conflict():
    world = World(
        """
S0 X  .  .
.  .  S1  .
.  X  .  ."""
    )
    world.reset()
    world.step([Action.SOUTH, Action.WEST])
    # Move to provoke a swapping conflict -> observations should remain identical
    with pytest.raises(ValueError) as _:
        world.step([Action.EAST, Action.WEST])


def test_walk_into_laser_source():
    world = World(
        """
        @ L0S @ 
        .  .  . 
        X  .  S0
        .  .  ."""
    )
    world.reset()
    world.step([Action.WEST])
    world.step([Action.NORTH])
    with pytest.raises(ValueError):
        world.step([Action.NORTH])


def test_walk_outside_map():
    world = World(
        """@ @ L0S @  @
@ .  .  .  @
@ X  .  S0 @
@ .  .  .  @
@ @  .  @  @
"""
    )
    world.reset()
    world.step([Action.SOUTH])
    world.step([Action.WEST])
    world.step([Action.SOUTH])
    with pytest.raises(ValueError):
        world.step([Action.SOUTH])


def test_world_done():
    world = World(
        """
G  G  . .  S1
X  .  . @  .
@  .  G .  .
G  .  . G  X
@ L0N . S0 ."""
    )
    world.reset()
    world.step([Action.STAY, Action.WEST])
    world.step([Action.STAY, Action.WEST])
    world.step([Action.STAY, Action.WEST])
    try:
        world.step([Action.STAY, Action.WEST])
        raise Exception("The game should be finished")
    except ValueError:
        pass


def test_gems_collected():
    world = World("S0 G X")
    world.reset()
    assert world.gems_collected == 0
    world.step([Action.EAST])
    assert world.gems_collected == 1
    world.step([Action.EAST])
    assert world.gems_collected == 1


class StatusThread(Thread):
    INITIAL = 0
    FINISHED = 1

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.status = StatusThread.INITIAL

    def run(self):
        print(self.data)
        self.status = StatusThread.FINISHED


def test_action_send_thread():
    t = StatusThread(Action.NORTH)
    t.start()
    t.join()
    assert t.status == StatusThread.FINISHED


def test_world_send_thread():
    world = World("S0 . X")
    t = StatusThread(world)
    t.start()
    t.join()
    assert t.status == StatusThread.FINISHED


def test_rendering_size():
    world = World("S0 . X")
    TILE_SIZE = 32
    expected_size = (TILE_SIZE * world.width + 1, TILE_SIZE * world.height + 1)
    assert world.image_dimensions == expected_size
    img = world.get_image()
    expected_shape = (expected_size[1], expected_size[0], 3)
    assert img.shape == expected_shape


def test_deepcopy():
    world = World("S0 . X")
    world2 = deepcopy(world)
    assert world.agents_positions == world2.agents_positions
    assert world.agents_positions is not world2.agents_positions
    assert world.width == world2.width


def test_deepcopy_not_initial_state():
    world = World("S0 . X")
    world.reset()
    world.step([Action.EAST])
    world2 = deepcopy(world)
    assert world.agents_positions == world2.agents_positions
    assert world.agents_positions is not world2.agents_positions
    assert world.width == world2.width


def test_get_state():
    world = World("S0 G X")
    world.reset()
    state = world.get_state()
    assert state.agents_positions == [(0, 0)]
    assert state.gems_collected == [False]
    world.step([Action.EAST])
    state = world.get_state()
    assert state.agents_positions == [(0, 1)]
    assert state.gems_collected == [True]


def test_set_state():
    world = World("S0 G X")
    world.reset()
    world.step([Action.EAST])
    world.set_state(WorldState([(0, 0)], [False]))
    assert world.agents_positions == [(0, 0)]
    assert world.gems_collected == 0

    world.set_state(WorldState([(0, 2)], [True]))
    assert world.agents_positions == [(0, 2)]
    assert world.gems_collected == 1


def test_world_state_hash_eq():
    world = World("S0 G X")
    world.reset()
    state1 = world.get_state()
    state2 = world.get_state()
    assert hash(state1) == hash(state2)
    assert state1 == state2
    world.step([Action.EAST])
    state1 = world.get_state()
    state2 = world.get_state()
    assert hash(state1) == hash(state2)
    assert state1 == state2


def test_world_state_hash_neq():
    s1 = WorldState([(0, 0)], [False])
    s2 = WorldState([(0, 1)], [False])

    assert hash(s1) != hash(s2)
    assert s1 != s2


def test_get_standard_level():
    for i in range(1, 7):
        World.level(i)
        World.from_file(f"lvl{i}")
        World.from_file(f"level{i}")
