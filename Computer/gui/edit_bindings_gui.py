# External
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets  # https://www.riverbankcomputing.com/software/pyqt/download5

# Internal
from gui.edit_bindings_qtdesigner import Ui_MainWindow
from button_bindings import ButtonBindings


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, bindings=ButtonBindings('default')):
        super(MyWindow, self).__init__()
        # compile resources file with:
        # pyuic5 -x gui/edit_bindings_qtdesigner.ui -o gui/edit_bindings_qtdesigner.py
        # pyrcc5.exe -o gui/resources_rc.py gui/resources.qrc

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bindings = bindings
        self.profile = self.bindings.get_current_profile()
        self.update_profile_list()

        self.ui.input_profile.currentTextChanged.connect(self.load_profile)
        self.ui.action_save_new_profile.clicked.connect(self.store_profile)
        self.ui.action_delete_profile.clicked.connect(self.delete_profile)
        self.ui.action_change_binding.clicked.connect(self.confirm_key_input)
        self.ui.action_cancel_binding.clicked.connect(self.hide_key_input)

        self.ui.input_key_choice.hide()
        self.ui.action_change_binding.hide()
        self.ui.action_cancel_binding.hide()

        for button in self.ui.controller_buttons.buttons():
            button.setText(self.bindings.get_binding(button.objectName()))
            button.clicked.connect(self.start_key_input)

        self.ui.input_key_choice.addItems(self.bindings.get_possible_keys())
        self.active_button = None
        self.show()

    def start_key_input(self):
        self.active_button = self.sender()
        self.show_key_input()

    def show_key_input(self):
        self.ui.input_key_choice.show()
        self.ui.action_change_binding.show()
        self.ui.action_cancel_binding.show()

    def hide_key_input(self):
        self.active_button = None
        self.ui.input_key_choice.hide()
        self.ui.action_change_binding.hide()
        self.ui.action_cancel_binding.hide()

    def confirm_key_input(self):
        key = self.ui.input_key_choice.currentText()
        self.bindings.edit_binding(self.active_button.objectName(), key)
        self.active_button.setText(key)
        self.bindings.store_profiles()
        self.hide_key_input()

    def store_profile(self):
        profile_name = self.ui.input_new_profile_name.text()
        self.ui.input_new_profile_name.clear()
        self.bindings.create_profile(profile_name, self.bindings.get_current_profile())
        self.bindings.store_profiles()
        self.bindings.load_profiles()
        self.update_profile_list()

    def load_profile(self):
        # to avoid a crash when updating the list (since it causes a change on the combobox, triggering this)
        profile_name = self.ui.input_profile.currentText() if self.ui.input_profile.currentText() else 'default'
        self.bindings.choose_profile(profile_name)

        for button in self.ui.controller_buttons.buttons():
            button.setText(self.bindings.get_binding(button.objectName()))

    def delete_profile(self):
        profile_name = self.ui.input_profile.currentText()
        self.bindings.remove_profile(profile_name)
        self.update_profile_list()

    def update_profile_list(self):
        self.ui.input_profile.clear()
        profile_names = sorted(self.bindings.get_profile_names())  # alphabetical order
        self.ui.input_profile.addItems(profile_names)
        current_index = self.ui.input_profile.findText(self.bindings.current_profile)
        self.ui.input_profile.setCurrentIndex(current_index)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
