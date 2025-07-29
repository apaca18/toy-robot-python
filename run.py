# -*- coding: utf-8 
#----------------------------------------------------------------------------
# Created By  Aaron PAcanowski 
# Created Date: 17/7/2025
# version ='1.0'
# ---------------------------------------------------------------------------
"""Toy Robot Challenge"""
# ---------------------------------------------------------------------------

from toyrobot.robot import Robot
from toyrobot.robot_rotator import RobotRotator
from toyrobot.robot_reporter import RobotReporter
from toyrobot.table import Table
from toyrobot.robot_placer import RobotPlacer
from toyrobot.robot_mover import RobotMover
import sys
import json

def load_config():
    """
    Loads the configuration from the config.json file.
    """
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("Error: config.json file not found. Using default configuration.")
        return {
            "table_size": {"width": 5, "length": 5},
            "directions": {"NORTH": 90, "EAST": 0, "SOUTH": 270, "WEST": 180}
        }
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse config.json - {e}. Using default configuration.")
        return {
            "table_size": {"width": 5, "length": 5},
            "directions": {"NORTH": 90, "EAST": 0, "SOUTH": 270, "WEST": 180}
        }

def process_command(command, robot, table):
    """Process a single command for the robot."""
    command = command.strip()
    if not command:
        return
        
    split_command = command.split(' ')
    first_word = split_command[0].strip().upper()
    
    if first_word == "PLACE" and len(split_command) > 1:
        place_arguments = split_command[1]
        try:
            robot.robot_placer.place(place_arguments, robot, table)
        except Exception as e:
            print(f"Error: Invalid PLACE command - {e}")
    elif robot.position is None:
        print("Command ignored: Robot not placed on the table.")
    else:
        if first_word == "MOVE":
            try:
                robot.robot_mover.move_one_space(robot, table)
            except Exception as e:
                print(f"Error during MOVE command: {e}")
        elif first_word == "RIGHT":
            try:
                robot.robot_rotator.right(robot)
            except Exception as e:
                print(f"Error during RIGHT command: {e}")
        elif first_word == "LEFT":
            try:
                robot.robot_rotator.left(robot)
            except Exception as e:
                print(f"Error during LEFT command: {e}")
        elif first_word == "REPORT":
            try:
                robot.robot_reporter.report(robot)
            except Exception as e:
                print(f"Error during REPORT command: {e}")
        elif first_word == "EXIT":
            print("Goodbye!")
            sys.exit(0)
        else:
            print(f"Error: Unknown command '{first_word}'")

def main():
    config = load_config()
    table_size = config["table_size"]
    directions = config["directions"]
    
    # Initialize table and robot components
    table = Table(table_size["width"], table_size["length"])
    robot_rotator = RobotRotator()
    robot_reporter = RobotReporter()
    robot_placer = RobotPlacer()
    robot_mover = RobotMover()
    
    # Create the robot
    robot = Robot(directions, robot_rotator, robot_reporter, 
                 table, robot_placer, robot_mover)
    
    # Check if a file was provided as an argument
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1]) as f:
                lines = f.readlines()
                for line in lines:
                    process_command(line, robot, table)
        except FileNotFoundError:
            print(f"File {sys.argv[1]} not found.")
            return
        except Exception as e:
            print(f"Error processing file: {e}")
    else:
        # Interactive mode
        print("Toy Robot Simulator")
        print("Available commands: PLACE X,Y,F | MOVE | LEFT | RIGHT | REPORT | EXIT")
        print("Type EXIT to quit")
        
        while True:
            try:
                command = input("Enter command: ")
                process_command(command, robot, table)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()