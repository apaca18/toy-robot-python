"""
Filename: table.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    This module defines the Table class representing the tabletop surface
    on which the robot moves. The table has a defined width and length.
"""

class Table:
    def __init__(self,width,length):
        """ 
        Initialises a Table object with a defined width and length.
        
        The table is a grid with coordinates from (0,0) to (length-1, width-1).
        For example, a 5x5 table has coordinates from (0,0) to (4,4).
        """
        self.width = width  # North-South direction
        self.length = length  # East-West direction