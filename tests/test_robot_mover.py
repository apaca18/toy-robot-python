"""
Filename: test_robot_mover.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    Test suite for the RobotMover class. Validates that the robot
    moves correctly within the table boundaries and doesn't fall off the edge.
"""
import unittest
from parameterized import parameterized
from toyrobot.robot_mover import RobotMover
from toyrobot.robot import Robot
from toyrobot.table import Table
from toyrobot.position import Position

class TestRobotMover(unittest.TestCase):
    def setUp(self):
        self.table = Table(5, 5)
        self.directions = {"NORTH": 90, "EAST": 0, "SOUTH": 270, "WEST": 180}
        self.robot = Robot(self.directions)
        self.mover = RobotMover()

    @parameterized.expand([
        ("move_within_bounds_north", Position(0, 0), 90, Position(0, 1)),
        ("move_within_bounds_east", Position(0, 0), 0, Position(1, 0)),
        ("move_out_of_bounds_north", Position(0, 4), 90, Position(0, 4)),
        ("move_out_of_bounds_east", Position(4, 0), 0, Position(4, 0)),
    ])
    def test_move(self, name, initial_position, facing_angle, expected_position):
        self.robot.position = initial_position
        self.robot.facing_angle = facing_angle
        self.mover.move_one_space(self.robot, self.table)
        self.assertEqual(self.robot.position.x, expected_position.x)
        self.assertEqual(self.robot.position.y, expected_position.y)

if __name__ == "__main__":
    unittest.main()
