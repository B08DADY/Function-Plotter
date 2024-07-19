import pytest
from PySide2.QtWidgets import QLineEdit, QPushButton, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Task import app, window

#SteUp The Tests
@pytest.fixture(scope='function')
def qt_app(qtbot):
    """Fixture to launch and close the application"""
    global app  # Ensure we use the global app defined in Task.py
    if QApplication.instance() is None:
        app = QApplication([])

    app_window = window  # Keep a reference to the main window

    # Start the application event loop with QtBot
    qtbot.addWidget(app_window)

    yield app

    # Cleanup after the test
  #  window.close()
    app.quit()

########################################################################################
########################################################################################

# inVALID FUNC FORMAT TEST
@pytest.mark.usefixtures('qt_app')
@pytest.mark.order(1)
def test_invalid_func_format(qtbot, qt_app):
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
    qtbot.wait(10000)

########################################################################################
########################################################################################

# VALID FUNC FORMAT TEST
@pytest.mark.usefixtures('qt_app')
@pytest.mark.order(2)
def test_valid_func_format(qtbot, qt_app):
    # Simulate user input
    func_entry = window.findChild(QLineEdit, "func_entry")
    minx_entry = window.findChild(QLineEdit, "minx_entry")
    maxx_entry = window.findChild(QLineEdit, "maxx_entry")

    assert func_entry is not None, "func_entry is None"
    assert minx_entry is not None, "minx_entry is None"
    assert maxx_entry is not None, "maxx_entry is None"

    func_entry.setText("lg10(x*2)")
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
    qtbot.wait(10000)

########################################################################################
########################################################################################

# Valid X values Test
@pytest.mark.usefixtures('qt_app')
@pytest.mark.order(3)
def test_valid_X_values(qtbot, qt_app):
    # Simulate user input
    func_entry = window.findChild(QLineEdit, "func_entry")
    minx_entry = window.findChild(QLineEdit, "minx_entry")
    maxx_entry = window.findChild(QLineEdit, "maxx_entry")

    assert func_entry is not None, "func_entry is None"
    assert minx_entry is not None, "minx_entry is None"
    assert maxx_entry is not None, "maxx_entry is None"

    func_entry.setText("5*x^3+10")
    minx_entry.setText("1")
    maxx_entry.setText("100")


    # Simulate clicking the plot button
    plot_button = window.findChild(QPushButton, "plotButton")
    plot_button.click()

    # Assert the plot is drawn
    canvas = window.findChild(FigureCanvas)
    assert canvas.figure.axes is not None
    assert len(canvas.figure.axes[0].lines) > 0  # Check if at least one line is drawn

    # Run the QtBot event loop to keep the window open
    qtbot.wait(200)

########################################################################################
########################################################################################


# inVALID X VLAUES TEST
@pytest.mark.usefixtures('qt_app')
@pytest.mark.order(4)
def test_invalid_X_values(qtbot, qt_app):
    # Simulate user input
    func_entry = window.findChild(QLineEdit, "func_entry")
    minx_entry = window.findChild(QLineEdit, "minx_entry")
    maxx_entry = window.findChild(QLineEdit, "maxx_entry")

    assert func_entry is not None, "func_entry is None"
    assert minx_entry is not None, "minx_entry is None"
    assert maxx_entry is not None, "maxx_entry is None"

    func_entry.setText("6+x")
    minx_entry.setText("not x ;)")
    maxx_entry.setText("100")


    # Simulate clicking the plot button
    plot_button = window.findChild(QPushButton, "plotButton")
    plot_button.click()