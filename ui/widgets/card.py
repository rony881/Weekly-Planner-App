from PyQt6.QtWidgets import (
    QVBoxLayout, QWidget, QSizePolicy,QHBoxLayout
)
from qfluentwidgets import CardWidget,SubtitleLabel,PushButton,BodyLabel


class TaskCard(CardWidget):
    def __init__(self, task, time):
        super().__init__()

        self.setFixedHeight(100)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        self.time_label = SubtitleLabel(time)
        self.task_label = BodyLabel(task)
        self.complete_button = PushButton("Complete")

        main_layout.addWidget(self.time_label)
        main_layout.addWidget(self.task_label)

        main_layout.addStretch()

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.complete_button)

        main_layout.addLayout(button_layout)