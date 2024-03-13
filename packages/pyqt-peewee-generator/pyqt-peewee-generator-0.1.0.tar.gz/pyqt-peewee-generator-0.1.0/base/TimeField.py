import datetime

from PyQt5.QtWidgets import QLabel, QTimeEdit, QVBoxLayout, QWidget


class TimeField(QWidget):
    def __init__(self, label: str):
        super().__init__()

        # UI
        label = QLabel(label)
        self.edit = QTimeEdit()

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.edit)

        self.setLayout(layout)

    @property
    def value(self) -> datetime.time:
        return self.edit.time().toPyTime()

    @value.setter
    def value(self, val):
        self.edit.setTime(val)

    @staticmethod
    def check():
        return True
