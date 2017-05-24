import sys
from PyQt5 import QtWidgets
import ui

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ui.Ui_MainMW()
    qtUI = QtWidgets.QMainWindow()
    ui.setupUi(qtUI)
    qtUI.show()
    ui.centralwidget.parent().setObjectName("学生管理系统")
    ui.centralwidget.resize(ui.centralwidget.parent().size())
    ui.centralwidget.setColumnCount(5)
    ui.centralwidget.setHorizontalHeaderLabels(["aaa","bbb","ccc","ddd","eee"])
    #ui.centralwidget.adjustSize()
    ui.centralwidget.setRowCount(10)
    item  = QtWidgets.QTableWidgetItem()
    item.setText("123")
    ui.centralwidget.setItem(0,0,item)
    ui.centralwidget.setAutoScroll(1)
    exit(app.exec())