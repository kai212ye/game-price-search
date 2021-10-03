from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QShortcut,
    QWidget,
    QLabel,
)
import sys, consts, search_functions

# Configures a class for the app that inherits from QMainWindow
class AppWindow(QMainWindow):

    # Constructor
    def __init__(self):
        super(AppWindow, self).__init__()
        self.setGeometry(consts.XPOS, consts.YPOS, consts.WIDTH, consts.HEIGHT)
        self.setWindowTitle(consts.WINDOW_TITLE)
        self.initUI()

    # Initialises the UI
    def initUI(self):
        # Labels the window
        self.label = QtWidgets.QLabel(self)
        self.label.setText(consts.WINDOW_TITLE)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.adjustSize()
        self.label.move(consts.TITLE_X, consts.TITLE_Y)

        # Adds a search button and the Enter key as its shortcut
        self.search = QtWidgets.QPushButton(self)
        self.search.setText(consts.SEARCH_BTN)
        self.search.move(consts.SEARCH_X, consts.SEARCH_Y)
        self.search.clicked.connect(self.click_search)
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(self.click_search)

        # Create a search bar
        self.search_bar = QtWidgets.QLineEdit(self)
        self.search_bar.move(consts.BAR_X, consts.BAR_Y)
        self.search_bar.resize(consts.BAR_WIDTH, consts.BAR_HEIGHT)

    # Defines search button behaviour and handles the search function
    def click_search(self):
        input_term = self.search_bar.text()

        # Configure the output based on Steam search results, and handles error when no results are found.
        try:
            name, sale, original_price, price, link = search_functions.steam(input_term)
        except ValueError:
            self.label.setText("No results found.")
            return ()

        if sale:
            search_result = (
                "Game title: "
                + name
                + "\nOn sale!"
                + "\nOriginal Price: "
                + original_price
                + "\nPrice: "
                + price
                + "\nLink: "
                + link
            )
        else:
            search_result = (
                "Game title: " + name + "\nPrice: " + price + "\nLink: " + link
            )

        # Update and display search results
        self.label.setText(search_result)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.update()

    # Updates the window every time changes occur
    def update(self):
        self.label.adjustSize()


# Entry point for the app
def window():

    # Initialises the app
    app = QApplication(sys.argv)
    win = AppWindow()

    # Runs and exits the app
    win.show()
    sys.exit(app.exec_())


# Starts the app
window()
