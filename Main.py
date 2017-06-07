import sys
from PyQt5 import QtWidgets
import UI
import DBcon

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




    no = 0
    results = DBcon.Select();
    ui.centralwidget.setRowCount(results.__len__())
    for row in results:

    #     print("%d."% no,end = "")
    #     print("id:%d num:%d" % row)
    #     print("%d"%row[0])

        for num in range(0,5):
            item = QtWidgets.QTableWidgetItem()
            item.setText("%s"%row[num])
            ui.centralwidget.setItem(no,num,item)
            ui.centralwidget.setAutoScroll(1)
        no = no + 1


    exit(app.exec())