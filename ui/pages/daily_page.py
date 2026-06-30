from PyQt6.QtWidgets import QWidget

class DailyPage(QWidget):
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._build_ui()

    def _build_ui(self):
        ...