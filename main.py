from PySide2.QtWidgets import QApplication
from mainwindow import MainWindows
import sys

app = QApplication()
ventana = MainWindows()
ventana.show()

sys.exit(app.exec_())
