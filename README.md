# Week Five Python Assignment

This assignment consists of two parts: designing a class with inheritance and exploring polymorphism with animals.

## Part 1: Smartphone Class Design 🏗️

### Description
This part of the assignment involves creating a `Smartphone` base class and a `GamingPhone` inherited class to demonstrate object-oriented programming concepts like attributes, methods, constructors, and inheritance.

### Classes
1. **Smartphone (Base Class)**
   - **Attributes**: brand, model, storage
   - **Methods**: 
     - `call(number)`: Simulates calling a number
     - `info()`: Displays phone information

2. **GamingPhone (Inherited Class)**
   - **Additional Attribute**: cooling_system
   - **Overridden Method**: `info()` to include cooling system information

### How to Run
1. Ensure you have Python installed on your system.
2. Save the `smartphones.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `smartphones.py`.
5. Run the program using the command:
   ```
   python smartphones.py
   ```

### Example Output
```
Brand: Samsung, Model: Galaxy S24, Storage: 256GB
Samsung Galaxy S24 is calling 123456789 📞
Gaming Phone - Asus ROG Phone 7, 512GB, Cooling: Liquid Cooling
Asus ROG Phone 7 is calling 987654321 📞
```

## Part 2: Polymorphism Challenge 🎭

### Description
This part demonstrates polymorphism by creating animal classes that all have a `move()` method, but each implements it differently.

### Classes
1. **Animal (Base Class)**
   - **Method**: `move()` with a generic message

2. **Dog (Derived Class)**
   - **Overridden Method**: `move()` to print "Dog runs on four legs 🐕"

3. **Bird (Derived Class)**
   - **Overridden Method**: `move()` to print "Bird flies in the sky 🕊️"

4. **Fish (Derived Class)**
   - **Overridden Method**: `move()` to print "Fish swims in water 🐟"

### How to Run
1. Ensure you have Python installed on your system.
2. Save the `animals.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `animals.py`.
5. Run the program using the command:
   ```
   python animals.py
   ```

### Example Output
```
Dog runs on four legs 🐕
Bird flies in the sky 🕊️
Fish swims in water 🐟
```

## Key Concepts Demonstrated
- **Class Design**: Creating classes with attributes and methods
- **Constructors**: Using `__init__` to initialize objects with unique values
- **Inheritance**: Creating a derived class that inherits from a base class
- **Polymorphism**: Different classes implementing the same method in different ways
- **Method Overriding**: A derived class providing a specific implementation of a method already defined in its base class
