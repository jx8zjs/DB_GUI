from PyQt5 import QtWidgets
import DBcon
import dialog
from PyQt5 import QtCore

gresult = None
def showTable(ui):
    ui.centralwidget.setColumnCount(5)
    ui.centralwidget.setHorizontalHeaderLabels(["学号", "姓名", "性别", "生日", "专业"])
    global dui
    dui = ui

    SelectUI(ui)
    addEvents(ui)

def addEvents(ui):
    qw = ui.centralwidget
    qw.itemChanged.connect(outChange)
    qw.itemClicked.connect(outSelect)

def addMenuEvents(ui):
    ui.actionAdd.triggered.connect(newForm)
    ui.actionDelete.triggered.connect(deleteRow)

def outChange(item):
    print(item.text())

def outSelect():
    items = dui.centralwidget.selectedIndexes()
    for it in items:
        print('selected item index found at %s' % it.row())
#查询
def SelectUI(ui):
    no = 0
    results = DBcon.Select()
    global gresult
    gresult = results
    ui.centralwidget.setRowCount(results.__len__())
    for row in results:
        for num in range(0,5):
            item = QtWidgets.QTableWidgetItem()
            item.setText("%s"%row[num])
            ui.centralwidget.setItem(no,num,item)
            ui.centralwidget.setAutoScroll(1)
        no = no + 1
    # return results.__len__()

#添加
def InsertUI():
    InStr = ""
    DBcon.Insert(InStr)

#删除
def DeleteUI(index):
    DBcon.Delete(gresult.__getitem__(index)[0])

#修改
def UpdateUI(index):
    UpStr = ""
    id = gresult.__getitem__(index)[0]
    DBcon.Update(UpStr,id)

def newForm(menu):
    print(menu)
    dia = dialog.Ui_Dialog()
    qtdia = QtWidgets.QDialog()
    dia.setupUi(qtdia)
    qtdia.exec_()
def deleteRow():
    items = dui.centralwidget.selectedIndexes()
    for it in items:
        print('selected item index found at %s' % it.row())
    reply = QtWidgets.QMessageBox.question(None, '消息', '确认删除？',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    if(reply==QtWidgets.QMessageBox.Yes):
        print('delete')
    else:
        pass