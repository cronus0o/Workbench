# Side bar ChatbotScreen

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit

chatbot_list = {
    "hi": "Hello! How can I help you with Linux?",
    "hello": "Hi there! Ask me anything about Linux or shell commands.",
    "what is linux": "Linux is an open-source operating system kernel used in many systems.",
    "what is shell": "A shell is a command-line interface to interact with the operating system.",
    "what is terminal": "Terminal is a program that opens a shell where you can type commands.",
    "what is file system": "A file system organizes data and defines how files are stored and retrieved.",
    "what is /": "‘/’ is the root directory in Linux – the top of the file system hierarchy.",
    "what is /home": "/home contains users’ personal directories and data.",
    "what is /etc": "/etc holds system-wide configuration files.",
    "what is /bin": "/bin contains essential user binaries (programs).",
    "what is /usr": "/usr holds user-installed software and libraries.",
    "what is /var": "/var contains variable data like logs and databases.",
    "what is /tmp": "/tmp is for temporary files, deleted after reboot.",
    "what is man": "`man` shows the manual page for commands, like `man ls`.",
    "how to use man": "Just type `man command`, e.g., `man mv`.",
    "what is pwd": "`pwd` stands for 'print working directory' – it shows your current location.",
    "how to use pwd": "Just type `pwd` to see your current directory path.",
    "what is ls": "`ls` lists files and directories in the current location.",
    "how to use ls": "`ls` shows files. Add options like `-l` for details or `-a` for hidden files.",
    "what is cd": "`cd` is used to change directories.",
    "how to use cd": "`cd directory_name` moves into that directory. Use `cd ..` to go up one level.",
    "what is mkdir": "`mkdir` creates a new directory.",
    "how to use mkdir": "Type `mkdir new_folder` to make a new directory.",
    "what is rm": "`rm` removes files or directories.",
    "how to use rm": "`rm filename` deletes a file. Use `rm -r foldername` for directories.",
    "what is mv": "`mv` moves or renames files and directories.",
    "how to use mv": "`mv source destination` moves or renames items.",
    "how to go back": "Use `cd ..` to go up one directory.",
    "what is a hidden file": "Files starting with `.` are hidden in Linux.",
    "how to see hidden files": "Use `ls -a` to list all files including hidden ones.",
    "what is absolute path": "Absolute paths start from `/`, like `/home/user/docs`.",
    "what is relative path": "Relative paths are based on your current location.",
    "difference between / and ~/": "`/` is root. `~/` is your home directory.",
    "what is sudo": "`sudo` lets you run commands as a superuser (admin).",
    "how to clear terminal": "Use `clear` or `Ctrl+L` to clear the screen.",
    "what is touch": "`touch` creates an empty file, e.g., `touch file.txt`.",
    "what is echo": "`echo` prints text to the terminal, like `echo Hello`.",
    "how to create file": "Use `touch filename` or `echo 'text' > filename`.",
    "how to remove folder": "`rm -r foldername` deletes a folder recursively.",
    "how to copy files": "Use `cp source destination` to copy files.",
    "how to move files": "`mv old new` moves or renames files.",
    "what is chmod": "`chmod` changes file permissions.",
    "what is chown": "`chown` changes file ownership.",
    "how to list permissions": "Use `ls -l` to view file permissions.",
    "what is bash": "Bash is a popular shell used to run commands and scripts.",
    "how to write script": "Write commands in a `.sh` file and run with `bash script.sh`.",
    "how to run script": "Make it executable with `chmod +x script.sh`, then run `./script.sh`.",
    "what is shebang": "`#!/bin/bash` at the top of a script tells which shell to use.",
    "how to see processes": "Use `ps` or `top` to see running processes.",
    "how to stop program": "Use `Ctrl+C` to stop foreground programs, or `kill PID` for background ones.",
    "bye": "Goodbye! See you again!",
}

class MyChatbot :
    def __init__(self) :
        self.memory = []
        self.context = {}

    def receive_input(self, user_input) :
        context = user_input.strip().lower()
        self.memory.append(context)
        for keyword in chatbot_list:
            if keyword in context and keyword != "":
                return chatbot_list[keyword]

        return "I’m not sure what you mean. Can you try rephrasing?"

class ChatbotScreen(QWidget) :
    def __init__(self, user_name) :
        super().__init__()
        self.user_name = user_name
        self.chat = MyChatbot()

        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.input = QLineEdit()
        self.input.setPlaceholderText("Talk To Your Chatbot!...")

        layout.addWidget(self.output)
        layout.addWidget(self.input)
        self.setLayout(layout)

        self.input.returnPressed.connect(self.respond)

    def respond(self) :
        cmd_line = self.input.text()
        self.input.clear()
        if not cmd_line :
            return
        self.output.append(f"{self.user_name} : {cmd_line}")
        response = self.chat.receive_input(cmd_line)
        self.output.append(f"Chatbot : {response}")
    

if __name__ == "__main__" :
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = ChatbotScreen("testest")
    window.show()
    print(window.input.text())
    sys.exit(app.exec_())

