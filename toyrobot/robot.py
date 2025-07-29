"""
Filename: robot.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    This module implements the core Robot class for the Toy Robot simulation.
    The Robot class manages its position and direction on the table and
    delegates specific operations to specialised components.
"""

from toyrobot.robot_rotator import RobotRotator
from toyrobot.robot_reporter import RobotReporter
from toyrobot.robot_placer import RobotPlacer
from toyrobot.robot_mover import RobotMover
from toyrobot.position import Position

class Robot:
    def __init__(self, directions, robot_rotator=None, robot_reporter=None, 
                table=None, robot_placer=None, robot_mover=None):
        """
        Initialize a Robot with required components.
        
        The robot starts with no position (not on the table) and no facing direction.
        It will be placed on the table using the PLACE command.

        Facing Angle:
        - The robot's facing angle is represented in degrees.
        - 0° corresponds to East, and the positive direction is counterclockwise.
          For example:
          - 90° = North
          - 180° = West
          - 270° = South
        """
        self.position = None  # Will be a Position object once placed
        self.facing_angle = None  # Will be set when placed
        self.directions = directions
        self.table = table
        self.robot_rotator = robot_rotator or RobotRotator()
        self.robot_reporter = robot_reporter or RobotReporter()
        self.robot_placer = robot_placer or RobotPlacer()
        self.robot_mover = robot_mover or RobotMover()