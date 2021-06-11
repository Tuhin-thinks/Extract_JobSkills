from PyQt5 import QtGui, QtWidgets


class DropLabel(QtWidgets.QLabel):
    def __init__(self, parent_widget, parent_obj):
        QtWidgets.QLabel.__init__(self, parent_widget)
        self.setAcceptDrops(True)
        self.original_stylesheet = """QLabel{\
                        border: 2px dashed grey;\
                        border-radius: 5px;\
                        font-weight: bold;
        }"""
        self.setStyleSheet(self.original_stylesheet)
        self.drop_style = """QLabel{
            border: 2px dashed black;\
            border-radius: 5px;\
            color:  rgb(85, 87, 83);\
            font: 75 25pt "Yrsa";\
            font-weight: bold;\
            background-color: rgb(186, 189, 182);\
            padding: 0px;}"""
        self.parent_ = parent_obj

    def paste_event(self):
        data = QtWidgets.QApplication.clipboard().text()

    def dragEnterEvent(self, event: QtGui.QDropEvent):
        if event.mimeData().hasText():
            self.setStyleSheet(self.drop_style)
            event.acceptProposedAction()

    def dropEvent(self, event: QtGui.QDropEvent):
        print("Am here")
        if event.mimeData().hasText():  # it'll be valid for only text drag and drop
            dropped_text: str = event.mimeData().text()
            print(dropped_text)
        self.setStyleSheet(self.original_stylesheet)
        event.acceptProposedAction()
        self.update()
