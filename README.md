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


**Main Program**:
- `Task.py`: The main application file. Contains the GUI setup, function parsing, plotting logic, and application styles.

**test_Plotting.py (Provide a Predefined Inputs to check the validation of the Application)**:
- `test_invalid_func_format.py`: Test function for invalid function formats **( Failed Test )**.
- `test_valid_func_format.py`: Test function for valid function formats **( Passed Test )**.
- `test_valid_X_values.py`: Test function for valid x-values  **( Passed Test )**.
- `test_invalid_X_values.py`: Test function for invalid x-values **( Failed Test )**.
  

## Requirements

- ***Python 3.10.11***

### To Run App And Install the required libraries:
- Open a terminal or command prompt.
- Install Virtual Environment  `pip install virtualenv`.
- Create a Virtual Environment `virtualenv myenv`.
- Activate the Virtual Environment `myenv\Scripts\activate`.
- Navigate to the directory where the project files `cd path/to/your/project`.
- ***Installing Requirements*** `pip install -r requirements.txt`.
- Finally run the App `python Task.py`

### To Run Automated Tests :
- Open a terminal or command prompt.
- Navigate to the directory where the project files cd `path/to/your/project`.
- Run the tests By Putting  `pytest`   in the terminal.
- ***DO NOT CLOSE THE APP***
