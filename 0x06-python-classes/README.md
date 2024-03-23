**README.md**

# Python Classes - Square

In this project, we will create a series of Python classes to define and manipulate squares. Each task will build upon the previous one, adding new features and functionality to our Square class.

## 0. Square with Size
**File:** `0-square.py`

We begin by defining an empty class `Square` that represents a square. The class is intentionally left empty to fulfill the requirements of the task. No methods or attributes are defined at this stage.

Example Usage:
```python
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))  # Output: <class '0-square.Square'>
print(my_square.__dict__)  # Output: {}
```

## 1. Square with Size
**File:** `1-square.py`

In this task, we enhance the `Square` class by adding a private instance attribute `size`. The `size` attribute represents the side length of the square. We provide instantiation with a size parameter but no type or value verification is performed at this stage.

Example Usage:
```python
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))  # Output: <class '1-square.Square'>
print(my_square.__dict__)  # Output: {'_Square__size': 3}
```

## 2. Size Validation
**File:** `2-square.py`

Here, we add validation to the `size` attribute of the `Square` class. The size must be an integer and greater than or equal to 0. If the provided size is invalid, appropriate exceptions are raised.

Example Usage:
```python
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(my_square_1.size)  # Output: 3

my_square_2 = Square()
print(my_square_2.size)  # Output: 0

my_square_3 = Square("3")  # Raises TypeError: size must be an integer
my_square_4 = Square(-89)  # Raises ValueError: size must be >= 0
```

## 3. Area of a Square
**File:** `3-square.py`

In this task, we implement a public instance method `area()` that calculates and returns the area of the square based on its size attribute.

Example Usage:
```python
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area:", my_square_1.area())  # Output: Area: 9

my_square_2 = Square(5)
print("Area:", my_square_2.area())  # Output: Area: 25
```

## 4. Access and Update Private Attribute
**File:** `4-square.py`

We introduce getter and setter methods for the `size` attribute of the `Square` class. This allows controlled access and modification of the private attribute, enforcing type and value validation.

Example Usage:
```python
Square = __import__('4-square').Square

my_square = Square(89)
print("Area:", my_square.area(), "for size:", my_square.size)  # Output: Area: 7921 for size: 89

my_square.size = 3
print("Area:", my_square.area(), "for size:", my_square.size)  # Output: Area: 9 for size: 3

my_square.size = "5 feet"  # Raises TypeError: size must be an integer
```

## 5. Printing a Square
**File:** `5-square.py`

We implement a public instance method `my_print()` that prints a square using the `#` character. The size of the square determines the number of `#` characters in each row.

Example Usage:
```python
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()
# Output:
# ###
# ###
# ###

my_square.size = 10
my_square.my_print()
# Output: (square of size 10)

my_square.size = 0
my_square.my_print()
# Output:
#
```

## 6. Coordinates of a Square
**File:** `6-square.py`

The `Square` class now includes a private instance attribute `position` representing the top-left corner of the square. We enhance the `my_print()` method to support printing squares at specified positions.

Example Usage:
```python
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()
# Output:
# ###
# ###
# ###

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()
# Output: (square of size 3 with position (1, 1))

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()
# Output: (square of size 3 with position (3, 0))
```