from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout


class ListWidget:
    def __init__(self, parent, item_widget, spacing=False):
        self.scroll = QScrollArea()
        self.parent = parent
        self.item_widget = item_widget
        self.spacing = spacing

    def show_list(self, items):
        scroll = QScrollArea()
        list_widget = QWidget()
        list_layout = QVBoxLayout()
        if not self.spacing:
            list_layout.setSpacing(0)
        for item in items:
            list_layout.addWidget(self.item_widget(item))
        list_widget.setLayout(list_layout)
        self.scroll.setParent(None)
        self.scroll = scroll
        self.scroll.setWidget(list_widget)
        list_widget.setObjectName("listWidget")
        list_widget.setStyleSheet("QWidget#listWidget {background-color: transparent} QPushButton {max-width: 100px}")
        self.scroll.setStyleSheet("QScrollArea {border: 0; background-color: transparent;}")
        self.parent.addWidget(self.scroll)