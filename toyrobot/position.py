"""
Filename: position.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    This module provides a Position class that abstracts the representation
    of a 2D position using complex numbers. It simplifies position manipulation
    without requiring knowledge of complex number mathematics.
"""
import cmath
import math

class Position:
    def __init__(self, x=0, y=0):
        """
        Initialize a position with x and y coordinates.
        
        Args:
            x (int): X coordinate (East-West)
            y (int): Y coordinate (North-South)
        """
        self._complex_pos = complex(x, y)
    
    @property
    def x(self):
        """Get the x coordinate (East-West position)."""
        return round(self._complex_pos.real)
    
    @property
    def y(self):
        """Get the y coordinate (North-South position)."""
        return round(self._complex_pos.imag)
    
    def move_in_direction(self, distance, angle_degrees):
        """
        Move the position in the specified direction for the given distance.
        
        Args:
            distance (float): Distance to move.
            angle_degrees (float): Direction angle in degrees (0=East, 90=North, etc.).
            
        Returns:
            Position: A new Position object representing the moved position.

        Notes:
        - 0° corresponds to East, and the positive direction is counterclockwise.
        """
        # Convert angle to radians and calculate the new position using polar form
        radians = math.radians(angle_degrees)
        new_complex = self._complex_pos + cmath.rect(distance, radians)
        
        # Create and return new Position object
        new_position = Position()
        new_position._complex_pos = new_complex
        return new_position
    
    def constrain_to_bounds(self, min_x, max_x, min_y, max_y):
        """
        Ensure position stays within the specified bounds
        
        Args:
            min_x (int): Minimum allowed x coordinate
            max_x (int): Maximum allowed x coordinate
            min_y (int): Minimum allowed y coordinate
            max_y (int): Maximum allowed y coordinate
            
        Returns:
            Position: A new Position object constrained to the bounds
        """
        # Constrain x and y to the specified ranges
        constrained_x = min(max(min_x, self.x), max_x)
        constrained_y = min(max(min_y, self.y), max_y)
        
        # Create and return a new Position with constrained coordinates
        return Position(constrained_x, constrained_y)
    
    def __str__(self):
        """String representation of position as 'x,y'"""
        return f"{self.x},{self.y}"
