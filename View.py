from PyQt5 import QtWidgets
import DBcon

gresult = None
#展示
def showTable(ui):
    ui.centralwidget.setColumnCount(5)
    ui.centralwidget.setHorizontalHeaderLabels(["学号", "姓名", "性别", "生日", "专业"])
    global dui
    dui = ui

    SelectUI(ui)
    addEvents(ui)
#添加事件
def addEvents(ui):
    qw = ui.centralwidget
    qw.itemChanged.connect(outChange)
    qw.itemClicked.connect(outSelect)

def outChange(item):
    # print(item.text())
    pass

def outSelect():
    items = dui.centralwidget.selectedIndexes()
    for it in items:
        print('selected item index found at %s' % it.row())
#查询
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
#添加
def InsertUI():
    pass
#删除
def DeleteUI():
    pass
#修改
def UpdateUI():
    pass