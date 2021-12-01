# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 1/12/2021 21:15
# @File: mysql.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import pymysql
import yaml
from model.contact import Contact

file = open('config.yaml', 'r', encoding='utf-8')
config = yaml.load(file, Loader=yaml.FullLoader)
file.close()


def getConnect():
    coon = pymysql.Connect(host=config['DataBase']['host'],
                           user=config['DataBase']['username'],
                           passwd=config['DataBase']['password'],
                           db=config['DataBase']['db'], autocommit=True)
    return coon


def queryAll() -> list:
    coon = getConnect()
    cur = coon.cursor()
    cur.execute('SELECT * FROM USER')
    data = []
    for i in cur.fetchall():
        data.append(Contact(i[1], i[2], i[3], i[4], i[0]))
    coon.close()
    cur.close()
    return data


def query(cid):
    coon = getConnect()
    cur = coon.cursor()
    cur.execute('SELECT * FROM USER WHERE id = ' + str(cid))
    tmp = list(cur.fetchone())
    coon.close()
    cur.close()
    return Contact(tmp[1], tmp[2], tmp[3], tmp[4], tmp[0])


def delete(cid):
    coon = getConnect()
    cur = coon.cursor()
    sql = "DELETE FROM USER WHERE id = {}"
    cur.execute(sql.format(cid))
    coon.close()
    cur.close()


def update(cid, contact):
    coon = getConnect()
    cur = coon.cursor()
    sql = "UPDATE USER SET name = '{}', " \
          "gender = '{}', " \
          "phone = '{}', " \
          "wx = '{}' " \
          "WHERE id = {}"
    cur.execute(sql.format(contact.name,contact.gender,contact.phone,contact.wx_code,cid))
    coon.close()
    cur.close()



def insert(data):
    coon = getConnect()
    cur = coon.cursor()
    sql = "INSERT INTO USER(name, gender, phone, wx) VALUES ('{}', '{}','{}', '{}')"
    for i in data:
        cur.execute(sql.format(i.name, i.gender, i.phone, i.wx_code))
    coon.close()
    cur.close()
