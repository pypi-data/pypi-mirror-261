def CDB(text,mydb):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE " + text)

def CTB(text,mydb):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE " + text)

def ITBV(text, text1,text2,mydb):
    sqlFormula = "INSERT INTO " + text + text1
    mycursor = mydb.cursor()
    mycursor.execute(sqlFormula, text2)
    mydb.commit()

def ITBVS(text, text1,text2,mydb):
    sqlFormula = "INSERT INTO " + text + text1
    mycursor = mydb.cursor()
    mycursor.executemany(sqlFormula, text2)
    mydb.commit()
