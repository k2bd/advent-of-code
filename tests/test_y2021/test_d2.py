from advent_of_code.y2021.d2 import Position, get_position_p1, get_position_p2

TEST_INPUT = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_d2_p1():
    assert get_position_p1(TEST_INPUT) == Position(horizontal=15, depth=10)


def test_d2_p2():
    assert get_position_p2(TEST_INPUT) == Position(horizontal=15, depth=60, aim=10)
