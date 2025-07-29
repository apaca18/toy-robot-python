"""
Filename: test_robot_reporter.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    Test suite for the RobotReporter class. Validates that the robot's
    position and direction are correctly reported in the expected format.
"""
import unittest
from toyrobot.robot_reporter import RobotReporter
from toyrobot.robot import Robot
from toyrobot.position import Position
from io import StringIO
import sys

class TestRobotReporter(unittest.TestCase):
    def setUp(self):
        self.directions = {"NORTH": 90, "EAST": 0, "SOUTH": 270, "WEST": 180}
        self.robot = Robot(self.directions)
        self.reporter = RobotReporter()

    def test_report(self):
        self.robot.position = Position(1, 2)
        self.robot.facing_angle = 90  # NORTH

        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.reporter.report(self.robot)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Assert the captured output
        self.assertIn("1,2,NORTH", captured_output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
