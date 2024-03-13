import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QDateEdit, QVBoxLayout


class DateRangeField(QWidget):
    def __init__(self, label: str):
        super().__init__()

        # UI
        h_label_layout = QHBoxLayout()
        h_label_layout.setAlignment(Qt.AlignLeft)
        label = QLabel(label)
        self.error = QLabel()
        self.error.setStyleSheet("color: red")

        h_label_layout.addWidget(label)
        h_label_layout.addWidget(self.error)

        h_edit_layout = QHBoxLayout()
        h_edit_layout.setAlignment(Qt.AlignLeft)

        self.from_edit = QDateEdit()
        self.to_edit = QDateEdit()
        h_edit_layout.addWidget(QLabel("C"))
        h_edit_layout.addWidget(self.from_edit)
        h_edit_layout.addWidget(QLabel("До"))
        h_edit_layout.addWidget(self.to_edit)
        layout = QVBoxLayout()
        layout.addLayout(h_label_layout)
        layout.addLayout(h_edit_layout)

        self.setLayout(layout)

    @property
    def from_value(self) -> datetime.date:
        return self.from_edit.date().toPyDate()

    @property
    def to_value(self) -> datetime.date:
        return self.to_edit.date().toPyDate()

    @from_value.setter
    def from_value(self, val):
        self.from_edit.setDate(val)

    @to_value.setter
    def to_value(self, val):
        self.to_edit.setDate(val)

    def check(self) -> bool:
        is_valid = self.from_value < self.to_value
        if not is_valid:
            self.error.setText("Не корректный промежуток")
        else:
            self.error.setText("")
        return is_valid
