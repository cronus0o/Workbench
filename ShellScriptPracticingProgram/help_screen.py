# SIde bar help screen

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit

information = """
Q : What is this program?
A : This is a Linux practice tool designed to help you learn and explore the fundamentals of the Linux operating system, especially terminal scripting using shells like Bash and Zsh.
    It provides an interactive learning environment where you can build practical skills through hands-on exercises. Linux is a powerful, open-source operating system that serves as the foundation for many computing systems around the world, including servers, cloud platforms, and embedded devices.

Q : Why should I learn about Linux?
A : While most personal computers run Windows or macOS, the majority of the world's servers, cloud services, supercomputers, and developer tools run on Linux.
    Learning Linux gives you direct access to the core of computing systems and is an essential skill for software developers, system administrators, and computer science students.
    If you want to truly understand how computers work — beyond graphical user interfaces — Linux is the right place to start.

Q : What is a shell script?
A : A shell script is a series of commands written for the shell — the command-line interface that connects the user and the operating system kernel.
    Instead of typing commands one by one, you can automate them using a script. Shell scripts are powerful tools for automating tasks, managing files, executing logic, and interacting with system-level tools efficiently.

Q : Why should I learn shell scripting?
A : Shell scripting greatly enhances your ability to control, automate, and customize your computing environment.
    Whether you're automating repetitive tasks, managing large server systems, configuring environments, or building simple utilities, scripting gives you superpowers at the terminal. It is also widely used in DevOps, cloud operations, CI/CD pipelines, and system monitoring.

Q : What will I learn in this program?
A : By the end of this program, you will be able to:
    Navigate the Linux file system using terminal commands
    Write and execute shell scripts using Bash and Zsh
    Understand and apply key concepts like variables, conditionals, loops, and functions
    Automate file operations, scheduling, and system tasks
    Use powerful tools like grep, sed, awk, and cron
    This program starts from the basics and gradually builds your skills toward becoming confident in the Linux environment.

Q : Who is this program for?
A : This program is ideal for:
    Complete beginners who want to learn Linux
    Students interested in systems programming or computer science
    Developers who want to improve command-line productivity
    Aspiring DevOps engineers or system administrators
    Anyone curious about how computers really work under the hood

Q : What kind of exercises are included?
A : You will find interactive exercises and real-world examples such as:
    Creating, editing, and organizing files via terminal
    Writing backup scripts and automation tools
    Managing users, processes, and permissions
    Scheduling tasks with cron
    Parsing and processing text with command-line utilities

Q : What will I achieve after completing this program?
A : After completing this program, you’ll be equipped with essential Linux and shell scripting skills. 
    You’ll understand how to interact with the system at a low level, write your own scripts, and think like a Linux power user.
    This is the first step on your journey to becoming a Linux expert — or even a future DevOps engineer.

Start your Linux journey today, and unlock the full power of the terminal! 💻
"""

class HelpScreen(QWidget) :
    def __init__(self) :
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Help Information"))
        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setText(information)
        layout.addWidget(self.text)
        self.setLayout(layout)

if __name__ == "__main__" :
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = HelpScreen()
    window.show()
    sys.exit(app.exec_())