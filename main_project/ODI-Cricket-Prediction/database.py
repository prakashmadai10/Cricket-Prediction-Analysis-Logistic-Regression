import sqlite3
import os
conn = sqlite3.connect('Major.db')
c = conn.cursor()

'''
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS playerinfo(name TEXT, match int, inn int,run int,hs int,avg REAL,sr REAL)')
def data():
    c.execute("insert into playerinfo values('virat kohli',209,201,9663,183,58.21,92.14)")
    conn.commit()
    c.close()
    conn.close()
'''
def readdata(naam):
    con = sqlite3.connect('Major.db')
    ca = con.cursor()
    str2="%"+naam+"%"
    str1="select match from playerinfo where name LIKE "
    querry=str1+"'{}'".format(str2)
    print(querry)
    ca.execute(querry)
    res=ca.fetchall()



    str1 = "select inn from playerinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res1 = ca.fetchall()


    str1 = "select run from playerinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res2 = ca.fetchall()


    str1 = "select hs from playerinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res3 = ca.fetchall()


    str1 = "select avg from playerinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res4 = ca.fetchall()

    str1 = "select sr from playerinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res5 = ca.fetchall()


    str1 = "select photo from playerinfo where name LIKE "

    querry = str1 + "'{}'".format(str2)

    ca.execute(querry)
    res6 = ca.fetchall()





    return res,res1,res2,res3,res4,res5,res6





#create_table()
#data()
readdata('ange')