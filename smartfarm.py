import sys,time,json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
# import mysql.connector as con
import MySQLdb as con




ui, _ = loadUiType('Smart Farm Management System.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('SmartFarm Management System')

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menubar.setVisible(False)
        self.b01.clicked.connect(self.login)

        self.menuUsers.triggered.connect(self.show_add_new_user_tab)

        # self.menuUsers.triggered.connect(self.show_records_tab)
        self.menuUsers.triggered.connect(self.save_user_details)
        self.menuVacination_Records.triggered.connect(self.show_records_tab)
        self.menuInquiries.triggered.connect(self.show_inquiries)
        self.menuReplies.triggered.connect(self.show_replies)
        self.menuTestimonies.triggered.connect(self.show_testimonies)
        self.menuFarm_Produce.triggered.connect(self.show_produce)
        self.menuNoticeable_Diseases.triggered.connect(self.noticeable_diseases)
        # self.menuUsers.triggered.connect(self.show_vaccination)
        self.actionExit.triggered.connect(self.exit_smartfarm)

        self.B11.clicked.connect(self.save_user_details)
        # self.B11.clicked.connect(self.S)

# Login Form
    def login(self):
        un = self.tb01.text()
        pw = self.tb02.text()
        if (un=="admin" and pw=="admin"):
            self.menubar.setVisible(True)
            self.tabWidget.setCurrentIndex(1)
            # QMessageBox.Ok(self, "SMARTFARM","WELCOME")
        else:
            QMessageBox.information(self, "SmartFarm Management System", "Invalid Cred Try Again")
            self.l01.setText("**INVALID CREDENTIALS**")

# Add user
    def show_add_new_user_tab(self):
        self.tabWidget.setCurrentIndex(2)

       

# Show records 
    def show_records_tab(self):
        self.tabWidget.setCurrentIndex(3)

# Inquiries
    def show_inquiries(self):
        self.tabWidget.setCurrentIndex(4)

# Replies
    def show_replies(self):
        self.tabWidget.setCurrentIndex(5)

# Testimonies
    def show_testimonies(self):
        self.tabWidget.setCurrentIndex(6)

# Farm Produce
    def show_produce(self):
        self.tabWidget.setCurrentIndex(7)

# Noticeable Diseases
    def noticeable_diseases(self):
        self.tabWidget.setCurrentIndex(8)


# Exit  the program
    def exit_smartfarm(self):
        self.tabWidget.setCurrentIndex(0)
        self.menubar.setVisible(False)
        self.tb01.clear()
        self.tb02.clear()
        self.l01.setText("WELCOME BACK | SMARTfARM")



    # db

    # Connect to Database
    def connectToDatabase(self):
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName("databases/smartfarm.sql")

        if not self.database.open():
            print("Unable to open data source file.")
            sys.exit(1)

        #Check if the table exists
        tables_needed = {'Users','farm_produce','inquiries','noticeable_diseases','record','testimonies'}
        tables_not_found = tables_needed - set(self.database.tables())
        if tables_not_found:
            QMessageBox.critical(None, 'Error',
                                 'The following tables are missing from the database: {}'.
                                 format(tables_not_found))
            sys.exit(1)

    def save_user_details(self):
        try:
            mydb=con.connect(host='localhost/phpmyadmin', user='root',password='',db='farm')
            # mydb=con.connect("localhost", "root","New@user.com1234","farm")
            cursor = mydb.cursor()
            # cursor.execute("DROP TABLE IF EXISTS USERS")
            # query = "CREATE TABLE USERS(" \
            #         "id int(10)," \
            #         "user_name varchar(20)," \
            #         "full_name varchar(50)," \
            #         "gender varchar(10)," \
            #         "vocation varchar(10)," \
            #         "date_of_birth varchar(20)," \
            #         "age int(10)," \
            #         "PRIMARY KEY (id))"
            # cursor.execute(query)
            # # mydb.close()
            # mydb=con.connect("localhost", "root","New@user.com1234","farm")
            # cursor=mydb.cursor()
            # query_insert= """INSERT INTO USERS (id int primary key,username,full_name,gender,vocation,date_of_birth,age))
            #                VALUES (%s,'%s','%s',%s,'%s',%s,%s)""")
            # cursor.execute(query_insert)
            # # result = cursor.fetchall()
            # # return result
            # mydb.commit()
            # print("Record insterted successfully")



            user_name = self.tb11_2.text()
            full_name = self.tb12.text()
            gender = self.cb11.currentText()
            vocation = self.cb22.text()
            date_of_birth = self.tb13.text()
            age = self.tb11.text()

            query = "insert into Users (user_name,full_name,gender,vocation,date_of_birth,age) values(%s,%s,%s,%s,%s)"
            values = (user_name,full_name,gender,vocation,date_of_birth,age)
            cursor.execute(query,values)
            mydb.commit()

            self.menuUsers.setText("User details saved successfully")
            QMessageBox.information(self, "SmartFarm management system","User details added successfully")
        except:
            print("Cannot connect to the Database")







def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()