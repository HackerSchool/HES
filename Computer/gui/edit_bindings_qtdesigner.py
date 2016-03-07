# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/edit_bindings_qtdesigner.ui'
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
        self.input_new_profile_name = QtGui.QLineEdit(self.centralwidget)
        self.input_new_profile_name.setGeometry(QtCore.QRect(470, 20, 151, 20))
        self.input_new_profile_name.setObjectName(_fromUtf8("input_new_profile_name"))
        self.input_up = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_up.setGeometry(QtCore.QRect(120, 110, 41, 41))
        self.input_up.setObjectName(_fromUtf8("input_up"))
        self.input_left = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_left.setGeometry(QtCore.QRect(70, 160, 41, 41))
        self.input_left.setObjectName(_fromUtf8("input_left"))
        self.input_right = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_right.setGeometry(QtCore.QRect(170, 160, 41, 41))
        self.input_right.setObjectName(_fromUtf8("input_right"))
        self.input_down = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_down.setGeometry(QtCore.QRect(120, 200, 41, 41))
        self.input_down.setObjectName(_fromUtf8("input_down"))
        self.input_b = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_b.setGeometry(QtCore.QRect(520, 200, 41, 41))
        self.input_b.setObjectName(_fromUtf8("input_b"))
        self.input_a = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_a.setGeometry(QtCore.QRect(610, 200, 41, 41))
        self.input_a.setObjectName(_fromUtf8("input_a"))
        self.input_select = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_select.setGeometry(QtCore.QRect(290, 220, 51, 21))
        self.input_select.setObjectName(_fromUtf8("input_select"))
        self.input_start = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_start.setGeometry(QtCore.QRect(390, 220, 51, 21))
        self.input_start.setObjectName(_fromUtf8("input_start"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
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

