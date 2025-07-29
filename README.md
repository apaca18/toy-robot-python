# Toy Robot Simulator

**Author**: Aaron Pacanowski  
**Email**: aaronpaca@gmail.com  
**Phone**: +61468451613  
**Date**: 28/7/2025

A command-line application that simulates a toy robot moving on a square tabletop.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Table Dimensions](#table-dimensions)
- [Usage](#usage)
  - [Interactive Mode](#interactive-mode)
  - [File Input Mode](#file-input-mode)
- [Example Scenarios](#example-scenarios)
- [Project Structure](#project-structure)
- [Design Decisions](#design-decisions)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)

## Description

This application is a simulation of a toy robot moving on a square tabletop of dimensions 5x5 units. The robot is free to roam around the surface of the table, but is prevented from falling to destruction.

The application can read in commands in the following form:

```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```

- `PLACE` will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
- `MOVE` will move the toy robot one unit forward in the direction it is currently facing.
- `LEFT` and `RIGHT` will rotate the robot 90 degrees in the specified direction without changing the position.
- `REPORT` will announce the X,Y and orientation of the robot.
- `EXIT` will quit the application.

## Requirements

- Python 3.6 or higher (tested with Python 3.11.7)

## Installation

No installation is required. Just clone the repository:

```
git clone https://github.com/apaca18/toy-robot-python.git
cd toy-robot-python
```

## Configuration

The application uses a single configuration file, `config.json`, to define the table size and directions.

### Example `config.json`

```json
{
  "table_size": {
    "width": 5,
    "length": 5
  },
  "directions": {
    "NORTH": 90,
    "EAST": 0,
    "SOUTH": 270,
    "WEST": 180
  }
}
```

Modify this file to customise the table size or directions.

## Table Dimensions

The table is a 5x5 grid with coordinates from (0,0) to (4,4). The origin (0,0) is the south-west corner.

```
y
^
4 . . . . .
3 . . . . .
2 . . . . .
1 . . . . .
0 . . . . .
  0 1 2 3 4 -> x
```

Any attempt to move the robot off the table (i.e., to coordinates where x < 0, y < 0, x > 4, or y > 4) will be prevented.

## Usage

### Interactive Mode

Run the application in interactive mode:

```
python run.py
```

Enter commands at the prompt.

### File Input Mode

Run the application with a file containing commands:

```
python run.py examples/example1.txt
```

## Example Scenarios

The following example files are provided in the `examples` directory to test various scenarios:

### **Example 1: Basic Movement**
- **File**: `examples/example1.txt`
- **Description**: Tests basic placement, movement, and reporting.
- **Input**:
  ```
  PLACE 0,0,NORTH
  MOVE
  REPORT
  ```
- **Expected Output**:
  ```
  0,1,NORTH
  ```

---

### **Example 2: Rotation**
- **File**: `examples/example2.txt`
- **Description**: Tests placement, rotation (LEFT), and reporting.
- **Input**:
  ```
  PLACE 0,0,NORTH
  LEFT
  REPORT
  ```
- **Expected Output**:
  ```
  0,0,WEST
  ```

---

### **Example 3: Complex Movement**
- **File**: `examples/example3.txt`
- **Description**: Tests placement, movement, rotation (LEFT), and reporting.
- **Input**:
  ```
  PLACE 1,2,EAST
  MOVE
  MOVE
  LEFT
  MOVE
  REPORT
  ```
- **Expected Output**:
  ```
  3,3,NORTH
  ```

---

### **Example 4: Edge Movement**
- **File**: `examples/example4.txt`
- **Description**: Tests movement to the edge of the table and ensures the robot does not fall off.
- **Input**:
  ```
  PLACE 1,2,NORTH
  LEFT
  MOVE
  MOVE
  MOVE
  MOVE
  MOVE
  MOVE
  MOVE
  MOVE
  MOVE
  MOVE
  REPORT
  ```
- **Expected Output**:
  ```
  0,2,WEST
  ```

---

### **Example 5: Moving to the Edge**
- **File**: `examples/example5.txt`
- **Description**: Tests movement to the edge of the table in different directions.
- **Input**:
  ```
  PLACE 0,0,SOUTH
  MOVE
  REPORT
  PLACE 4,4,EAST
  REPORT
  ```
- **Expected Output**:
  ```
  0,0,SOUTH
  4,4,EAST
  ```

---

### **Example 6: Multiple `PLACE` Commands**
- **File**: `examples/example6.txt`
- **Description**: Tests how the robot handles multiple `PLACE` commands in a sequence.
- **Input**:
  ```
  PLACE 0,0,NORTH
  MOVE
  REPORT
  PLACE 2,2,EAST
  MOVE
  REPORT
  ```
- **Expected Output**:
  ```
  0,1,NORTH
  3,2,EAST
  ```

---

### **Example 7: Invalid Commands**
- **File**: `examples/example7.txt`
- **Description**: Tests how the application handles invalid commands and ignores them.
- **Input**:
  ```
  MOVE
  LEFT
  PLACE 0,0,NORTH
  MOVE
  JUMP
  REPORT
  ```
- **Expected Output**:
  ```
  Command ignored: Robot not placed on the table.
  Command ignored: Robot not placed on the table.
  Error: Unknown command 'JUMP'
  0,1,NORTH
  ```

---

### **Example 8: Full Edge Traversal**
- **File**: `examples/example8.txt`
- **Description**: Tests the robot's ability to traverse the edges of the table.
- **Input**:
  ```
  PLACE 0,0,EAST
  MOVE
  MOVE
  MOVE
  MOVE
  REPORT
  PLACE 4,4,SOUTH
  MOVE
  MOVE
  REPORT
  ```
- **Expected Output**:
  ```
  4,0,EAST
  4,2,SOUTH
  ```

---

### **Example 9: Complex Sequence**
- **File**: `examples/example9.txt`
- **Description**: Tests a complex sequence of commands to ensure the robot behaves as expected.
- **Input**:
  ```
  PLACE 1,1,NORTH
  MOVE
  MOVE
  LEFT
  MOVE
  RIGHT
  MOVE
  REPORT
  ```
- **Expected Output**:
  ```
  0,4,NORTH
  ```

---

### **How to Run Examples**
To run an example, use the following command:

```bash
python run.py examples/example1.txt
```

Replace `example1.txt` with the desired example file.

## Project Structure

```
.
├── coding_test_instructions_2025.md - Original challenge requirements
├── config.json - Configuration for table size and directions
├── examples/ - Example input files
├── run.py - Main application entry point
├── tests/ - Unit tests for the application
│   ├── test_position.py
│   ├── test_robot_mover.py
│   ├── test_robot_placer.py
│   ├── test_robot_reporter.py
│   └── test_robot_rotator.py
├── toyrobot/ - Main application module
│   ├── position.py - Position tracking abstraction
│   ├── robot.py - Main robot class
│   ├── robot_mover.py - Movement logic
│   ├── robot_placer.py - Robot placement logic
│   ├── robot_reporter.py - Position reporting logic
│   ├── robot_rotator.py - Rotation logic
│   └── table.py - Table representation
```

## Design Decisions

### Position Abstraction

The implementation uses a `Position` class that provides an abstraction over complex numbers for position tracking. This provides:

1. Simple x,y coordinate access
2. Movement calculations that hide complex number math
3. Clear bounds-checking to prevent falling off the table
4. Intuitive methods for movement and position manipulation

### Modular Design

The application follows SOLID principles with:

1. Single Responsibility Principle: Each class has a specific purpose
2. Open/Closed Principle: New functionality can be added without modifying existing code
3. Dependency Injection: Components are passed to the Robot constructor

## Testing

To run the tests, use the following command:

```
PYTHONPATH=. python -m unittest discover -s tests
```

This will execute all the test files in the `tests/` directory.

## Future Enhancements

- Support for additional commands
- Support for multiple robots
- Support for obstacles on the table
