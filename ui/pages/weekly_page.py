from sched import scheduler

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout,QTabWidget
)
from PyQt6.QtCore import Qt
from ui.widgets.card import TaskCard
from qfluentwidgets import TitleLabel,SmoothScrollArea


WEEKLY_SCHEDULE = {
    "Sat" : {
        "Morning" : ["Reading", "Drawing", "Meditation"],
        "AfterNoon" : ["Exercise", "Drawing", "Meditation"],
        "Night" : ["Reading", "Leg Day", "Meditation"]
    },
    "Sun" : {
        "Morning" : ["Reading", "Drawing", "Meditation"],
        "AfterNoon" : ["Exercise", "Drawing", "Meditation"],
        "Night" : ["Reading", "Leg Day", "Meditation"]
    },
    "Mon" : {
        "Morning" : ["Reading", "Drawing", "Meditation"],
        "AfterNoon" : ["Exercise", "Drawing", "Meditation"],
        "Night" : ["Reading", "Leg Day", "Meditation"]
    },
    "Tue" : {
        "Morning" : ["Reading", "Drawing", "Meditation"],
        "AfterNoon" : ["Exercise", "Drawing", "Meditation"],
        "Night" : ["Reading", "Leg Day", "Meditation"]
    },
    "Wed" : {
        "Morning" : ["Reading", "Drawing", "Meditation"],
        "AfterNoon" : ["Exercise", "Drawing", "Meditation"],
        "Night" : ["Reading", "Leg Day", "Meditation"]
    },
    "Thu" : {
        "Morning" : ["Reading", "Drawing", "Meditation"],
        "AfterNoon" : ["Exercise", "Drawing", "Meditation"],
        "Night" : ["Reading", "Leg Day", "Meditation"]
    },
    "Fri" : {
        "Morning" : ["Reading", "Drawing", "Meditation"],
        "AfterNoon" : ["Exercise", "Drawing", "Meditation"],
        "Night" : ["Reading", "Leg Day", "Meditation"]
    }
} 

class WeeklyTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # ================
        # Header / Title
        # ================
        title = TitleLabel("Weekly Schedule")
        layout.addWidget(title)

        # ================
        # Tabbar
        #================
        tabs = QTabWidget()
        for day,schedule in WEEKLY_SCHEDULE.items():
            tabs.addTab(DayWidget(schedule),day)

        layout.addWidget(tabs)

class DayWidget(SmoothScrollArea):
    def __init__(self, routine):
        super().__init__()

        self.setWidgetResizable(True)

        mainLayout = QVBoxLayout(self)

        # Content widget 
        content = QWidget()
        contentLayout = QVBoxLayout(content)
        self.setWidget(content)

        for time, tasks in routine.items():
            for task in tasks:
                card = TaskCard(task, time)
                contentLayout.addWidget(card)

        contentLayout.addStretch()
