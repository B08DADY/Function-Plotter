# Function Plotter Application

## Overview

This project is a Function Plotter application built using PySide2 and matplotlib.
The application allows users to input a mathematical function and plot it within a specified range of x-values.
The project also includes automated tests using pytest and QtBot to ensure the application's functionality and reliability.

## Features

- **Function Input:** Enter a mathematical function in various formats (e.g., `x^2`, `sqrt(x)`, `x*10`).
- **Range Specification:** Define the minimum and maximum x-values for the plot.
- **Plot Generation:** Generates and displays the plot based on user inputs.
- **Error Handling:** Provides informative error messages for invalid input.

## Project Structure

**Main Program
    - `Task.py`: The main application file. Contains the GUI setup, function parsing, plotting logic, and application styles.
    
**Tests (Provide a Predefined Inputs to check the validation of the Application)
    - `test_valid_func_format.py`: Tests for valid function formats.
    - `test_invalid_func_format.py`: Tests for invalid function formats.
    - `test_valid_X_values.py`: Tests for valid x-values.
    - `test_invalid_X_values.py`: Tests for invalid x-values.


## Requirements

- Python 3.10.11

### Install the required libraries:

```bash
pip install -r requirements.txt
