
from PyQt4 import QtGui, QtCore
from gui.edit_bindings_qtdesigner import Ui_MainWindow


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # compile resources file with:
        # pyuic4 -x gui/edit_bindings_qtdesigner.ui -o gui/edit_bindings_qtdesigner.py
        # pyrcc4.exe -py3 -o gui/resources_rc.py gui/resources.qrc

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
