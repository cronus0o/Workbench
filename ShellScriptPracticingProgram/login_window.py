# Login Window Screen

import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox
from account_administrator import DatabaseAdministrator

class LoginWindow(QDialog) :
    def __init__(self) :
        super().__init__()
        self.admin = DatabaseAdministrator()
        self.admin.create_table()
        self.login_user_id = None
        self.layout = QVBoxLayout()
        self.init_ui()
        
    def init_ui(self) :
        self.setWindowTitle("Hello")
        self.resize(300, 200)
        self.clear_layout()


        self.button_login = QPushButton("Log In")
        self.button_signin = QPushButton("Sign In")
        self.layout.addWidget(self.button_login)
        self.layout.addWidget(self.button_signin)
    
        self.setLayout(self.layout)
        self.button_login.clicked.connect(self.login)
        self.button_signin.clicked.connect(self.signin)


    def clear_layout(self) :
        while self.layout.count() :
            child = self.layout.takeAt(0)
            if child.widget() :
                child.widget().deleteLater()

    def login(self) :
        self.setWindowTitle("Login")
        self.clear_layout()

        self.label_id = QLabel("Enter ID:")
        self.input_id = QLineEdit()

        self.label_pw = QLabel("Enter Password:")
        self.input_pw = QLineEdit()
        self.input_pw.setEchoMode(QLineEdit.Password)

        self.button = QPushButton("Login")
        self.button.clicked.connect(self.check_credentials)

        self.layout.addWidget(self.label_id)
        self.layout.addWidget(self.input_id)
        self.layout.addWidget(self.label_pw)
        self.layout.addWidget(self.input_pw)
        self.layout.addWidget(self.button)

    def signin(self) :
        self.setWindowTitle("Sign In")
        self.clear_layout()

        self.label_id = QLabel("Enter New ID:")
        self.input_id = QLineEdit()

        self.label_pw = QLabel("Enter New Password:")
        self.input_pw = QLineEdit()
        self.input_pw.setEchoMode(QLineEdit.Password)

        self.button = QPushButton("Create Account")
        self.button.clicked.connect(self.create_account)

        self.layout.addWidget(self.label_id)
        self.layout.addWidget(self.input_id)
        self.layout.addWidget(self.label_pw)
        self.layout.addWidget(self.input_pw)
        self.layout.addWidget(self.button)

    def check_credentials(self) :
        user_id = self.input_id.text()
        password = self.input_pw.text()

        if self.admin.check_credentials(user_id, password) :
            self.login_user_id = user_id
            QMessageBox.information(self, "Success", f"Welcome {user_id}!")
            self.accept()
        else :
            QMessageBox.warning(self, "Login Failed", "Invalid ID or Password.")
            self.init_ui()

    def create_account(self):
        user_id = self.input_id.text()
        password = self.input_pw.text()

        if self.admin.create_account(user_id, password) :
            QMessageBox.information(self, "Account Created", "Account successfully registered!")
        else :
            QMessageBox.warning(self, "Failed", "Account creation failed. ID may already exist.")
        self.init_ui()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())