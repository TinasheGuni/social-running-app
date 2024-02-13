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
        self.setFixedSize(360, 320)
        self.setWindowTitle("New Account")
        self.setUpWindow()

    def setUpWindow(self):
        label_login = QLabel("Create New Account", self)
        label_login.setFont(QFont("Arial", 20))
        label_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Main Layout
        layout_main = QVBoxLayout()
        layout_main.addWidget(label_login)
        layout_main.addStretch()

        self.setLayout(layout_main)