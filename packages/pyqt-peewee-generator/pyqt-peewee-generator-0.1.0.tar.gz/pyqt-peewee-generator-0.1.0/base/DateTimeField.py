import datetime

from PyQt5.QtWidgets import QWidget, QLabel, QDateTimeEdit, QVBoxLayout


class DateTimeField(QWidget):
    def __init__(self, label: str):
        super().__init__()

        # UI
        label = QLabel(label)
        self.edit = QDateTimeEdit()

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.edit)

        self.setLayout(layout)

    @property
    def value(self) -> datetime.datetime:
        return self.edit.dateTime().toPyDateTime()

    @value.setter
    def value(self, val):
        self.edit.setDateTime(val)

    @staticmethod
    def check():
        return True
