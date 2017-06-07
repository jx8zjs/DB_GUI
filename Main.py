import sys
from PyQt5 import QtWidgets
import UI
import View
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI.Ui_MainMW()
    qtUI = QtWidgets.QMainWindow()
    ui.setupUi(qtUI)
    qtUI.show()
    ui.centralwidget.parent().setObjectName("学生管理系统")
    ui.centralwidget.resize(ui.centralwidget.parent().size())


    View.showTable(ui)
    #View.addEvents(ui)
    exit(app.exec())