__author__ = 'Tony'

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchFrame.ui'
#
# Created: Sun Aug 17 14:45:56 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 336)
        self.pushButton_exportlist = QtWidgets.QPushButton(Form)
        self.pushButton_exportlist.setGeometry(QtCore.QRect(470, 250, 75, 23))
        self.pushButton_exportlist.setObjectName("pushButton_exportlist")
        self.pushButton_close = QtWidgets.QPushButton(Form)
        self.pushButton_close.setGeometry(QtCore.QRect(470, 290, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 441, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_sum = QtWidgets.QLabel(Form)
        self.label_sum.setGeometry(QtCore.QRect(470, 174, 71, 20))
        self.label_sum.setObjectName("label_sum")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(478, 30, 61, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_ischeckin = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_ischeckin.setObjectName("checkBox_ischeckin")
        self.verticalLayout.addWidget(self.checkBox_ischeckin)
        self.checkBox_isnotcheckin = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_isnotcheckin.setObjectName("checkBox_isnotcheckin")
        self.verticalLayout.addWidget(self.checkBox_isnotcheckin)
        self.checkBox_iswin = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_iswin.setObjectName("checkBox_iswin")
        self.verticalLayout.addWidget(self.checkBox_iswin)

        self.retranslateUi(Form)
        self.checkBox_ischeckin.clicked.connect(Form.checkclick)
        self.checkBox_isnotcheckin.clicked.connect(Form.checkclick)
        self.checkBox_iswin.clicked.connect(Form.iswinclick)
        self.pushButton_exportlist.clicked.connect(Form.exportlist)
        self.pushButton_close.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "抽米 v1.0 查询 -内测版"))
        self.pushButton_exportlist.setText(_translate("Form", "导出"))
        self.pushButton_close.setText(_translate("Form", "关闭"))
        self.label_sum.setText(_translate("Form", ""))
        self.checkBox_ischeckin.setText(_translate("Form", "已签到"))
        self.checkBox_isnotcheckin.setText(_translate("Form", "未签到"))
        self.checkBox_iswin.setText(_translate("Form", "已中奖"))

