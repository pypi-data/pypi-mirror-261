from PyQt5.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget
from typing import Callable


class Select(QWidget):
    def __init__(self, label: str, get_variants: Callable):
        super().__init__()

        # UI
        label = QLabel(label)
        self.select = QComboBox()
        self.select.addItems(get_variants())

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.select)

        self.setLayout(layout)

    @property
    def value(self) -> str:
        return self.select.currentText()

    @value.setter
    def value(self, val):
        self.select.setCurrentIndex(val)

    @property
    def index(self) -> int:
        return self.select.currentIndex()

    @staticmethod
    def check():
        return True
