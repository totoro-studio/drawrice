__author__ = 'Tony'

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created: Sun Aug 17 13:32:16 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 387)
        self.pushButton_Search = QtWidgets.QPushButton(Form)
        self.pushButton_Search.setGeometry(QtCore.QRect(410, 332, 75, 41))
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.pushButton_DrawLottery = QtWidgets.QPushButton(Form)
        self.pushButton_DrawLottery.setGeometry(QtCore.QRect(320, 332, 75, 41))
        self.pushButton_DrawLottery.setObjectName("pushButton_DrawLottery")
        self.comboBox_WinType = QtWidgets.QComboBox(Form)
        self.comboBox_WinType.setGeometry(QtCore.QRect(320, 275, 91, 31))
        self.comboBox_WinType.setObjectName("comboBox_WinType")
        self.pushButton_AddQueue = QtWidgets.QPushButton(Form)
        self.pushButton_AddQueue.setGeometry(QtCore.QRect(230, 250, 75, 23))
        self.pushButton_AddQueue.setObjectName("pushButton_AddQueue")
        self.pushButton_ImportAll = QtWidgets.QPushButton(Form)
        self.pushButton_ImportAll.setGeometry(QtCore.QRect(70, 310, 91, 23))
        self.pushButton_ImportAll.setObjectName("push_Button_ImportAll")
        self.pushButton_Checkin = QtWidgets.QPushButton(Form)
        self.pushButton_Checkin.setGeometry(QtCore.QRect(70, 350, 91, 23))
        self.pushButton_Checkin.setObjectName("pushButton_Checkin")
        self.pushButton_DelQueue = QtWidgets.QPushButton(Form)
        self.pushButton_DelQueue.setGeometry(QtCore.QRect(230, 280, 75, 23))
        self.pushButton_DelQueue.setObjectName("pushButton_DelQueue")
        self.pushButton_DelAllQueue = QtWidgets.QPushButton(Form)
        self.pushButton_DelAllQueue.setGeometry(QtCore.QRect(230, 310, 75, 23))
        self.pushButton_DelAllQueue.setObjectName("pushButton_DelAllQueue")
        self.pushButton_Reset = QtWidgets.QPushButton(Form)
        self.pushButton_Reset.setGeometry(QtCore.QRect(230, 350, 75, 23))
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(230, 10, 261, 221))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 221, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_statistic1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_statistic1.setObjectName("label_statistic1")
        self.verticalLayout.addWidget(self.label_statistic1)
        self.label_statistic2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_statistic2.setObjectName("label_statistic2")
        self.verticalLayout.addWidget(self.label_statistic2)
        self.label_statistic3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_statistic3.setObjectName("label_statistic3")
        self.verticalLayout.addWidget(self.label_statistic3)
        self.label_statistic4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_statistic4.setObjectName("label_statistic4")
        self.verticalLayout.addWidget(self.label_statistic4)
        self.label_statistic5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_statistic5.setObjectName("label_statistic5")
        self.verticalLayout.addWidget(self.label_statistic5)
        self.label_statistic6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_statistic6.setObjectName("label_statistic6")
        self.verticalLayout.addWidget(self.label_statistic6)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 10, 211, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 191, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 250, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(440, 250, 31, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_number = QtWidgets.QComboBox(Form)
        self.comboBox_number.setGeometry(QtCore.QRect(430, 275, 51, 31))
        self.comboBox_number.setObjectName("comboBox_number")

        self.retranslateUi(Form)
        self.comboBox_WinType.currentIndexChanged.connect(Form.refreshwinnumber)
        self.pushButton_AddQueue.clicked.connect(Form.addqueue)
        self.pushButton_DelQueue.clicked.connect(Form.delqueue)
        self.pushButton_DelAllQueue.clicked.connect(Form.clearqueue)
        self.pushButton_ImportAll.clicked.connect(Form.importall)
        self.pushButton_Checkin.clicked.connect(Form.importcheckin)
        self.pushButton_Reset.clicked.connect(Form.clean)
        self.pushButton_DrawLottery.clicked.connect(Form.drawlottery)
        self.pushButton_Search.clicked.connect(Form.search)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "抽米 v1.0 -内测版"))
        self.pushButton_Search.setText(_translate("Form", "查询"))
        self.pushButton_DrawLottery.setText(_translate("Form", "抽奖"))
        self.pushButton_AddQueue.setText(_translate("Form", "<-"))
        self.pushButton_ImportAll.setText(_translate("Form", "导入All"))
        self.pushButton_Checkin.setText(_translate("Form", "导入Checkin"))
        self.pushButton_DelQueue.setText(_translate("Form", "->"))
        self.pushButton_DelAllQueue.setText(_translate("Form", "->>"))
        self.pushButton_Reset.setText(_translate("Form", "清理数据"))
        self.groupBox.setTitle(_translate("Form", "统计信息"))
        self.label_statistic1.setText(_translate("Form", ""))
        self.label_statistic2.setText(_translate("Form", ""))
        self.label_statistic3.setText(_translate("Form", ""))
        self.label_statistic4.setText(_translate("Form", ""))
        self.label_statistic5.setText(_translate("Form", ""))
        self.label_statistic6.setText(_translate("Form", ""))
        self.groupBox_2.setTitle(_translate("Form", "抽奖序列"))
        self.label.setText(_translate("Form", "奖 项"))
        self.label_2.setText(_translate("Form", "人 数"))

