# This is a main start page of program

import sys
from PyQt5.QtWidgets import QApplication, QDialog

from login_window import LoginWindow
from main_window import MainWindow


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    login_window = LoginWindow()

    if login_window.exec_() == QDialog.Accepted :
        print("loginPOP")
        user_name = login_window.login_user_id
        main_window = MainWindow(user_name)
        main_window.show()
        sys.exit(app.exec_())