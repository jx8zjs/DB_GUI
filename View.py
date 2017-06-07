from PyQt5 import QtWidgets
import DBcon

gresult = None
def showTable(ui):
    ui.centralwidget.setColumnCount(5)
    ui.centralwidget.setHorizontalHeaderLabels(["学号", "姓名", "性别", "生日", "专业"])
    global dui
    dui = ui
    no = 0
    global gresult
    results = DBcon.Select();
    gresult = results
    ui.centralwidget.setRowCount(results.__len__())
    for row in results:
        for num in range(0, 5):
            item = QtWidgets.QTableWidgetItem()
            item.setText("%s" % row[num])
            ui.centralwidget.setItem(no, num, item)
            ui.centralwidget.setAutoScroll(1)
        no = no + 1
    addEvents(ui)

def addEvents(ui):
    qw = ui.centralwidget
    qw.itemChanged.connect(outChange)
    qw.itemClicked.connect(outSelect)

def outChange(item):
    print(item.text())

def outSelect():
    items = dui.centralwidget.selectedIndexes()
    for it in items:
        print('selected item index found at %s' % it.row())
