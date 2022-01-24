import subprocess
import tkinter.messagebox
from tkinter import *

# ================= top level functions ================= #

def run (cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

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
win.title('CAPH Tool')
# win.geometry('500x200')

def startupBlurb():
    tkinter.messagebox.showinfo(f"Welcome to version {version} of the Compiled and Performant Helpdesk tool")

labelInputUserLogin = Label(win, text="AD Username").pack()#.grid(row=0)
labelInputUserPassword = Label(win, text="Password").pack()#.grid(row=1)

inputUserLogin = Entry(win)
inputUserPassword = Entry(win)

inputUserLogin.pack()#.grid(row=0, column=1)
inputUserPassword.pack()#.grid(row=1, column=1)

buttonLogin = Button(win, text="Log in", command=startupBlurb)
# buttonQuit = Button(win, text="Quit", width=10, height=5, command=exit)

buttonLogin.pack()#.grid(row=2)


win.mainloop()
