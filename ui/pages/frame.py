from PyQt6.QtWidgets import (
 QWidget, QLabel, QVBoxLayout,
)

class Page_Header(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 4, 0)

    def set_title(self,h1:str= None, h2:str = None,h3:str = None):

        if h1:
            a1 = QLabel(h1)
            a1.setStyleSheet("font-weight: bold; font-size: 25px")
            self.layout.addWidget(a1)

        if h2:
            a2 = QLabel(h2)
            a2.setStyleSheet("font-size: 18px")
            self.layout.addWidget(a2)

        if h3:
            a3 = QLabel(h3)
            a3.setStyleSheet("font-size: 12px")
            self.layout.addWidget(a3)

