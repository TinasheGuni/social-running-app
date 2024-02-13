# Import the necessary modules
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import  QFont, QPixmap
from PyQt6.QtCore import Qt

from user_registration import NewUserDialog

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # self.setFixedSize(360, 220)
        self.setWindowTitle("Login")

        self.setUpWindow()
        self.show()

    def setUpWindow(self):
        self.login_is_successful = False;

        label_login = QLabel("Sign in", self)
        label_login.setFont(QFont("Arial", 20))

        # username
        label_username = QLabel("Username:", self)
        self.edit_username = QLineEdit(self)
        self.edit_username.setPlaceholderText("email/ username")

        layout_username = QVBoxLayout()
        layout_username.addWidget(label_username)
        layout_username.addWidget(self.edit_username)

        # password
        label_password = QLabel("Password:", self)
        self.edit_password = QLineEdit(self)
        self.edit_password.setPlaceholderText("Password")
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.cb_show_password = QCheckBox("Show Password", self)
        self.cb_show_password.toggled.connect(self.showPassword)

        layout_password = QVBoxLayout()
        layout_password.addWidget(label_password)
        layout_password.addWidget(self.edit_password)
        layout_password.addWidget(self.cb_show_password)

        # sign in button
        button_login = QPushButton("Login", self)
        button_login.clicked.connect(self.userVerification)

        # New user
        label_new_user = QLabel("New User?", self)
        button_sign_up = QPushButton("Sign Up", self)
        button_sign_up.clicked.connect(self.createNewUser)

        layout_new_user = QHBoxLayout()
        layout_new_user.addWidget(label_new_user)
        layout_new_user.addWidget(button_sign_up)

        # Vertical main layout
        layout_main = QVBoxLayout()
        layout_main.addWidget(label_login)
        layout_main.addStretch()
        layout_main.addLayout(layout_username)
        layout_main.addStretch()
        layout_main.addLayout(layout_password)
        layout_main.addStretch()
        layout_main.addWidget(button_login)
        layout_main.addStretch()
        layout_main.addLayout(layout_new_user)

        self.setLayout(layout_main)

    def userVerification(self):
        users = {}
        file = "files/users.txt"

        try:
            with open(file, 'r') as f:
                for line in f:
                    user_info = line.split(" ")
                    username_info = user_info[0]
                    password_info = user_info[1].strip('\n')
                    users[username_info] = password_info

            username = self.edit_username.text()
            password = self.edit_password.text()

            if (username, password) in users.items():
                QMessageBox.information(self, "Success!",
                                        "<b><green>Login Successful!</green></b>",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.login_is_successful = True
                self.close()
                self.openApplicationWindow()
            else:
                QMessageBox.warning(self, "Error Message",
                                    "The username or password is incorrect.",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error",
                                f"""<p>File not found.</p>
<p>Error: {error}</p>""",
                                QMessageBox.StandardButton.Ok)
            f = open(file, "w")
    def showPassword(self, checked):
        if checked:
            self.edit_password.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

    def createNewUser(self):
        self.create_new_user_window = NewUserDialog()
        self.create_new_user_window.show()
    def openApplicationWindow(self):
        # self.main_window = MainWindow()
        self.main_window.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())