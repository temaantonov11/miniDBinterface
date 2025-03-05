import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                             QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtCore import Qt

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)
        
        central_widget = QWidget()
        
        self.setCentralWidget(central_widget)
       
        main_layout = QVBoxLayout(central_widget)

        
        central_widget.setStyleSheet("""
            QWidget {
                padding: 0px;
                margin: 0px;
            }
            QLabel {
                padding: 0px;
                margin: 0px;
                font-size: 15px;
            }
            QLineEdit {
                font-size: 16px;
                padding: 5px;
                margin: 0px;
            }
        """)

        info_title = QLabel("Input user data and choose role")
        info_title.setStyleSheet("font-size: 20px;")

        self.username_field = QLineEdit(self)
        self.password_field = QLineEdit(self)

        self.admin_option = QRadioButton("Admin")
        self.guest_option = QRadioButton("Guest")

        self.login_option = QRadioButton("log in")
        self.registry_option = QRadioButton("sign up")

        self.start_button = QPushButton("Start")

        self.role_group = QButtonGroup()
        self.role_group.addButton(self.admin_option, 1)
        self.role_group.addButton(self.guest_option, 2)

        self.init_group = QButtonGroup()
        self.init_group.addButton(self.login_option, 1)
        self.init_group.addButton(self.registry_option, 2)

        info_layout = QHBoxLayout()
        
        role_layout = QHBoxLayout()
        role_layout.setSpacing(0)
        role_layout.setContentsMargins(0, 0, 0, 0)

        auth_layout = QVBoxLayout()
        auth_layout.setSpacing(0)
        auth_layout.setContentsMargins(0, 0, 0, 0)

        init_layout = QHBoxLayout()
        init_layout.setSpacing(0)
        init_layout.setContentsMargins(0, 0, 0, 0)

        info_layout.addWidget(info_title)

        auth_layout.addWidget(QLabel('Username: '))
        auth_layout.addWidget(self.username_field)
        auth_layout.addWidget(QLabel('Password: '))
        auth_layout.addWidget(self.password_field)

        role_layout.addWidget(self.admin_option)
        role_layout.addWidget(self.guest_option)        
        
        init_layout.addWidget(self.login_option)
        init_layout.addWidget(self.registry_option)

        main_layout.addLayout(info_layout)
        main_layout.addLayout(auth_layout)
        main_layout.addLayout(role_layout)
        main_layout.addLayout(init_layout)
        main_layout.addWidget(self.start_button)

        info_layout.addStretch(1)
        auth_layout.addStretch(1)
        role_layout.addStretch(1)
        init_layout.addStretch(1)
        main_layout.addStretch(1)
        
        
    
        


        
