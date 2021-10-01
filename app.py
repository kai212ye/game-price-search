from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, consts

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
        self.label.adjustSize()
        self.label.move(consts.TITLE_X, consts.TITLE_Y)
        
        # Adds a search button
        self.search = QtWidgets.QPushButton(self)
        self.search.setText(consts.SEARCH_BTN)
        self.search.move(consts.SEARCH_X, consts.SEARCH_Y)
        self.search.clicked.connect(self.click_search)
        
    # Defines search button behaviour
    def click_search(self):
        self.label.setText("YOU'VE PRESSED THE BUTTON")
        self.update()
        print("YEAH PRESS ME DADDY")
        
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