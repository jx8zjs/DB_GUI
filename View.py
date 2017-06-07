from PyQt5 import QtWidgets
import DBcon
import dialog

#全局变量
dui = None
gresult = None
gclomn = None
number = None

def showTable(ui):
    ui.centralwidget.setColumnCount(5)
    ui.centralwidget.setHorizontalHeaderLabels(["学号", "姓名", "性别", "生日", "专业"])
    global dui
    dui = ui
    SelectUI(dui)

    addEvents(ui)
    addMenuEvents(ui)

def addEvents(ui):
    qw = ui.centralwidget
    qw.itemChanged.connect(outChange)
    qw.itemClicked.connect(outSelect)

def addMenuEvents(ui):
    ui.actionAdd.triggered.connect(newForm)
    ui.actionDelete.triggered.connect(deleteRow)

def disEvents(ui):
    qw = ui.centralwidget
    qw.itemChanged.disconnect(outChange)
    qw.itemClicked.disconnect(outSelect)

def disMenuEvents(ui):
    ui.actionAdd.triggered.disconnect(newForm)
    ui.actionDelete.triggered.disconnect(deleteRow)

def outChange(item):
    print(item.text())
    disEvents(dui)
    disMenuEvents(dui)
    global gclomn
    UpdateUI(dui.centralwidget.selectedIndexes()[0].row(),gclomn,item)
    SelectUI(dui)
    addEvents(dui)
    addMenuEvents(dui)
def outSelect():
    items = dui.centralwidget.selectedIndexes()
    global gclomn
    gclomn = dui.centralwidget.currentColumn()
    print("列："+str(dui.centralwidget.currentColumn())+"type")
    print(type(dui.centralwidget.currentColumn()))
    for it in items:
        print('selected item index found at %s' % it.row())
#查询
def SelectUI(ui):

    print("select开始")
    no = 0
    results = DBcon.Select()
    print("select连接数据库")
    global gresult
    gresult = results
    ui.centralwidget.setRowCount(results.__len__())
    print("select生成界面")
    for row in results:
        for num in range(0,5):
            item = QtWidgets.QTableWidgetItem()
            item.setText("%s"%row[num])
            ui.centralwidget.setItem(no,num,item)
            ui.centralwidget.setAutoScroll(1)
        no = no + 1
    # return results.__len__()
    global number
    number = 2016102501
    for num in range(0,gresult.__len__()):
        if number == gresult[num][0]:
            number = number+1
        else:
            break
    # print(number)

    print("select调用完成")
#添加
def InsertUI():
    InStr = ""
    DBcon.Insert(InStr)

#删除
def DeleteUI(index):
    DBcon.Delete(gresult.__getitem__(index)[0])

#修改
def UpdateUI(index,column,item):
    UpStr = ""
    print("开始数据比对")
    print(type(index))
    for num in range(0,5):
        print("循环"+str(column)+str(num))
        print(type(num))
        print(type(column))
        if num == column :
            print("比较,item.text()类型")
            print(type(item.text()))
            UpStr = UpStr + item.text() + " "
        else:
            print("不相等情况"+str(gresult.__getitem__(index)[num]))
            UpStr = UpStr + str(gresult.__getitem__(index)[num])+" "

    id = gresult.__getitem__(index)[0]
    print("数据" + UpStr+"..id:"+str(id))
    SqlStr = UpStr.split(" ")
    print(SqlStr)
    print(type(SqlStr))
    print(SqlStr[0])
    # date = datetime.datetime.strptime(SqlStr[3],'%Y-%m-%d').date()
    DBcon.Update(int(SqlStr[0]),SqlStr[1],SqlStr[2],SqlStr[3],SqlStr[4],id)


def newForm(menu):
    print(menu)
    dia = dialog.Ui_Dialog()
    qtdia = QtWidgets.QDialog()
    dia.setupUi(qtdia)
    revalue = qtdia.exec_()

    if revalue:
        print(dia.id.text()+' '+dia.major.text()+' '+dia.comboBox.currentText()+' '+dia.dateEdit.text())
        id = int(dia.id.text())
        # birthday = dia.dateEdit.text().replace("/","-")
        date = dia.dateEdit.text().split('/')
        if int(date[1]) < 10 :
            date[1] = '0'+date[1]
        if int(date[2]) < 10 :
            date[2] = '0'+date[2]
        birthday = date[0]+'-'+date[1]+'-'+date[2]
        print(birthday)
        disMenuEvents(dui)
        disEvents(dui)
        DBcon.Insert(id,dia.name.text(),dia.comboBox.currentText(),birthday,dia.major.text())
        SelectUI(dui)
        addMenuEvents(dui)
        addEvents(dui)
    else:
        pass
def deleteRow():
    items = dui.centralwidget.selectedIndexes()
    # for it in items
    #     # print('selected item index found at %s' % it.row())
    #
    reply = QtWidgets.QMessageBox.question(None, '消息', '确认删除？',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    if(reply==QtWidgets.QMessageBox.Yes):
        print(items[0].row())
        disEvents(dui)
        disMenuEvents(dui)
        DeleteUI(items[0].row())
        SelectUI(dui)
        addMenuEvents(dui)
        addEvents(dui)
        print("测试")

    else:
        pass
def getNumber():
    return number