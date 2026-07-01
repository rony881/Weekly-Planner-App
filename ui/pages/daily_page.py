from PyQt6.QtWidgets import QHBoxLayout, QScrollArea, QVBoxLayout, QWidget, QFrame
from qfluentwidgets import PrimaryPushButton, TransparentPushButton, FluentIcon as FI

from ui.widgets.title_bar import TitleBar


class DailyPage(QWidget):
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        # main Layout of this page
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0,0,0,0)
        
        self._build_ui()

    def _build_ui(self):
        # ======= Header =========
        # title shown on top of the page
        self.title = TitleBar(self,"My Task")
        self.page_layout.addWidget(self.title)

        # ======= Main Content ======
        # Scroll Area for the Tasks List
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setStyleSheet("QScrollArea{background: transparent; border: none;}")

        # main container for Tasks List
        self.list_container = QWidget(self)
        self.list_container.setStyleSheet("background: transparent;")
        self.list_layout = QVBoxLayout(self.list_container)
        self.list_layout.setContentsMargins(0, 4, 0, 4)
        self.list_layout.setSpacing(8)
        self.list_layout.addStretch(1)

        self.scroll_area.setWidget(self.list_container)
        self.page_layout.addWidget(self.scroll_area, 1)

        # ========== Footer =========
        # clear complete and Add Task Button Area
        footer = QHBoxLayout()
        self.clr_task_btn = TransparentPushButton("Clear Completed")
        footer.addWidget(self.clr_task_btn)
        footer.addStretch(1)
        add_btn = PrimaryPushButton(FI.ADD,"Add Task")
        footer.addWidget(add_btn)
        self.page_layout.addLayout(footer)
        
        
        
        