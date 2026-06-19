from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget,
)
from PyQt6.QtCore import Qt
from .frame import Page_Header

days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]


class TaskColumn(QFrame):
    def __init__(self, title, tasks):
        super().__init__()

        self.setFrameShape(QFrame.Shape.Box)

        layout = QVBoxLayout(self)

        # Column Header
        header = QLabel(title)
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet(
            """
            font-size: 14px;
            font-weight: bold;
            padding: 6px;
            border-bottom: 1px solid gray;
            """
        )

        layout.addWidget(header)

        # Tasks
        for task in tasks:
            task_label = QLabel(task)
            task_label.setStyleSheet("padding: 4px;")
            layout.addWidget(task_label)

        # Push button to bottom
        layout.addStretch()

        add_btn = QPushButton("+ New")
        layout.addWidget(add_btn)


class DayPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        morning_tasks = ["Workout","Reading","Meditate"]

        day_tasks = ["Project Work"]

        night_tasks = ["Art Practice","Study"]

        layout.addWidget(TaskColumn("Morning", morning_tasks),1)
        layout.addWidget(TaskColumn("Day", day_tasks),1)
        layout.addWidget(TaskColumn("Night", night_tasks),1)


class Weekly_Tab(QWidget):
    def __init__(self):
        super().__init__()

        title = Page_Header("Weekly Schedule","Build Habits, Build Tommorow")
        main_layout = QVBoxLayout(self)
                                                                          
        main_layout.addWidget(title)

        tabs = QTabWidget()

        for day in days:
            tabs.addTab(DayPage(), day)

        main_layout.addWidget(tabs)
