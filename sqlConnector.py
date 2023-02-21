import mysql.connector


def connectToDB():
    mydb = mysql.connector.connect(
        host="sql9.freemysqlhosting.net",
        user="sql9599584",
        password="Ww3ax3MrzE"
    )
    print(mydb)

connectToDB()