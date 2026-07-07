from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget,QHBoxLayout
from qfluentwidgets import FluentIcon, IconWidget, ProgressBar, TransparentToolButton
from qfluentwidgets.components import CardWidget
from config import UI_CONFIG
from core.utils.logger import logger

HEIGHT = 67
SLEEP_LOG = {
    "date" : "Mon, Jul 6",
    "time" : "12:32 pm - 8:45 am",
    "duration" : "7.67 hrs",
    "score" : 86,
    "mood" : "🙂  Good"
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
        layout.setContentsMargins(13, 13, 13, 10)
        layout.setSpacing(15)

        # Icon
        self.icon = IconWidget(FluentIcon.CALENDAR)
        self.icon.setFixedSize(24, 24)
        layout.addWidget(self.icon, alignment=Qt.AlignmentFlag.AlignTop)

        # ============= Time and Date Layout ==============
        t_d_Layout = QVBoxLayout()
        t_d_Layout.setSpacing(4)

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

        t_d_Layout.addWidget(self.date)
        t_d_Layout.addWidget(self.sleep_time)
        # =================================================
        
        # ============== sleep Duration and Progress ======
        due_prog_Layout = QVBoxLayout()
        due_prog_Layout.setSpacing(4)

        self.duration = QLabel(self.logs["duration"])
        self.duration.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
        """)
        due_prog_Layout.addWidget(self.duration)

        self.due_prog = ProgressBar()
        self.due_prog.setValue(80)
        due_prog_Layout.addWidget(self.due_prog)

        self.score = QLabel("Score:"+ str(self.logs["score"]))
        self.score.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
        """)

        self.mood = QLabel(self.logs["mood"])
        self.mood.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
        """)

        edit_btn = TransparentToolButton(FluentIcon.EDIT)
        delete_btn = TransparentToolButton(FluentIcon.DELETE)
        

        layout.addLayout(t_d_Layout)
        layout.addLayout(due_prog_Layout)
        layout.addWidget(self.score)
        layout.addWidget(self.mood)
        layout.addStretch()
        layout.addWidget(edit_btn)
        layout.addWidget(delete_btn)