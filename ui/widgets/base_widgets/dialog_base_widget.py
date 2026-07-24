from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QWidget


class DialogBaseWidget(QDialog):
    """Base Widget For Making Dialogs for the Application."""

    def __init__(self, parent: QWidget | None):
        super().__init__(parent)
        """Initialize the Dialog."""
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Dialog)
        self.outer = QVBoxLayout(self)
        self.outer.setContentsMargins(24, 24, 24, 24)
        
    def setDialogTitle(self, title: str):
        """Set Dialog Window Title"""
        self.setWindowTitle(title)

    def setDialogSize(self, width: int= 600, height: int= 300):
        """Set Dialog Window size"""
        self.resize(width, height)
        