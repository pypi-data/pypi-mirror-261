import datetime

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QDateEdit


class DateField(QWidget):
    def __init__(self, label: str):
        super().__init__()

        # UI
        label = QLabel(label)
        self.edit = QDateEdit()

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.edit)

        self.setLayout(layout)

    @property
    def value(self) -> datetime.date:
        return self.edit.date().toPyDate()

    @value.setter
    def value(self, val):
        self.edit.setDate(val)

    @staticmethod
    def check():
        return True
