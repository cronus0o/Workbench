# Side bar CLIScreen


from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit
from virtual_shell import VirtualShell

class CLIScreen(QWidget) :
    def __init__(self, user_name) :
        super().__init__()
        self.user_name = user_name
        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter command here...")

        layout.addWidget(self.output)
        layout.addWidget(self.input)
        self.setLayout(layout)

        self.vshell = VirtualShell(self.user_name)
        self.input.returnPressed.connect(self.execute_command)

    def execute_command(self) :
        cmd_line = self.input.text().strip()
        self.input.clear()
        if not cmd_line:
            return

        self.output.append(f">{self.user_name}@{self.user_name}device$ {cmd_line}")

        tokens = cmd_line.split()
        cmd = tokens[0]
        args = tokens[1:]

        def execute_man(args) :
            if not args :
                return "Available commands: pwd, cd, ls, man, mkdir, mv, rm, exit"
            manual = {
                "pwd" : "pwd: Print the current working directory.",
                "cd" : "cd <dir>: Change the current directory.",
                "ls" : "ls [dir]: List directory contents.",
                "man" : "man [cmd]: Show the manual of the command.",
                "mkdir" : "mkdir <dir>: Create a new directory.",
                "mv" : "mv <src> <dst>: Move or rename files/directories.",
                "rm" : "rm <file/dir>: Remove files or directories.",
                "exit" : "exit: Exit the shell.",
            }
            return manual.get(args[0], f"man: no manual entry for {args[0]}")

        command_functions = {
            "pwd" : lambda args : self.vshell.pwd(),
            "cd" : lambda args : self.vshell.cd(args[0]) if args else "cd: missing operand",
            "ls" : lambda args : self.vshell.ls(args[0]) if args else self.vshell.ls(),
            "mkdir" : lambda args : self.vshell.mkdir(args[0]) if args else "mkdir: missing operand",
            "mv" : lambda args : self.vshell.mv(args[0], args[1]) if len(args) >= 2 else "mv: missing file operand",
            "rm" : lambda args : self.vshell.rm(args[0]) if args else "rm: missing operand",
            "man" : execute_man,
            "exit" : lambda args : "exit",
        }

        func = command_functions.get(cmd)
        if func :
            result = func(args)
            if result == "exit" :
                self.output.append("Exiting shell.")
                # 윈도우 닫기나 앱 종료 로직 필요 시 여기서 처리
                return
            elif result is not None :
                # VirtualShell 메서드가 print 대신 문자열 반환한다면 여기에 출력
                self.output.append(str(result))
                self.output.append("")
        else :
            self.output.append(f"{cmd}: command not found")


if __name__ == "__main__" :
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = CLIScreen("testest")
    window.show()
    print(window.input.text())
    sys.exit(app.exec_())