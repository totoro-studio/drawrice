__author__ = 'Tony'

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DrawLotteryForm(object):
    def setupUi(self, Form_DrawLottery):
        Form_DrawLottery.setObjectName("Form_DrawLottery")
        Form_DrawLottery.resize(400, 300)

        self.retranslateUi(Form_DrawLottery)

        QtCore.QMetaObject.connectSlotsByName(Form_DrawLottery)

    def retranslateUi(self, Form_DrawLottery):
        _translate = QtCore.QCoreApplication.translate
        Form_DrawLottery.setWindowTitle(_translate("DrawLotteryForm", "抽米 v1.0 抽奖 -内测版"))
