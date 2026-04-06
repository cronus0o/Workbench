## Terminal Command auto-save Macro Program

This project creates a Python macro that logs your terminal commands and their outputs into organized `.md` files.

많은 리눅스 초보자들은 정말 간단한 command 조차 어떻게 사용하는지 잘 모르고, 조금만 명령어가 복잡해지면 이해를 포기한다. 결과적으로는 누군가 작성해놓은 명령어를 복사 & 붙여넣기만 하게 되며, 이 과정에서 자신이 어떤 명령어를 실행했는지, 결과가 어떻게 나왔는지 기억하지 못한다. 이렇게 오랜 기간 OS를 사용하게 되면, 시스템에 문제가 생길 수 있으며, 결과적으로 리눅스 실력이 늘지 않는다. 
따라서 나는 자신이 실행한 리눅스 커맨드가 무엇인지, 그 결과는 무엇인지, 또한 왜 그런 커맨드를 입력했는지 이해하고, 기억할 수 있도록 프로그램을 작성한다.

유저가 선택한 방식에 따라 분류될 수 있도록 여러 가지 기능을 추가
(ls -al 에서 ls 와 같이 각 커맨드의 중심이 되는 명령어를 중심으로 하는 파일 생성)
(전체 로그 파일 생성)

---

## 📦 Features

- ✅ Logs each executed command in your terminal.
- ✅ Automatically creates a new `{command}.md` file if it doesn't exist.
- ✅ Appends only **unique** command+output entries (prevents duplication).
- ✅ Captures the output of the command (except in long/interactive cases).
- ✅ Includes a toggle to **enable or disable** logging with a simple shell function.

---

## 📁 Folder Structure
main.py
input.py
hash.md
output.py

~/user/appointed/directory/
~/Obsidian_Vault/Linux/LinuxCommands/
├── ls.md
├── grep.md
├── git.md
└── ...

Each file stores history of that specific command.

---

## Operate Process

`Main Program Execute` -> `Another Shell` -> `User Input` -> `Store Input`
-> `Hand Over to Shell` -> `Run command in Shell` -> `Store Result`

1. Start the main program
2. Create a new shell (using pexpect, pywinpty, etc.)
import pexpect
shell = pexpect.spawn('/bin/bash', encoding='utf-8')

3. Wait for user input
4. Parse and store the input
5. Pass the command to the shell (e.g., bash)
6. Execute the command
7. Parse and store the result
8. Return to step 2

---

## 🧠 Required Python Modules

import os          # Interact with file system
import subprocess  # Run terminal commands and capture output
import hashlib     # Create hash of command+output for deduplication

---

## Optimization

modulization with GUI option

**Caution** Initialize function
make 'initialize path to restore' function
with 'initPath' command 
(add this particular command in while True paragraph)
newPath = input('Write Your New Path : ')
setDir = os.path.expanduser(newPath)
os.makedirs(setDir, exist_ok=True)

make 'initialize exit command' functioin
with 'initExit' command
newExit = input('Write Your New Exit Command : ')
exitCommand = newExit 

---

