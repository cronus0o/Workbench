# Main Window Screen

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from virtual_shell import VirtualShell
from help_screen import HelpScreen
from cli_screen import CLIScreen
from gui_screen import GUIScreen
from chatbot_screen import ChatbotScreen


class MainWindow(QMainWindow) :
    def __init__(self, user_name) :
        super().__init__()
        self.user_name = user_name
        vsh = VirtualShell(self.user_name)
        vsh.basicDirectory()
        
        self.setWindowTitle(f"Welcome {self.user_name}!") 
        self.resize(1000, 650)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QHBoxLayout()
        main_widget.setLayout(layout)

        # Sidebar
        self.sidebar = QVBoxLayout()
        self.sidebar.setSpacing(10)
        layout.addLayout(self.sidebar, 1)

        # Screen Area
        self.stack = QStackedWidget()
        layout.addWidget(self.stack, 5)

        # Screens
        self.help_screen = HelpScreen()
        self.cli_screen = CLIScreen(user_name)
        self.gui_screen = GUIScreen(user_name)
        self.chatbot_screen = ChatbotScreen(user_name)

        self.stack.addWidget(self.help_screen)
        self.stack.addWidget(self.cli_screen)
        self.stack.addWidget(self.gui_screen)
        self.stack.addWidget(self.chatbot_screen)

        # Buttons
        self.add_sidebar_button("Help", 0)
        self.add_sidebar_button("CLI", 1)
        self.add_sidebar_button("GUI", 2)
        self.add_sidebar_button("Chatbot", 3)

    def add_sidebar_button(self, name, index) :
        button = QPushButton(name)
        button.clicked.connect(lambda: self.stack.setCurrentIndex(index))
        self.sidebar.addWidget(button)

# Testing Line
if __name__ == "__main__" :
    user_name = "admin"
    app = QApplication(sys.argv)
    window = MainWindow(user_name)
    window.show()
    sys.exit(app.exec_())
