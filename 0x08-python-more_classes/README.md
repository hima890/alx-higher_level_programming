# Rectangle

## Table of Contents
* [Description](#description)
* [Files](#files)
* [Tasks](#tasks)
  * [0. Simple rectangle](#0-simple-rectangle)
  * [1. Real definition of a rectangle](#1-real-definition-of-a-rectangle)
  * [2. Area and Perimeter](#2-area-and-perimeter)
  * [3. String representation](#3-string-representation)
  * [4. Eval is magic](#4-eval-is-magic)
  * [5. Detect instance deletion](#5-detect-instance-deletion)
  * [6. How many instances](#6-how-many-instances)
  * [7. Change representation](#7-change-representation)
  * [8. Compare rectangles](#8-compare-rectangles)
  * [9. A square is a rectangle](#9-a-square-is-a-rectangle)

## Description
This repository contains Python scripts and classes related to rectangles and their operations.

## Files
* `0-rectangle.py`: Defines an empty class `Rectangle`.
* `1-rectangle.py`: Defines a class `Rectangle` with private instance attributes `width` and `height`, and initializes them with optional parameters in the constructor.
* `2-rectangle.py`: Adds methods `area` and `perimeter` to the `Rectangle` class to calculate the area and perimeter of the rectangle.
* `3-rectangle.py`: Enhances the `Rectangle` class with string representation methods `__str__` and `__repr__` to print the rectangle using `#` symbols.
* `4-rectangle.py`: Extends the `Rectangle` class to include a static method `bigger_or_equal` that compares two rectangles and returns the one with the bigger area.
* `5-rectangle.py`: Adds functionality to print a message when a `Rectangle` instance is deleted.
* `6-rectangle.py`: Updates the `Rectangle` class to include a class attribute `number_of_instances` that keeps track of the number of instances created and destroyed.
* `7-rectangle.py`: Adds a public class attribute `print_symbol` to customize the symbol used for string representation of the rectangle.
* `8-rectangle.py`: Introduces a class method `square(cls, size=0)` to create a square `Rectangle` instance with equal width and height.
* `9-rectangle.py`: Implements the `Rectangle` class with additional methods and attributes as specified in the tasks.

## Tasks

### 0. Simple rectangle
Defines an empty class `Rectangle` that represents a rectangle.

### 1. Real definition of a rectangle
Defines a class `Rectangle` with private instance attributes `width` and `height`, and initializes them with optional parameters in the constructor.

### 2. Area and Perimeter
Enhances the `Rectangle` class with methods `area` and `perimeter` to calculate the area and perimeter of the rectangle.

### 3. String representation
Updates the `Rectangle` class to include string representation methods `__str__` and `__repr__` to print the rectangle using `#` symbols.

### 4. Eval is magic
Extends the `Rectangle` class to include a static method `bigger_or_equal` that compares two rectangles and returns the one with the bigger area.

### 5. Detect instance deletion
Adds functionality to print a message when a `Rectangle` instance is deleted.

### 6. How many instances
Updates the `Rectangle` class to include a class attribute `number_of_instances` that keeps track of the number of instances created and destroyed.

### 7. Change representation
Adds a public class attribute `print_symbol` to the `Rectangle` class to customize the symbol used for string representation of the rectangle.

### 8. Compare rectangles
Introduces a static method `bigger_or_equal` to the `Rectangle` class that compares two rectangles and returns the one with the bigger area.

### 9. A square is a rectangle
Implements the `Rectangle` class with additional methods and attributes as specified in the task. Specifically, adds a class method `square(cls, size=0)` to create a square `Rectangle` instance with equal width and height.