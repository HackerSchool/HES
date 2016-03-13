# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/edit_bindings_qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 348)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(732, 348))
        MainWindow.setMaximumSize(QtCore.QSize(732, 348))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("image: url(:/background/HES_front.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_profile = QtWidgets.QComboBox(self.centralwidget)
        self.input_profile.setGeometry(QtCore.QRect(40, 20, 161, 21))
        self.input_profile.setObjectName("input_profile")
        self.action_load_profile = QtWidgets.QPushButton(self.centralwidget)
        self.action_load_profile.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.action_load_profile.setObjectName("action_load_profile")
        self.action_save_new_profile = QtWidgets.QPushButton(self.centralwidget)
        self.action_save_new_profile.setGeometry(QtCore.QRect(630, 20, 75, 23))
        self.action_save_new_profile.setObjectName("action_save_new_profile")
        self.action_delete_profile = QtWidgets.QPushButton(self.centralwidget)
        self.action_delete_profile.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.action_delete_profile.setObjectName("action_delete_profile")
        self.input_new_profile_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_new_profile_name.setGeometry(QtCore.QRect(470, 20, 151, 20))
        self.input_new_profile_name.setObjectName("input_new_profile_name")
        self.input_up = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_up.setGeometry(QtCore.QRect(120, 110, 41, 41))
        self.input_up.setObjectName("input_up")
        self.input_left = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_left.setGeometry(QtCore.QRect(70, 160, 41, 41))
        self.input_left.setObjectName("input_left")
        self.input_right = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_right.setGeometry(QtCore.QRect(170, 160, 41, 41))
        self.input_right.setObjectName("input_right")
        self.input_down = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_down.setGeometry(QtCore.QRect(120, 200, 41, 41))
        self.input_down.setObjectName("input_down")
        self.input_b = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_b.setGeometry(QtCore.QRect(520, 200, 41, 41))
        self.input_b.setObjectName("input_b")
        self.input_a = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_a.setGeometry(QtCore.QRect(610, 200, 41, 41))
        self.input_a.setObjectName("input_a")
        self.input_select = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_select.setGeometry(QtCore.QRect(290, 220, 51, 21))
        self.input_select.setObjectName("input_select")
        self.input_start = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_start.setGeometry(QtCore.QRect(390, 220, 51, 21))
        self.input_start.setObjectName("input_start")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.action_load_profile.setText(_translate("MainWindow", "Load"))
        self.action_save_new_profile.setText(_translate("MainWindow", "Save new"))
        self.action_delete_profile.setText(_translate("MainWindow", "Delete"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

