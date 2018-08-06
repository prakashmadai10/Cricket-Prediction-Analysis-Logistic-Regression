import sqlite3
import os
conn = sqlite3.connect('Major.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS countryinfo(name TEXT, match int, won int,lost int,tied int,noresult int,wl REAL,hs int,ls int)')
'''
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

    ca.execute(querry)
    res=ca.fetchall()

    str1 = "select id from playerinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)

    ca.execute(querry)
    re = ca.fetchall()

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

    str1 = "select details from playerinfo where name LIKE "

    querry = str1 + "'{}'".format(str2)

    ca.execute(querry)
    res7 = ca.fetchall()

    str1 = "select name from playerinfo where name LIKE "

    querry = str1 + "'{}'".format(str2)

    ca.execute(querry)
    res8 = ca.fetchall()

    return res,res1,res2,res3,res4,res5,res6,res7,re,res8

def desh(countr):
    a='alter table countryinfo add ranking int'
    con = sqlite3.connect('Major.db')
    ca = con.cursor()
    str2 = "%" + countr + "%"

    str1 = "select match from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res = ca.fetchall()


    str1 = "select won from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)

    ca.execute(querry)
    re = ca.fetchall()

    str1 = "select lost from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res1 = ca.fetchall()

    str1 = "select tied from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res2 = ca.fetchall()

    str1 = "select noresult from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res3 = ca.fetchall()

    str1 = "select wl from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res4 = ca.fetchall()

    str1 = "select hs from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res5 = ca.fetchall()

    str1 = "select ls from countryinfo where name LIKE "

    querry = str1 + "'{}'".format(str2)

    ca.execute(querry)
    res6 = ca.fetchall()

    str1 = "select name from countryinfo where name LIKE "

    querry = str1 + "'{}'".format(str2)

    ca.execute(querry)
    res8 = ca.fetchall()

    str1 = "select rank from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    res9 = ca.fetchall()


    str1 = "select mostwins from countryinfo where name LIKE "
    querry = str1 + "'{}'".format(str2)
    ca.execute(querry)
    ress = ca.fetchall()
    return res,re,res1,res2,res3,res4,res5,res6,res8,res9,ress




#create_table()
#desh('australia')
#data()
