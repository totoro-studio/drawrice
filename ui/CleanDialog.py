# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CleanDialog.ui'
#
# Created: Tue Aug 19 13:19:16 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(205, 179)
        self.pushButton_clean = QtWidgets.QPushButton(Dialog)
        self.pushButton_clean.setGeometry(QtCore.QRect(70, 140, 75, 23))
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 10, 145, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_cleanall = QtWidgets.QCheckBox(self.widget)
        self.checkBox_cleanall.setObjectName("checkBox_cleanall")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox_cleanall)
        self.verticalLayout.addWidget(self.checkBox_cleanall)
        self.checkBox_cleancheckin = QtWidgets.QCheckBox(self.widget)
        self.checkBox_cleancheckin.setObjectName("checkBox_cleancheckin")
        self.buttonGroup.addButton(self.checkBox_cleancheckin)
        self.verticalLayout.addWidget(self.checkBox_cleancheckin)
        self.checkBox_cleanwin = QtWidgets.QCheckBox(self.widget)
        self.checkBox_cleanwin.setObjectName("checkBox_cleanwin")
        self.buttonGroup.addButton(self.checkBox_cleanwin)
        self.verticalLayout.addWidget(self.checkBox_cleanwin)
        self.checkBox_directory = QtWidgets.QCheckBox(self.widget)
        self.checkBox_directory.setObjectName("checkBox_directory")
        self.verticalLayout.addWidget(self.checkBox_directory)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_clean.setText(_translate("Dialog", "开始清理"))
        self.checkBox_cleanall.setText(_translate("Dialog", "清除所有记录"))
        self.checkBox_cleancheckin.setText(_translate("Dialog", "清除签到记录"))
        self.checkBox_cleanwin.setText(_translate("Dialog", "清除获奖记录"))
        self.checkBox_directory.setText(_translate("Dialog", "清空导出及日志文件夹"))

