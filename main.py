import sys
from PySide6 import QtWidgets
from MainWindow import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    dialog = MainWindow()
    dialog.show()

    sys.exit(app.exec())
