"""
Filename: test_position.py
Author: Aaron Pacanowski
Email: aaronpaca@gmail.com
Date: 2025-07-28
Description:
    Test suite for the Position class. Validates that positions can be
    created, moved in various directions, and constrained to table boundaries.
"""
import unittest
import math
from parameterized import parameterized
from toyrobot.position import Position

class TestPosition(unittest.TestCase):
    @parameterized.expand([
        ("origin", 0, 0),
        ("positive_coordinates", 4, 4),
        ("negative_coordinates", -3, -7), # for extensibility
        ("mixed_coordinates", -5, 4), # for extensibility
    ])
    def test_initial_position(self, name, x, y):
        pos = Position(x, y)
        self.assertEqual(pos.x, x)
        self.assertEqual(pos.y, y)

    @parameterized.expand([
        # name, start_x, start_y, distance, angle, expected_x, expected_y
        ("move_north", 0, 0, 1, 90, 0, 1),  # Move 1 unit North
        ("move_east", 0, 0, 1, 0, 1, 0),    # Move 1 unit East
        ("move_south", 0, 0, 1, 270, 0, -1), # Move 1 unit South
        ("move_west", 0, 0, 1, 180, -1, 0),  # Move 1 unit West
        ("move_northeast", 0, 0, math.sqrt(2), 45, 1, 1),  # Move diagonal NE
        ("move_multiple_units", 0, 0, 3, 0, 3, 0),  # Move 3 units East
        ("move_from_non_origin", 4, 4, 2, 90, 4, 6),  # Changed from 5,5 to 4,4 (valid start position)
    ])
    def test_move_in_direction(self, name, start_x, start_y, distance, angle, expected_x, expected_y):
        pos = Position(start_x, start_y)
        new_pos = pos.move_in_direction(distance, angle)
        self.assertAlmostEqual(new_pos.x, expected_x)
        self.assertAlmostEqual(new_pos.y, expected_y)

    @parameterized.expand([
        # name, pos_x, pos_y, min_x, max_x, min_y, max_y, expected_x, expected_y
        ("within_bounds", 2, 3, 0, 4, 0, 4, 2, 3), 
        ("exceed_max_x", 7, 3, 0, 4, 0, 4, 4, 3),   
        ("exceed_max_y", 2, 8, 0, 4, 0, 4, 2, 4),  
        ("below_min_x", -2, 3, 0, 4, 0, 4, 0, 3),   
        ("below_min_y", 2, -1, 0, 4, 0, 4, 2, 0),   
        ("exceed_all_bounds", 10, 10, 0, 4, 0, 4, 4, 4), 
    ])
    def test_constrain_to_bounds(self, name, pos_x, pos_y, min_x, max_x, min_y, max_y, expected_x, expected_y):
        pos = Position(pos_x, pos_y)
        constrained_pos = pos.constrain_to_bounds(min_x, max_x, min_y, max_y)
        self.assertEqual(constrained_pos.x, expected_x)
        self.assertEqual(constrained_pos.y, expected_y)

    def test_str_representation(self):
        pos = Position(3, 4)
        self.assertEqual(str(pos), "3,4")

    def test_equality(self):
        pos1 = Position(3, 4)
        pos2 = Position(3, 4)
        pos3 = Position(4, 3)
        
        # Test comparison using x and y attributes
        self.assertEqual(pos1.x, pos2.x)
        self.assertEqual(pos1.y, pos2.y)
        self.assertNotEqual(pos1.x, pos3.x)
        self.assertNotEqual(pos1.y, pos3.y)

    def test_rounding(self):
        # Test that positions with floating point values are rounded correctly
        pos = Position(1.4, 2.7)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 3)  # 2.7 should be rounded to 3

if __name__ == "__main__":
    unittest.main()
