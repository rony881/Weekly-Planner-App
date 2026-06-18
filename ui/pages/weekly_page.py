from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget
)
from .frame import Page_Header


days = ["SAT","SUN","MON","TUE","WED","THU","FRI"]
dummy_tasks = ["Reading","Study","Maditate","Workout","Art"]


class Weekly_Tab(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

        layout = QVBoxLayout(self)
        tab = QTabWidget(self)
        
        page_header = Page_Header(self)
        page_header.set_title("Weekly Schedule",h3="Build Havits, Build Tomorrow")

        for day in days:
            tab.addTab(Task_Area(dummy_tasks),day)
        
        layout.addWidget(page_header)
        layout.addWidget(tab)

class Task_Area(QWidget):
    def __init__(self, tasks):
        super().__init__()

        layout = QVBoxLayout(self)

        for task in tasks:
            layout.addWidget(QLabel(task))

        layout.addStretch()

        add_btn = QPushButton("+ New")
        layout.addWidget(add_btn)
