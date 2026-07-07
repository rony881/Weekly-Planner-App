from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget,QHBoxLayout,QFrame
from qfluentwidgets import FluentIcon, IconWidget
from qfluentwidgets.components import CardWidget
from config import UI_CONFIG
from core.utils.logger import logger

HEIGHT = UI_CONFIG["card_height"]
SLEEP_LOG = {
    "date" : "Mon, Jul 6",
    "time" : "12:32 pm - 8:45 am"
}

class SleepJournal(QWidget):
    """Slepp Journal Page"""
    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Sleep Journal Page Initialized Successfully")
        self.main_layout = QVBoxLayout(self)

        self._build_ui()

    def _build_ui(self):
        self.main_layout.addWidget(SleepCard(self,SLEEP_LOG))

class SleepCard(CardWidget):
    """Card Widget Displaying Sleep Logs"""

    def __init__(self, parent, logs: dict):
        super().__init__(parent)

        self.logs = logs
        self.setFixedHeight(HEIGHT)

        self.setStyleSheet("""
            CardWidget{
                border: 1px solid #999999;
                border-radius: 8px;
            }

            QLabel{
                color: #333333;
            }
        """)

        # Main Layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(15)

        # Icon
        self.icon = IconWidget(FluentIcon.CALENDAR)
        self.icon.setFixedSize(24, 24)
        layout.addWidget(self.icon, alignment=Qt.AlignmentFlag.AlignTop)

        # Text Layout
        textLayout = QVBoxLayout()
        textLayout.setSpacing(4)

        self.date = QLabel(self.logs["date"])
        self.date.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
        """)

        self.sleep_time = QLabel(self.logs["time"])
        self.sleep_time.setStyleSheet("""
            font-size:13px;
            color:#666666;
        """)

        textLayout.addWidget(self.date)
        textLayout.addWidget(self.sleep_time)

        layout.addLayout(textLayout)
        layout.addStretch()