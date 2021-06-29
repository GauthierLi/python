# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rad_ditector(object):
    def setupUi(self, rad_ditector):
        rad_ditector.setObjectName("rad_ditector")
        rad_ditector.resize(391, 234)
        self.label = QtWidgets.QLabel(rad_ditector)
        self.label.setGeometry(QtCore.QRect(50, 30, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(rad_ditector)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 91, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(rad_ditector)
        self.pushButton.setGeometry(QtCore.QRect(150, 170, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(rad_ditector)
        self.checkBox.setGeometry(QtCore.QRect(50, 130, 221, 21))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(rad_ditector)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(rad_ditector)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 80, 181, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(rad_ditector)
        QtCore.QMetaObject.connectSlotsByName(rad_ditector)

    def retranslateUi(self, rad_ditector):
        _translate = QtCore.QCoreApplication.translate
        rad_ditector.setWindowTitle(_translate("rad_ditector", "Form"))
        self.label.setText(_translate("rad_ditector", "用户名："))
        self.label_2.setText(_translate("rad_ditector", "密码："))
        self.pushButton.setText(_translate("rad_ditector", "登录"))
        self.checkBox.setText(_translate("rad_ditector", "记住用户名和密码"))

# 加上这个类，命名必须和上面那个类差一个UI
class rad_ditector(QtWidgets.QMainWindow, Ui_rad_ditector):
    def __init__(self):
        super(rad_ditector, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = rad_ditector()
    ui.show()
    sys.exit(app.exec_())
