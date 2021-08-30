from pathlib import Path

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.uic import loadUi

from access.authorization_class.user_module import CL_userModule


class CL_main(QtWidgets.QDialog):
    switch_window = QtCore.pyqtSignal()


    def __init__(self):
        try:
            forms = []
            super(CL_main, self).__init__()
            cwd = Path.cwd()
            mod_path = Path(__file__).parent.parent.parent
            dirname = mod_path.__str__() + '/presentation/main_login_ui'
            filename = dirname + '/Cashier_New.ui'
            loadUi(filename, self)

            # print (CL_userModule.user_name)
            CL_userModule.loadPrivilages(self)
            CL_userModule.FN_AuthBranchUser(self)
            CL_userModule.FN_AuthSectionUser(self)

            self.setWindowTitle('HyperPOS Main Page')
        except Exception as err:
            print(err)

    # close application event
    def closeEvent(self, event):
        # print("event")
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit Application?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QApplication.quit()
        else:
            event.ignore()