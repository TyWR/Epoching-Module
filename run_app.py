import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QIcon
from app.menu import EpochingWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = EpochingWindow(None)
    main.show()
    sys.exit(app.exec_())
