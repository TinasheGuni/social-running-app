# import necessary modules
import sys
from PyQt6.QtWidgets import  *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap

class NewUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        # self.setFixedSize(360, 320)
        self.setWindowTitle("New Account")
        self.setUpWindow()

    def setUpWindow(self):
        label_login = QLabel("Create New Account", self)
        label_login.setFont(QFont("Arial", 20))
        label_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Username/ Email
        label_username = QLabel("Username:", self)
        self.edit_username = QLineEdit()
        self.edit_username.setPlaceholderText("Username / email")

        # Full name
        label_fullname = QLabel("Full Name:", self)
        self.edit_fullname = QLineEdit()
        self.edit_fullname.setPlaceholderText("Name Surname")

        # Password
        label_password = QLabel("Password:", self)
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.edit_password.setPlaceholderText("New Password")

        label_password_confirm = QLabel("Confirm Password:", self)
        self.edit_password_confirm = QLineEdit()
        self.edit_password_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        self.edit_password_confirm.setPlaceholderText("Confirm Password")

        # Sign Up
        button_sign_up = QPushButton("Sign Up", self)
        button_sign_up.clicked.connect(self.confirmSignUp)

        # Main Layout
        layout_main = QVBoxLayout()
        layout_main.addWidget(label_login)
        layout_main.addStretch()
        layout_main.addWidget(label_username)
        layout_main.addStretch()
        layout_main.addWidget(self.edit_username)
        layout_main.addStretch()
        layout_main.addWidget(label_fullname)
        layout_main.addStretch()
        layout_main.addWidget(self.edit_fullname)
        layout_main.addStretch()
        layout_main.addWidget(label_password)
        layout_main.addWidget(self.edit_password)
        layout_main.addWidget(label_password_confirm)
        layout_main.addWidget(self.edit_password_confirm)
        layout_main.addStretch()
        layout_main.addWidget(button_sign_up)

        self.setLayout(layout_main)

    def confirmSignUp(self):
        txt_name = self.edit_name.text()
        txt_password = self.edit_password.text()
        txt_confirm_password = self.edit_password_confirm.text()

        if txt_name == "" or txt_password == "":
            QMessageBox.warning(self, "Error Message!",
                                "Missing username or password",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        elif txt_password != txt_confirm_password:
            QMessageBox.warning(self, "Error Message!",
                                "The passwords you entered do not match.",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            with open("files/users.txt", "a+") as f:
                f.write("\n" + txt_name + " ")
                f.write(txt_password)
            self.close()