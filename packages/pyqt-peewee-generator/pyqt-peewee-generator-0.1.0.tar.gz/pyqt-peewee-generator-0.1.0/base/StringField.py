from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QStyle


class StringField(QWidget):
    def __init__(self, label: str, not_null: bool = False):
        super().__init__()
        self.not_null = not_null

        # UI
        h_layout = QHBoxLayout()
        h_layout.setAlignment(Qt.AlignLeft)
        label = QLabel(label + " *" if not_null else "")
        self.error = QLabel()
        self.error.setStyleSheet("color: red")

        h_layout.addWidget(label)
        h_layout.addWidget(self.error)

        self.edit = QLineEdit()
        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(self.edit)

        self.setLayout(layout)

    @property
    def value(self) -> str:
        return self.edit.text()

    @value.setter
    def value(self, val):
        self.edit.setText(val)

    def check(self) -> bool:
        is_valid = not self.not_null or self.value != ""
        if not is_valid:
            self.error.setText("Это поле не может быть пустым")
        else:
            self.error.setText("")
        return is_valid
