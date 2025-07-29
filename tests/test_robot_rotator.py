"""
Filename: test_robot_rotator.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    Test suite for the RobotRotator class. Validates that the robot
    rotates correctly in both directions and that the facing angle
    is properly normalized.
"""
import unittest
from toyrobot.robot_rotator import RobotRotator
from toyrobot.robot import Robot

class TestRobotRotator(unittest.TestCase):
    def setUp(self):
        self.directions = {"NORTH": 90, "EAST": 0, "SOUTH": 270, "WEST": 180}
        self.robot = Robot(self.directions)
        self.rotator = RobotRotator()

    def test_rotate(self):
        test_cases = [
            ("rotate_left_from_east", 0, 90, 90),  # EAST -> NORTH
            ("rotate_left_from_north", 90, 90, 180),  # NORTH -> WEST
            ("rotate_right_from_east", 0, -90, 270),  # EAST -> SOUTH
            ("rotate_right_from_south", 270, -90, 180),  # SOUTH -> WEST
            ("multiple_left_rotations", 0, 180, 180),  # EAST -> WEST
        ]

        for name, initial_angle, rotation_angle, expected_angle in test_cases:
            with self.subTest(name=name):
                self.robot.facing_angle = initial_angle
                self.rotator.rotate(self.robot, rotation_angle)
                self.assertEqual(self.robot.facing_angle, expected_angle)

if __name__ == "__main__":
    unittest.main()
