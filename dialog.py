# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import View
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(459, 301)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 54, 12))
        self.label.setObjectName("label")
        self.id = QtWidgets.QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.id.setText(str(View.getNumber()))
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 60, 54, 12))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(270, 50, 113, 20))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 54, 12))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 90, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 90, 54, 12))
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(270, 90, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1990, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 54, 12))
        self.label_5.setObjectName("label_5")
        self.major = QtWidgets.QLineEdit(Dialog)
        self.major.setGeometry(QtCore.QRect(90, 140, 113, 20))
        self.major.setObjectName("major")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加学生"))
        self.label.setText(_translate("Dialog", "学号"))
        self.label_2.setText(_translate("Dialog", "姓名"))
        self.label_3.setText(_translate("Dialog", "性别"))
        self.comboBox.setItemText(0, _translate("Dialog", "男"))
        self.comboBox.setItemText(1, _translate("Dialog", "女"))
        self.label_4.setText(_translate("Dialog", "生日"))
        self.label_5.setText(_translate("Dialog", "专业"))

