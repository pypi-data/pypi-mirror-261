from typing import Union

from PyQt5.QtWidgets import QVBoxLayout, QWidget

from base import *


class BaseForm:
    order: list[str]
    fields: dict[str, Union[
        CheckBox,
        DateField,
        DateRangeField,
        DateTimeField,
        DateTimeRangeField,
        NumberField,
        Select,
        StringField,
        TextField,
        TimeRangeField
    ]]

    def __init__(self):
        layout = QVBoxLayout()
        for name in self.order:
            layout.addWidget(self.fields[name])
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.widget = main_widget

    def check(self):
        is_valid = True
        for field in self.fields.values():
            is_valid = is_valid and field.check()
        return is_valid

