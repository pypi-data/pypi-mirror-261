from PyQt5.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    def __init__(self, label: str):
        super().__init__(label)

    @property
    def value(self) -> int:
        return self.isChecked()

    @value.setter
    def value(self, val):
        self.setChecked(val)

    @staticmethod
    def check():
        return True
