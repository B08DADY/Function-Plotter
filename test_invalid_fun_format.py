import pytest
from PySide2.QtWidgets import QMessageBox, QLineEdit, QPushButton, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Task import app, window

@pytest.fixture
def qt_app(qtbot):
    """Fixture to launch and close the application"""
    app_window = window  # Keep a reference to the main window

    # Start the application event loop with QtBot
    qtbot.addWidget(app_window)

    yield app

    # Cleanup after the test
    app.quit()

# Valid Function Format Test
@pytest.mark.usefixtures('qt_app')
def test_valid_func_format(qtbot, qt_app):
    # Simulate user input
    func_entry = window.findChild(QLineEdit, "func_entry")
    minx_entry = window.findChild(QLineEdit, "minx_entry")
    maxx_entry = window.findChild(QLineEdit, "maxx_entry")

    assert func_entry is not None, "func_entry is None"
    assert minx_entry is not None, "minx_entry is None"
    assert maxx_entry is not None, "maxx_entry is None"

    func_entry.setText("5x")
    minx_entry.setText("1")
    maxx_entry.setText("10")

    # Simulate clicking the plot button
    plot_button = window.findChild(QPushButton, "plotButton")
    plot_button.click()

    # Assert the plot is drawn
    canvas = window.findChild(FigureCanvas)
    assert canvas.figure.axes is not None
    assert len(canvas.figure.axes[0].lines) > 0  # Check if at least one line is drawn

    # Run the QtBot event loop to keep the window open
    qtbot.wait(200000)


