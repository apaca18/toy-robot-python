"""
Filename: robot_placer.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    This module handles placing the robot on the table at a specific position
    and orientation. It validates that the placement is within the table boundaries
    and that the direction is valid.
"""

from toyrobot.position import Position

class RobotPlacer:
    def place(self, string, robot, table):
        """
        Places the robot at the specified position and direction.
        """
        position_arguments = string.split(',')  # splits the string by the commas
        try:
            x_coord = int(position_arguments[0])
            y_coord = int(position_arguments[1])
            facing_direction = str(position_arguments[2].rstrip())
            
            # Ensure that the x and y values are on the tabletop (0-indexed, so max is length-1 or width-1)
            if 0 <= x_coord < table.length and 0 <= y_coord < table.width:
                robot.facing_angle = robot.directions[facing_direction]
                robot.position = Position(x_coord, y_coord)
            else:
                raise ValueError("Placement out of table bounds.")
        except (IndexError, ValueError, KeyError) as e:
            raise ValueError(f"Invalid PLACE command: {string}. Error: {e}")