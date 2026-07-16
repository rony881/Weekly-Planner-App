from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton

from qfluentwidgets import FluentIcon as FI, PrimaryPushButton, TitleLabel
from ui.theme import ADD_BTN_STYLE, TITLE_STYLE

class TitleBar(QFrame):
    """Title bar widget with optional add task button."""
    
    def __init__(self, parent, h1: str, btn: str | None = None):
        """Initialize title bar with title and optional button."""
        super().__init__(parent)
        self.parent = parent
        layout = QHBoxLayout(self)

        title = TitleLabel(h1)
        title.setStyleSheet(TITLE_STYLE)
        layout.addWidget(title)
        layout.addStretch(1)

        if btn:
            self.add_btn = PrimaryPushButton(FI.ADD,"    " + btn)
            self.add_btn.setStyleSheet(ADD_BTN_STYLE)
            self.add_btn.clicked.connect(self.parent.show_input_dialog)
            layout.addWidget(self.add_btn)
