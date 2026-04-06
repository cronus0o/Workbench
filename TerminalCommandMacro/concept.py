## Frame of Program

# Start the main program
# Create a new shell (using pexpect, pywinpty, etc.)
# Wait for user input
# Parse and store the input
# Pass the command to the shell (e.g., bash)
# Execute the command
# Parse and store the result
# Return to step 2


# import pexpect

# # 1. Start the main program
# def main():
#     return

# # 2. Create a new shell (using pexpect, pywinpty, etc.)
# shell = pexpect.spawn('/bin/bash', encoding='utf-8')

# # 3. Wait for user input
# user_input = input(">> ")

# # 4. Parse and store the input
# command_history.append(user_input)

# # 5. Pass the command to the shell (e.g., bash)
# shell.sendline(user_input)

# # 6. Execute the command
# shell.expect('\n', timeout=5)  # 줄 바꿈이나 프롬프트까지 대기

# # 7. Parse and store the result
# output = shell.before.strip()
# output_log.append(output)

# # 8. Return to step 2
# while True:
#     user_input = input(">> ")
#     if user_input in ('exit', 'quit'):
#         break

# -------------------------------------------------------------------------------------------
# Real Program Looks Like

import pexpect

def initializeSetting():
    return

def examinInput(user_input=""):
    user_input

def examinOutput(output=""):
    output

initializeSetting()
# /bin/bash, /usr/bin/zsh
shell = pexpect.spawn('/bin/bash', encoding='utf-8')
shell.sendline('export PS1="PEXPECT_PROMPT> "')
shell.expect('PEXPECT_PROMPT> ')

while True: 
    user_input = input("This is Python Input>> ")
    # print(user_input)
    if user_input in ('exit', 'quit'):
        break

    # examinInput(user_input)

    shell.sendline(user_input)
    shell.expect('PEXPECT_PROMPT> ')

    output = shell.before.strip()
    output_lines = output.splitlines()
    # examinOutput(output)
    if output_lines and output_lines[0] == user_input:
        output_lines = output_lines[1:]

    result_output = '\n'.join(output_lines)
    print(result_output)