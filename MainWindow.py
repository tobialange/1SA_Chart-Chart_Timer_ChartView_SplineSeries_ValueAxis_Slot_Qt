from PySide6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Temperatursimulation")

        self.setCentralWidget(CentralWidget(self))
