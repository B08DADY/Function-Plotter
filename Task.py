import sys
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

########################################################################################
########################################################################################


# Function to get and validate X values
def GetMaxMinX ():
    min_x_str = minx_entry.text()
    max_x_str = maxx_entry.text()

    # validate The values of the X
    try:
        min_x = float(min_x_str)
        max_x = float(max_x_str)
        if min_x >= max_x:
            QMessageBox.critical(window, "Input Error", "XMin must be less than XMax .")
            return min_x, max_x
    except ValueError as e:
        QMessageBox.critical(window, "Input Error", "x Must Be A Number Value")
        return min_x, max_x
    return min_x, max_x


########################################################################################
########################################################################################

# Function to plot a function of x
def PlotFunction():
    func_str = func_entry.text().lower()
    # Convert ^ to ** for Python evaluation
    func_str = func_str.replace("^", "**")
    # Validate and parse the function

    try:

        x = sp.symbols('x')
        func = sp.sympify(func_str, locals={'log10': sp.log, 'lg10': sp.log, 'lg': sp.log, 'sqrt': sp.sqrt, 'root': sp.sqrt})

    except sp.SympifyError:
        QMessageBox.critical(window, "Input Error", "Invalid function format,Please Try Agian with correct format like \"x^5+x*3...\"")
        return


    #Get the values of the min and max x
    min_x,max_x=GetMaxMinX()

    # Generate x values and evaluate the function
    x_vals = np.linspace(min_x, max_x, 400)
    try:
         y_vals = [float(func.evalf(subs={x: val})) for val in x_vals]
    except (TypeError, ValueError):
        QMessageBox.critical(window, "Input Error", "Mathematical Error:\nPlease Recheck The X values and The Function format ")
        return

    except ZeroDivisionError:
        QMessageBox.critical(window, "Input Error", "You Can't Devide on Zero:\nPlease Cahnge the function or the X values ")
        return

    # Clear any previous plot
    ax.clear()

    # Take x values and y values and plotting it
    ax.plot(x_vals, y_vals)
    ax.set_title(f"Plotting of ({func_entry.text().lower()})", color="green", fontsize=20)
    ax.set_xlabel("(x)", color="green", fontsize=15)
    ax.set_ylabel("(f(x))", color="green", fontsize=15)
    ax.grid(True)

    # Draw the canvas
    canvas.draw()


########################################################################################
########################################################################################

# Set Upp The window

app = QApplication([])

# Function to handle exit button click
def exit_application():
    app.quit()

# Set dark mode stylesheet with custom button and label styling
dark_stylesheet = """
    QWidget {
        background-color: #2E2E2E;
        color: #E0E0E0;
    }
    QLabel {
        color: #00FF00; /* Green color */
        font-weight: bold;
        font-size: 24px; /* Larger font size */
        font-family: Arial; /* Elegant font type */
    }
    QLineEdit {
        background-color: #3E3E3E;
        color: #E0E0E0;
        border: 1px solid #5A5A5A;
        padding: 5px;
        font-size: 14px;
    }
    QPushButton {
        background-color: #4E4E4E;
        color: #E0E0E0;
        border: 1px solid #5A5A5A;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #5A5A5A;
    }
    QPushButton#plotButton {
        background-color: green;
        color: white;
    }
    QPushButton#plotButton:hover {
        background-color: darkgreen;
    }
    QPushButton#exitButton {
        background-color: #FF0000; /* Red color */
        color: white;
    }
    QPushButton#exitButton:hover {
        background-color: #FF3333; /* Lighter red color on hover */
    }
"""

app.setStyleSheet(dark_stylesheet)

# Create the main window
window = QWidget()
window.setWindowTitle("Function Plotter")

# Set the window to full screen
window.showFullScreen()

# Set the main layout
main_layout = QVBoxLayout(window)

# Add a title label with custom styling
title_label = QLabel("Function Plotter")
title_label.setFont(QFont("Arial", 24, QFont.Bold))
title_label.setAlignment(Qt.AlignCenter)
main_layout.addWidget(title_label)

# Create a form layout for input fields
form_layout = QFormLayout()

# Function entry
func_entry = QLineEdit()
func_entry.setObjectName("func_entry")  # Set the object name
func_entry.setPlaceholderText("f(x): x+5 , log10(x) , sqrt(x) , x*10 , x^2.....")
form_layout.addRow("Enter function of x:", func_entry)

# Min x entry
minx_entry = QLineEdit()
minx_entry.setObjectName("minx_entry")  # Set the object name
minx_entry.setPlaceholderText("MIN x")
form_layout.addRow("Min x:", minx_entry)

# Max x entry
maxx_entry = QLineEdit()
maxx_entry.setObjectName("maxx_entry")  # Set the object name
maxx_entry.setPlaceholderText("MAX x")
form_layout.addRow("Max x:", maxx_entry)

# Add form layout to the main layout
main_layout.addLayout(form_layout)

# Matplotlib integration
fig, ax = plt.subplots()
canvas = FigureCanvas(fig)
main_layout.addWidget(canvas)

# Plot button with plot_function command
plot_button = QPushButton("Plotting")
plot_button.setObjectName("plotButton")
plot_button.clicked.connect(PlotFunction)
plot_button.setStyleSheet("""
    QPushButton#plotButton {
        background-color: green;
        color: white;
        border: none;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton#plotButton:hover {
        background-color: darkgreen;
    }
""")
main_layout.addWidget(plot_button)

# Exit button at the top right corner
exit_button = QPushButton("Exit")
exit_button.setObjectName("exitButton")
exit_button.clicked.connect(exit_application)
exit_button.setStyleSheet("""
    QPushButton#exitButton {
        background-color: #FF0000; /* Red color */
        color: white;
        border: none;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton#exitButton:hover {
        background-color: #FF3333; /* Lighter red color on hover */
    }
""")
exit_button.setMaximumWidth(100)  # Set a fixed width for the exit button
main_layout.addWidget(exit_button, alignment=Qt.AlignTop | Qt.AlignRight)

# Adjust subplot parameters to reduce white space around the plot
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

# Start the application event loop
window.show()

########################################################################################
########################################################################################


# Initiate The Application
def initialize_application():
    global app  # Make app global (optional)
    if not app:  # Check if app already exists
        app = QApplication([])


########################################################################################
########################################################################################


# Call initialize_application() when needed
if __name__ == '__main__':
    initialize_application()
    sys.exit(app.exec_())