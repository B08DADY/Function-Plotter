import pytest
from PySide2.QtTest import QTest
from PySide2.QtWidgets import QApplication, QPushButton, QMessageBox
from PySide2.QtCore import QTimer, Qt
from Task import window, func_entry, minx_entry, maxx_entry, PlotFunction

########################################################################################
########################################################################################

## PLEASE RELAX AND SEE THE MAGIC JUST RUN "pytest" AND WATCH THE TESTS
##                (((  DO NOT CLOSE THE APP  )))

########################################################################################
########################################################################################

@pytest.fixture
def setup_qt(qtbot):
    """Fixture to initialize the Qt application and provide a test bot."""
    qtbot.addWidget(window)
    window.show()  # Ensure the window is visible
    yield qtbot
    window.close()  # Ensure the window is closed after tests

########################################################################################
########################################################################################
def get_message_boxes():
    """Helper function to retrieve all QMessageBox instances."""
    return [w for w in QApplication.topLevelWidgets() if isinstance(w, QMessageBox)]

def assert_message_box_text_contains(expected_text):
    """Assert that a QMessageBox with the expected text appears."""
    msg_boxes = get_message_boxes()
    assert any(expected_text in msg.text() for msg in msg_boxes), f"Error message containing '{expected_text}' not found"


########################################################################################
########################################################################################

#                       TEST FOR CHECKING THE INVALID FUNCTION FORMAT

def test_invalid_func_format(qtbot):
    # Set invalid function format
    func_entry.setText("x++")
    minx_entry.setText("0")
    maxx_entry.setText("10")

    # Click the plot button
    plot_button = window.findChild(QPushButton, "plotButton")
    QTest.mouseClick(plot_button, Qt.LeftButton)
    qtbot.wait(2000)


    # Check for error message
    assert_message_box_text_contains("Invalid function format")

########################################################################################
########################################################################################

#                         TEST FOR CHECKING THE INVALID X VALUES

def test_invalid_X_values(qtbot):
    # Set invalid X values
    func_entry.setText("x+5")
    minx_entry.setText("10")
    maxx_entry.setText("0")

    # Click the plot button
    plot_button = window.findChild(QPushButton, "plotButton")
    QTest.mouseClick(plot_button, Qt.LeftButton)
    qtbot.wait(2000)


    # Check for error message
    assert_message_box_text_contains("XMin must be less than XMax")

########################################################################################
########################################################################################

#                       TEST FOR CHECKING THE INVALID FUNCTION FORMAT


def test_valid_func_format(qtbot):
    # Set valid function format
    func_entry.setText("x^2")
    minx_entry.setText("-10")
    maxx_entry.setText("10")

    # Click the plot button
    plot_button = window.findChild(QPushButton, "plotButton")
    QTest.mouseClick(plot_button, Qt.LeftButton)
    qtbot.wait(2000)


    # Check that no error message is shown
    msg_boxes = get_message_boxes()
    assert not any("Input Error" in msg.text() for msg in msg_boxes), "Unexpected error message for valid function format"


########################################################################################
########################################################################################

#                         TEST FOR CHECKING THE VALID X VALUES

def test_valid_X_values(qtbot):
    # Set valid X values
    func_entry.setText("sqrt(x)")
    minx_entry.setText("0")
    maxx_entry.setText("10")

    # Click the plot button
    plot_button = window.findChild(QPushButton, "plotButton")
    QTest.mouseClick(plot_button, Qt.LeftButton)

    qtbot.wait(2000)

    # Check that no error message is shown
    msg_boxes = get_message_boxes()
    assert not any("Input Error" in msg.text() for msg in msg_boxes), "Unexpected error message for valid X values"
