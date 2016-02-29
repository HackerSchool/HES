# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_bindings_qtdesigner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(732, 348)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(732, 348))
        MainWindow.setMaximumSize(QtCore.QSize(732, 348))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("image: url(:/background/HES_front.png);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_left = QtGui.QPushButton(self.centralwidget)
        self.button_left.setGeometry(QtCore.QRect(70, 160, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_left.sizePolicy().hasHeightForWidth())
        self.button_left.setSizePolicy(sizePolicy)
        self.button_left.setObjectName(_fromUtf8("button_left"))
        self.button_right = QtGui.QPushButton(self.centralwidget)
        self.button_right.setGeometry(QtCore.QRect(170, 160, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_right.sizePolicy().hasHeightForWidth())
        self.button_right.setSizePolicy(sizePolicy)
        self.button_right.setObjectName(_fromUtf8("button_right"))
        self.button_up = QtGui.QPushButton(self.centralwidget)
        self.button_up.setGeometry(QtCore.QRect(120, 110, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_up.sizePolicy().hasHeightForWidth())
        self.button_up.setSizePolicy(sizePolicy)
        self.button_up.setObjectName(_fromUtf8("button_up"))
        self.button_down = QtGui.QPushButton(self.centralwidget)
        self.button_down.setGeometry(QtCore.QRect(120, 200, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_down.sizePolicy().hasHeightForWidth())
        self.button_down.setSizePolicy(sizePolicy)
        self.button_down.setObjectName(_fromUtf8("button_down"))
        self.button_select = QtGui.QPushButton(self.centralwidget)
        self.button_select.setGeometry(QtCore.QRect(280, 220, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_select.sizePolicy().hasHeightForWidth())
        self.button_select.setSizePolicy(sizePolicy)
        self.button_select.setObjectName(_fromUtf8("button_select"))
        self.button_start = QtGui.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(390, 220, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy)
        self.button_start.setObjectName(_fromUtf8("button_start"))
        self.button_b = QtGui.QPushButton(self.centralwidget)
        self.button_b.setGeometry(QtCore.QRect(520, 200, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_b.sizePolicy().hasHeightForWidth())
        self.button_b.setSizePolicy(sizePolicy)
        self.button_b.setObjectName(_fromUtf8("button_b"))
        self.button_a = QtGui.QPushButton(self.centralwidget)
        self.button_a.setGeometry(QtCore.QRect(610, 200, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_a.sizePolicy().hasHeightForWidth())
        self.button_a.setSizePolicy(sizePolicy)
        self.button_a.setObjectName(_fromUtf8("button_a"))
        self.input_profile = QtGui.QComboBox(self.centralwidget)
        self.input_profile.setGeometry(QtCore.QRect(40, 20, 161, 21))
        self.input_profile.setObjectName(_fromUtf8("input_profile"))
        self.action_load_profile = QtGui.QPushButton(self.centralwidget)
        self.action_load_profile.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.action_load_profile.setObjectName(_fromUtf8("action_load_profile"))
        self.action_save_new_profile = QtGui.QPushButton(self.centralwidget)
        self.action_save_new_profile.setGeometry(QtCore.QRect(630, 20, 75, 23))
        self.action_save_new_profile.setObjectName(_fromUtf8("action_save_new_profile"))
        self.action_delete_profile = QtGui.QPushButton(self.centralwidget)
        self.action_delete_profile.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.action_delete_profile.setObjectName(_fromUtf8("action_delete_profile"))
        self.input_key = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_key.setGeometry(QtCore.QRect(350, 100, 41, 31))
        self.input_key.setObjectName(_fromUtf8("input_key"))
        self.input_new_profile_name = QtGui.QLineEdit(self.centralwidget)
        self.input_new_profile_name.setGeometry(QtCore.QRect(470, 20, 151, 20))
        self.input_new_profile_name.setObjectName(_fromUtf8("input_new_profile_name"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.button_left.setText(_translate("MainWindow", "Left", None))
        self.button_right.setText(_translate("MainWindow", "Right", None))
        self.button_up.setText(_translate("MainWindow", "Up", None))
        self.button_down.setText(_translate("MainWindow", "Down", None))
        self.button_select.setText(_translate("MainWindow", "Select", None))
        self.button_start.setText(_translate("MainWindow", "Start", None))
        self.button_b.setText(_translate("MainWindow", "B", None))
        self.button_a.setText(_translate("MainWindow", "A", None))
        self.action_load_profile.setText(_translate("MainWindow", "Load", None))
        self.action_save_new_profile.setText(_translate("MainWindow", "Save new", None))
        self.action_delete_profile.setText(_translate("MainWindow", "Delete", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

