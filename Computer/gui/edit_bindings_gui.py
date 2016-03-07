from time import sleep
from PyQt4 import QtGui, QtCore
from gui.edit_bindings_qtdesigner import Ui_MainWindow
from button_bindings import ButtonBindings


class MyWindow(QtGui.QMainWindow):
    def __init__(self, bindings=ButtonBindings('default')):
        super(MyWindow, self).__init__()
        # compile resources file with:
        # pyuic4 -x gui/edit_bindings_qtdesigner.ui -o gui/edit_bindings_qtdesigner.py
        # pyrcc4.exe -py3 -o gui/resources_rc.py gui/resources.qrc

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.input_key.hide()

        self.bindings = bindings
        self.profile = self.bindings.get_current_profile()
        self.ui.input_up.text = 'w'
        #self.ui.input_select.clicked.connect(self.change_binding)
        self.update_profile_list()

        self.ui.action_save_new_profile.clicked.connect(self.store_profile)

        self.ui.action_load_profile.clicked.connect(self.load_profile)

        self.ui.action_delete_profile.clicked.connect(self.delete_profile)

        self.show()

    def change_binding(self):
        button_name = self.sender().objectName().split('_')[1]  # get the name after '_'
        print(button_name)
        key = self.read_key()
        self.bindings.edit_binding(button_name, key)

    def read_key(self):
        self.ui.input_key.show()
        key = 'y'
        sleep(1)
        self.ui.input_key.hide()
        return key

    def store_profile(self):
        profile_name = self.ui.input_new_profile_name.text()
        self.bindings.create_profile(profile_name, self.bindings.get_current_profile())
        self.bindings.store_profiles()
        self.bindings.reload_profiles()
        self.update_profile_list()

    def load_profile(self):
        profile_name = self.ui.input_profile.currentText()
        self.bindings.choose_profile(profile_name)

    def delete_profile(self):
        profile_name = self.ui.input_profile.currentText()
        self.bindings.remove_profile(profile_name)
        self.update_profile_list()

    def update_profile_list(self):
        self.ui.input_profile.clear()
        self.ui.input_profile.addItems(self.bindings.get_profile_names())


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
