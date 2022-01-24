import subprocess
import tkinter.messagebox
from tkinter import *

# ================= top level functions ================= #

def run (cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def psGetCred(user, password):
    payload = (f"$psCred = New-Object System.Management.Automation.PSCredential -ArgumentList (\"{user}\", \"{password}\")")
    buffer = run(payload)
    if buffer.returncode != 0:
        print("Error: %s",buffer.stderr)
    else:
        print("Payload successful")
        out = run("Write-Host $psCred -OutBuffer 0")
        print(out)

# if __name__ == '__main__':
#     hello_command = "Write-Host 'Hello World!'"
#     hello_info = run(hello_command)
#     if hello_info.returncode != 0:
#         print("An error occured: %s", hello_info.stderr)
#     else:
#         print("Hello command executed successfully!")
    
#     print("-------------------------")
    
#     bad_syntax_command = "Write-Hst 'Incorrect syntax command!'"
#     bad_syntax_info = run(bad_syntax_command)
#     if bad_syntax_info.returncode != 0:
#         print("An error occured: %s", bad_syntax_info.stderr)
#     else:
#         print("Bad syntax command executed successfully!")

# ================== initial stuff ====================== #
version = "0.1.0"
win = Tk()
win.title(f"CAPH Tool {version}")
win.geometry('500x200')

def loginFunction():
    cred1 = inputUserLogin.get()
    cred2 = inputUserPassword.get()
    psGetCred(cred1, cred2)



labelInputUserLogin = Label(win, text="AD Username").grid(row=0)
labelInputUserPassword = Label(win, text="Password").grid(row=1)

inputUserLogin = Entry(win)
inputUserPassword = Entry(win, show="*")

inputUserLogin.grid(row=0, column=1)
inputUserPassword.grid(row=1, column=1)

buttonLogin = Button(win, text="Log in", command=loginFunction)
# buttonQuit = Button(win, text="Quit", width=10, height=5, command=exit)

buttonLogin.grid(row=2)

win.mainloop()
