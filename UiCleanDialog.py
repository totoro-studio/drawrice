__author__ = 'Tony'

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CleanDialog(object):
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
        self.pushButton_clean.clicked.connect(Dialog.beginclean)
        self.checkBox_cleanall.clicked.connect(Dialog.setbutton)
        self.checkBox_cleancheckin.clicked.connect(Dialog.setbutton)
        self.checkBox_cleanwin.clicked.connect(Dialog.setbutton)
        self.checkBox_directory.clicked.connect(Dialog.setbutton)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "抽米 V1.0 -内测版"))
        self.pushButton_clean.setText(_translate("Dialog", "退出"))
        self.checkBox_cleanall.setText(_translate("Dialog", "清除所有数据库记录"))
        self.checkBox_cleancheckin.setText(_translate("Dialog", "清除签到记录"))
        self.checkBox_cleanwin.setText(_translate("Dialog", "清除获奖记录"))
        self.checkBox_directory.setText(_translate("Dialog", "清空导出及日志文件夹"))

