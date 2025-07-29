"""
Filename: test_robot_placer.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    Test suite for the RobotPlacer class. Validates that the robot
    can be placed on the table at valid positions and that invalid
    placements are properly rejected.
"""
import unittest
from parameterized import parameterized
from toyrobot.robot_placer import RobotPlacer
from toyrobot.robot import Robot
from toyrobot.table import Table

class TestRobotPlacer(unittest.TestCase):
    def setUp(self):
        self.table = Table(5, 5)
        self.directions = {"NORTH": 90, "EAST": 0, "SOUTH": 270, "WEST": 180}
        self.robot = Robot(self.directions)
        self.placer = RobotPlacer()

    @parameterized.expand([
        ("valid_place_1", "1,2,NORTH", 1, 2, 90),
        ("valid_place_2", "0,0,EAST", 0, 0, 0),
        ("valid_place_3", "4,4,SOUTH", 4, 4, 270),
    ])
    def test_valid_place(self, name, place_command, expected_x, expected_y, expected_angle):
        self.placer.place(place_command, self.robot, self.table)
        self.assertEqual(self.robot.position.x, expected_x)
        self.assertEqual(self.robot.position.y, expected_y)
        self.assertEqual(self.robot.facing_angle, expected_angle)

    @parameterized.expand([
        ("out_of_bounds", "6,6,NORTH"),
        ("out_of_bounds_x", "5,4,NORTH"),
        ("out_of_bounds_y", "4,5,NORTH"), 
        ("invalid_direction", "1,1,NORTHEAST"),
        ("missing_arguments", "1,NORTH"),
    ])
    def test_invalid_place(self, name, place_command):
        with self.assertRaises(ValueError):
            self.placer.place(place_command, self.robot, self.table)

if __name__ == "__main__":
    unittest.main()
