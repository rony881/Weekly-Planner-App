from PyQt6.QtWidgets import QFrame,QHBoxLayout,QPushButton
from qfluentwidgets import TitleLabel

from ui.theme import ADD_BTN_STYLE

class TitleBar(QFrame):
    def __init__(self,parent, h1: str):
        super().__init__(parent)
        layout = QHBoxLayout(self)

        title = TitleLabel(h1)
        layout.addWidget(title)
        layout.addStretch()

        add_btn = QPushButton("+ Add Task")
        add_btn.setStyleSheet(ADD_BTN_STYLE)
        layout.addWidget(add_btn)