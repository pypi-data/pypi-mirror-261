from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox


class NumberField(QWidget):
    def __init__(self, label: str):
        super().__init__()

        # UI
        label = QLabel(label)
        self.edit = QSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.edit)

        self.setLayout(layout)

    @property
    def value(self) -> int:
        return int(self.edit.text())

    @value.setter
    def value(self, val):
        self.edit.setValue(val)

    @staticmethod
    def check():
        return True
