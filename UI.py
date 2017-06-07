# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmw.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,QtWidgets

class Ui_MainMW(object):
    def setupUi(self, MainMW):
        MainMW.setObjectName("MainMW")
        MainMW.resize(800, 600)
        self.centralwidget = QtWidgets.QTableWidget(MainMW)
        self.centralwidget.setRowCount(1)
        self.centralwidget.setColumnCount(1)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.horizontalHeader().setVisible(False)
        self.centralwidget.horizontalHeader().setCascadingSectionResizes(False)
        self.centralwidget.horizontalHeader().setSortIndicatorShown(False)
        self.menubar = QtWidgets.QMenuBar(MainMW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainMW.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMW)
        self.statusbar.setObjectName("statusbar")
        MainMW.setStatusBar(self.statusbar)
        self.actionAdd = QtWidgets.QAction(MainMW)
        self.actionAdd.setObjectName("actionAdd")
        self.actionDelete = QtWidgets.QAction(MainMW)
        self.actionDelete.setObjectName("actionDelete")
        self.menu.addAction(self.actionAdd)
        self.menu.addAction(self.actionDelete)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainMW)
        QtCore.QMetaObject.connectSlotsByName(MainMW)

    def retranslateUi(self, MainMW):
        _translate = QtCore.QCoreApplication.translate
        MainMW.setWindowTitle(_translate("MainMW", "学生管理系统"))
        self.menu.setTitle(_translate("MainMW", "添加数据"))
        self.actionAdd.setText(_translate("MainMW", "添加行"))
        self.actionDelete.setText(_translate("MainMW", "删除"))