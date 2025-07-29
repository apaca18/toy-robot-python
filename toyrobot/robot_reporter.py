"""
Filename: robot_reporter.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    This module handles reporting the robot's position and direction.
    It formats and outputs the robot's state in the specified format: X,Y,DIRECTION.
"""

class RobotReporter:
    def report(self, robot):
        """
        Reports the current position and direction of the robot.
        Prints in the format "X,Y,DIRECTION" (e.g. "0,1,NORTH").

        Notes:
        - The robot's facing angle is normalized to the range [0, 360).
        - 0° corresponds to East, and the positive direction is counterclockwise.
        """
        if robot.position is None:
            return  # Robot is not on the table

        # Get the position coordinates
        x_coord = robot.position.x
        y_coord = robot.position.y
        
        # Normalize the facing angle to be between 0 and 360 degrees
        robot.facing_angle %= 360
        
        # Get the direction name from the angle
        facing_direction = self.get_key_from_directions_dict(robot.facing_angle, robot)
        
        # Print the position report
        print(f"{x_coord},{y_coord},{facing_direction}")
    
    def get_key_from_directions_dict(self, val, robot):
        """
        Retrieves the key (direction name) from the directions dictionary
        based on the given angle.

        Args:
            val (float): The angle in degrees.
            robot: The robot object containing the directions dictionary.

        Returns:
            str: The direction name (e.g., "NORTH").
        """
        for key, value in robot.directions.items():
             if val == value:
                 return key
