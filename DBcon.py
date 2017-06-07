#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  pymysql.cursors
connect = pymysql.Connect(
    host='localhost',
    port=3308,
    user='root',
    passwd='mysql',
    db='mydb',
    charset='utf8'
)
cursor = connect.cursor()

# 插入
# sql = "INSERT INTO students (id,name,sex,birthday,major,grade) VALUE (%d,%d)"
# data = (15,211)
# cursor.execute(sql % data)
# connect.commit()

# 删除

# sql = "DELETE FROM students WHERE id = %d"
# data = (15)
# cursor.execute(sql % data)
# connect.commit()

# 修改
# sql = "UPDATE students SET num=%d WHERE id=%d"
# data = (121,15)
# cursor.execute(sql % data)
# connect.commit()

# 查询
def Select():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    return cursor.fetchall()
    cursor.close()
    connect.close()
    # no = 0
    # for row in cursor.fetchall():
    #     no = no + 1
    #     print("%d."% no,end = "")
    #     print("id:%d num:%d" % row)




