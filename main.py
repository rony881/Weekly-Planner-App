from ui.widgets.mainwindow import Mainwindow
from PyQt6.QtWidgets import QApplication
import sys


# ==============================================
# Run Application
# ==============================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())