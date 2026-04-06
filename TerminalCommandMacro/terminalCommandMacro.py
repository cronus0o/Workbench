# Terminal Command auto-save Macro Program

import os          # Interact with file system
import subprocess  # Run terminal commands and capture output
import hashlib     # Create hash of command+output for deduplication
from initializeKey import initPath, initExit

# Directory to store command history markdown files
logDir = os.path.expanduser("~/Obsidian_Vault/Linux/LinuxCommands/")
os.makedirs(logDir, exist_ok=True)

# Exit command to leave the macro and return to shell
exitCommand = "exit"

def get_log_filepath(command):
    base_name = command.strip().split()[0].replace("/", "_")
    return os.path.join(logDir, f"{base_name}.md")

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

print(f"\n Terminal Macro Logger Started (insert '{exitCommand}' to quit)")
print(f" Terminal Command History will store in '{logDir}'")
print(f"\n **insert 'initPath' to initialize Path history stored**")
print(f" **insert 'initExit' to initialize Exit Key**\n")

while True: # Main Loop
    try:
        command = input("$ ").strip()
        if command == "":
            continue
        if command == exitCommand:
            print("\n Exiting macro logger. Returning to your shell.\n")
            break

        command_hash = hashlib.md5(command.encode()).hexdigest()
        file_path = get_log_filepath(command)
        hash_path = os.path.join(logDir, 'hash.md')

        output = run_command(command)
        print(output)

        if os.path.exists(file_path):
            with open('hash.md', 'a+', encoding = 'utf-8') as f:
                f.seek(0)
                content = f.read()
                if command_hash not in content:
                    f.write(command_hash + '\n')
                    with open(file_path, 'a', encoding = 'utf-8') as f:
                        f.write(f"Command : {command}\nExecution : {output}\n\n")
        else:
            with open('hash.md', 'a', encoding = 'utf-8') as f:
                f.write(command_hash + '\n')
            with open(file_path, 'w', encoding = 'utf-8') as f:
                f.write(f"$ {command}\n{output}\n\n") 
    except (KeyboardInterrupt, EOFError):
        print("\n Exiting macro logger. Returning to your shell.\n")
        break

