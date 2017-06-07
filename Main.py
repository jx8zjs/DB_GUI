import sys
from PyQt5 import QtWidgets
import UI
import Select

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI.Ui_MainMW()
    qtUI = QtWidgets.QMainWindow()
    ui.setupUi(qtUI)
    qtUI.show()
    ui.centralwidget.parent().setObjectName("学生管理系统")
    ui.centralwidget.resize(ui.centralwidget.parent().size())
    ui.centralwidget.setColumnCount(5)

    ui.centralwidget.setHorizontalHeaderLabels(["学号","姓名","性别","生日","专业"])
    #ui.centralwidget.adjustSize()

    #查询
    count = Select.SelectUI(ui)
    print(count)

    exit(app.exec())