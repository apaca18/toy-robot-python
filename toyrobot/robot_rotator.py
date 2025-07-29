"""
Filename: robot_rotator.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    This module handles the rotation operations for the robot.
    It supports rotating the robot left (90 degrees counterclockwise),
    right (90 degrees clockwise), or by any arbitrary angle.
"""
    
class RobotRotator:
    def rotate(self, robot, rotation_angle):
        """
        Rotates the robot by the specified angle.

        Args:
            robot: The robot object to rotate.
            rotation_angle (float): The angle to rotate the robot, in degrees.
                - Positive values rotate counterclockwise.
                - Negative values rotate clockwise.

        Notes:
        - The robot's facing angle is normalized to the range [0, 360).
        - 0° corresponds to East, and the positive direction is counterclockwise.
        """
        robot.facing_angle = (robot.facing_angle + rotation_angle) % 360
        
    def left(self, robot):
        """
        Rotates the robot 90 degrees counterclockwise.
        """
        self.rotate(robot, 90)
        
    def right(self, robot):
        """
        Rotates the robot 90 degrees clockwise (or -90 degrees counterclockwise).
        """
        self.rotate(robot, -90)
