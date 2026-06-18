from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QSplitter
)
from ui.pages.weekly import Weekly_Page

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200,900)
        self.central_widget = QSplitter()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet(
            """
            background-color: #0a0a0a;
            """
)

        # Side Panel 
        self.side_panel = QWidget()
        self.side_menu = QListWidget()

        # Main Panel
        self.main_panel = QWidget()

        self.central_widget.addWidget(self.side_panel)
        self.central_widget.addWidget(self.main_panel)
        
        self.weekly_page = Weekly_Page(self)

        self._setup_layout()

    def _setup_layout(self):

        # Side Layout
        self.side_layout = QVBoxLayout(self.side_panel)
        self.side_layout.setContentsMargins(5, 5, 0, 5)
        self.side_layout.addWidget(self.side_menu)

        # Main Panel Layout
        self.main_panel_layout = QVBoxLayout(self.main_panel)
        self.main_panel_layout.setContentsMargins(0, 5, 5, 5)
        self.main_panel_layout.addWidget(self.weekly_page)

