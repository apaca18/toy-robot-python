"""
Filename: robot_mover.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    This module handles moving the robot on the table.
    It ensures the robot stays within the table boundaries and
    moves according to its current direction.
"""

from toyrobot.position import Position

class RobotMover:
    def move(self, distance, robot, table):
        """
        Moves the robot forward by the specified distance.
        """
        # Calculate the new position based on the robot's current position and facing angle
        new_position = robot.position.move_in_direction(distance, robot.facing_angle)
        
        # Constrain the position to the table dimensions (0-indexed, so max is length-1 or width-1)
        constrained_position = new_position.constrain_to_bounds(0, table.length-1, 0, table.width-1)
        robot.position = constrained_position
    
    def move_one_space(self, robot, table):
        """Moves the robot only 1 space forward as required in this implementation."""
        self.move(1, robot, table)