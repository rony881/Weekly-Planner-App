from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QFrame,
    QHBoxLayout,
    QVBoxLayout
)

days = ["SAT","SUN","MON","TUE","WED","THU","FRI"]
dummy_tasks = ["Reading","Study","Maditate","Workout","Art"]

class Weekly_Page(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        board = QHBoxLayout(self)

        for day in days:
            board.addWidget(DayColumn(day,dummy_tasks))


class DayColumn(QFrame):
    def __init__(self, title, tasks):
        super().__init__()
        self.setFrameShape(QFrame.Shape.Box)
        layout = QVBoxLayout(self)
        self.setStyleSheet(
            "background-color : #151419;"
        )

        # Header 
        header = QLabel(title)
        layout.addWidget(header)
        header.setStyleSheet(
            "font-size: 25px; font-weight: bold; background: #1b1b1e;")

        # Task
        for task in tasks:
            task_label = QLabel(task)
            task_label.setStyleSheet("border-radius: 4px;")
            task_label.setFixedHeight(30)
            layout.addWidget(task_label)


        add_btn = QPushButton("+ New")
        layout.addStretch()
        layout.addWidget(add_btn)
