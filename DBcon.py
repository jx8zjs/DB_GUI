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
def Insert(id,name,sex,birthday,major):
    print("开始插入 "+birthday)
    sql = "INSERT INTO students (id,name,sex,birthday,major) VALUE (%d,'%s','%s','%s','%s')"
    data = (id,name,sex,birthday,major)
    cursor.execute(sql % data)
    connect.commit()


# 删除
def Delete(id):
    sql = "DELETE FROM students WHERE id = %d"
    data = (id)
    cursor.execute(sql % data)
    connect.commit()

    print("已关闭")
# 修改
def Update(id,name,sex,birthday,major,wid):
    print("开始修改")
    print(type(wid))
    print(type(id))
    sql = "UPDATE students SET id=%d,name='%s',sex='%s',birthday='%s',major='%s' WHERE id=%d"
    data = (id,name,sex,birthday,major,wid)
    print(sql % data)
    cursor.execute(sql % data)
    print("修改数据中")
    connect.commit()


# 查询
def Select():

        sql = "SELECT * FROM students"
        cursor.execute(sql)
        return cursor.fetchall()


def close():
    cursor.close()
    connect.close()









