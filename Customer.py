import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gamz"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS customer(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
def remove():
    ID = input("Please enter an ID")
    if ID == "0":
        start()
    else:
        Q = "SELECT count(*) FROM customer where id='{}'".format(ID)
        mycursor.execute(Q)
        myresult = mycursor.fetchall()
        I = myresult[0][0]
        QQ = "SELECT count(*) FROM customer where id < '{}'".format(ID)
        mycursor.execute(QQ)
        myresult = mycursor.fetchall()
        II = myresult[0][0]
        if I < 1:
            print("Invalid ID, please try again")
            remove()
        else:
            print("Row =", II + 1)
            r = input("Please type 1 to confirm")
            if r == "1":
                query = "DELETE FROM customer where id = '{}'".format(ID)
                mycursor.execute(query)
                mydb.commit()
                print("Finish remove")
                print("type ID = 0 to go back")
                remove()
            else:
                remove()


def update():
    ID = input("Please enter an ID")

    if ID == "0":
        start()
    else:
        Q = "SELECT count(*) FROM customer where id='{}'".format(ID)
        mycursor.execute(Q)
        myresult = mycursor.fetchall()
        I = myresult[0][0]
        QQ = "SELECT count(*) FROM customer where id < '{}'".format(ID)
        mycursor.execute(QQ)
        myresult = mycursor.fetchall()
        II = myresult[0][0]
        if I < 1:
            print("Invalid ID, please try again")
            update()
        else:
            print ("Row =", II+1)
            newn = input("Please enter new name")
            newa = input("Please enter new address")
            query = "Update customer SET name= '{}', address = '{}' where id = '{}'".format(newn, newa, ID)
            mycursor.execute(query)
            mydb.commit()
            print("Finish update")
            print("type ID = 0 to go back")
            update()
def add():
    name = input("Please enter name")
    if name == "none":
        start()
    else:
        address = input("Please enter address")

        query = "SELECT count(*) FROM customer where name ='{}'".format(name)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        D = myresult[0][0]

        if D == 0:
            sql = "INSERT INTO customer (name, address) VALUES (%s,%s)"
            val = [name, address]
            mycursor.execute(sql, val)
            mydb.commit()
            print("Finish insert")
            print("type name = none to go back")
            add()
        else:
            print("Already exist please try again")
            add()
def start():
    Input = input("Please select Add or Update or Remove or Close")

    if Input == "Add":
        add()
    elif Input == "Update":
        update()
    elif Input == "Remove":
        remove()
    else:
        print("Finish")


start()