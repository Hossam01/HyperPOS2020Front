#!/usr/bin/env python3
# -*     - coding: utf-8 -*-
"""
Created on Mon Jun 29 19:52:06 2020



@author: emad
"""
#####
import sys
from pathlib import Path

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from mysql.connector import Error

from access.authorization_class.user_module import CL_userModule
# import Controller
from access.main_login_class.main import CL_main
from data_connection.h1pos import db1


class CL_login(QtWidgets.QDialog):
    switch_window = QtCore.pyqtSignal()
    username=""
    def FN_login(self):
        try:
            if len(self.LE_userName.toPlainText()) > 0 and len(self.LE_password.toPlainText()) > 0:
                print("Login!")
                self.username = self.LE_userName.toPlainText()
                self.password = self.LE_password.toPlainText()
                self.LE_userName.clear()
                self.LE_password.clear()
                self.FN_loadData(self.username, self.password)

            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Please enter your Username and Password")
        except:
            print(sys.exc_info())



    def FN_loadData(self, username, password):
        try:
            self.conn = db1.connect()
            sql_select_Query = "select * from SYS_USER where user_name = %s and user_password = %s and USER_STATUS  = 1"

            x = (username, password,)
            mycursor = self.conn.cursor()
            mycursor.execute(sql_select_Query, x)
            record = mycursor.fetchone()

            if mycursor.rowcount > 0:
                # save the login in the table
                CL_userModule.user_name = record[0]

                print(username)
                self.switch_window.emit()

            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Incorrect Username and Password")
                print("Please Enter Correct Username and Password")

        except Error as e:
            print("Error reading data from MySQL table", e)


    def __init__(self):
        super(CL_login, self).__init__()
        cwd = Path.cwd()
        mod_path = Path(__file__).parent.parent.parent
        dirname = mod_path.__str__() + '/presentation/main_login_ui'
        filename = dirname + '/AdminLogin.ui'

        loadUi(filename, self)
        self.setWindowTitle('HyperPOS Login Page')
        self.LE_userName.setText("admin")
        self.LE_password.setText("123")
        self.btn_login.clicked.connect(self.FN_login)

class CL_controller():
    def __init__(self):
        pass

    def FN_show_login(self):
        self.login = CL_login()
        self.user = self.login.username
        self.login.switch_window.connect(self.FN_show_main)
        self.login.show()

    def FN_show_main(self):
        self.window = CL_main()
        self.login.close()
        self.window.showMaximized()


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        controller = CL_controller()
        controller.FN_show_login()
        sys.exit(app.exec_())
    except Exception as err:

        print(err)

if __name__ == '__main__':
    main()
