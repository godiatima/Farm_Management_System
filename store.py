import sys,os
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class CreateDatabaseObjects():
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName("farm.sql")

    if not database.open():
        print("Unable to Open data source file.")
        print("Connection failed:", database.lastError().text())
        sys.exit(1)
    query = QSqlQuery()
    # Erase tables if already exists
    query.exec_("DROP TABLE IF EXISTS Users")
    query.exec_("DROP TABLE IF EXISTS farm_produce")
    query.exec_("DROP TABLE IF EXISTS inquiries")
    query.exec_("DROP TABLE IF EXISTS noticeable_diseases")
    query.exec_("DROP TABLE IF EXISTS record")
    query.exec_("DROP TABLE IF EXISTS testimonies")

    # Create Customers table
    query.exec_("""CREATE TABLE Users (
            User_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            username VARCHAR (100) NOT NULL,
            full_name VARCHAR (100) NOT NULL,
            gender VARCHAR (20) NOT NULL,
            vocation VARCHAR (10) NOT NULL,
            age int (10) NOT NULL)""")

    # Creat stores table
    query.exec_("""CREATE TABLE farm_produce (
            farm_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            farm_produce VARCHAR (100) NOT NULL,
            type VARCHAR (20),
            for_sale VARCHAR (10),
            save_details VARCHAR (5))""")

    # Create orders table
    query.exec_("""CREATE TABLE inquiries (
            inquiries_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
           id INTEGER,
           vocation VARCHAR (10) NOT NULL,
           issues VARCHAR (20) NOT NULL,
           in_details VARCHAR(20) NOT NULL,
           others VARCHAR(20))""")

    # Noticeable Diseases
    query.exec_("""CREATE TABLE noticeable_diseases (
                inquiries_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
               id INTEGER,
               diseases VARCHAR (10) NOT NULL,
               symptoms VARCHAR (20) NOT NULL,
               mitigation VARCHAR(20) NOT NULL,
               others VARCHAR(20))""")


    query.exec_("""CREATE TABLE noticeable_diseases (
                    inquiries_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                   id INTEGER,
                   diseases VARCHAR (10) NOT NULL,
                   symptoms VARCHAR (20) NOT NULL,
                   mitigation VARCHAR(20) NOT NULL,
                   others VARCHAR(20))""")

    # Create data and populate the table
class InsertDataIntoTables():
    Users = [["Jemo", "James Smith", "NULL","Male","farmer",21], ["Marrie", "Mary Ndungu", 'NULL',"female","vet",22]]


    # Create the QSqlQuery instance
    query = QSqlQuery()

    query.prepare("INSERT INTO Users (username, full_name,gender,vocation,age) VALUES (?,?,?,?,?)")
    for i in range(len(Users)):
        username = Users[i][0]
        full_name = Users[i][1]
        gender = Users[i][2]
        vocation = Users[i][3]
        age = Users[i][4]
        query.addBindValue(username)
        query.addBindValue(full_name)
        query.addBindValue(gender)
        query.addBindValue(vocation)
        query.addBindValue(age)
        query.exec_()


if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    CreateDatabaseObjects()
    InsertDataIntoTables()
    sys.exit(app.exec_())