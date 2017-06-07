from PyQt5 import QtWidgets
import DBcon

def SelectUI(ui):
    no = 0
    results = DBcon.Select();
    ui.centralwidget.setRowCount(results.__len__())
    for row in results:
        for num in range(0,5):
            item = QtWidgets.QTableWidgetItem()
            item.setText("%s"%row[num])
            ui.centralwidget.setItem(no,num,item)
            ui.centralwidget.setAutoScroll(1)
        no = no + 1
    return results.__len__()
