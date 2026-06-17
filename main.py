from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QFrame
)
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200,900)
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(
            """
            background-color: #0a0a0a;
            """
        )
        self.setCentralWidget(self.central_widget)
        self.side_bar = QFrame()
        self.side_bar.setFixedWidth(250)
        self.side_bar.setStyleSheet(
            """
            background-color: #161618;
            border-right: 1px solid #2e2e2e;
            """
        )
        self.central_panel = QFrame()

        self.weekly_calender = QFrame()
        self.weekly_calender.setFixedHeight(100)
        self.weekly_calender.setStyleSheet(
            """
            background-color: #161618;
            border: 1px solid #2e2e2e;
            border-radius: 7px;
            """
        )
        self.task_area = QFrame()
        self.task_area.setStyleSheet(
            """
            background-color: #161618;
            border: 1px solid #2e2e2e;
            border-radius: 7px;
            """
        )
        self.habit_tracker_area = QFrame()
        self.habit_tracker_area.setStyleSheet(
            """
            background-color: #161618;
            border: 1px solid #2e2e2e;
            border-radius: 7px;
            """
        )
        self.progress_area = QFrame()
        self.progress_area.setFixedHeight(100)
        self.progress_area.setStyleSheet(
            """
            background-color: #161618;
            border: 1px solid #2e2e2e;
            border-radius: 7px;
            """
        )

        self._setup_layout()
    def _setup_layout(self):
        
        # Central Layout
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.addWidget(self.side_bar)
        self.central_layout.addWidget(self.central_panel)

        self.side_layout = QVBoxLayout(self.side_bar)

        self.panel_layout = QVBoxLayout(self.central_panel)
        self.panel_layout.addWidget(self.weekly_calender)
        self.panel_layout.addWidget(self.task_area)
        self.panel_layout.addWidget(self.habit_tracker_area)
        self.panel_layout.addWidget(self.progress_area)



# ==============================================
# Run Application
# ==============================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())