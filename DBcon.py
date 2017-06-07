#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  pymysql.cursors

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='0213',
    db='mydb',
    charset='utf8'
)
cursor = connect.cursor()

# 插入
def Insert(string):
    sql = "INSERT INTO students (id,name,sex,birthday,major) VALUE (%s)"
    data = (string)
    cursor.execute(sql % data)
    connect.commit()

    cursor.close()
    connect.close()

# 删除
def Delete(id):
    sql = "DELETE FROM students WHERE id = %d"
    data = (id)
    cursor.execute(sql % data)
    connect.commit()

    cursor.close()
    connect.close()
    print("已关闭")
# 修改
def Update(upstring,id):
    sql = "UPDATE students SET %s WHERE id=%d"
    data = (upstring,id)
    cursor.execute(sql % data)
    connect.commit()

    cursor.close()
    connect.close()

# 查询
def Select():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    return cursor.fetchall()

    cursor.close()
    connect.close()





