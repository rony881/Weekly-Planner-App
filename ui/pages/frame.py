from PyQt6.QtWidgets import (
 QWidget, QLabel, QVBoxLayout,
)

class Page_Header(QWidget):
    def __init__(self,h1:str , h2:str = None):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 4, 0)

        if h1:
            title = QLabel(h1)
            title.setStyleSheet(
                """
                font-size: 22px;
                font-weight: bold;
                """
            )
            layout.addWidget(title)

        if h2:
            subtitle = QLabel("Build Habits, Build Tomorrow")
            subtitle.setStyleSheet("color: gray;")
            layout.addWidget(subtitle)


