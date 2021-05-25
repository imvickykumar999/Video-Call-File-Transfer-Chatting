import os

try:
    os.mkdir('chat/chat')
except Exception as e:
    pass
    # print(e)

try:
    os.mkdir('files/files')
except Exception as e:
    pass
    # print(e)

# --------------------------------------------

from tkinter import *

win = Tk()

def serverbtn():
    import files.fileserver as fs
    fs.fserver()

def clientbtn():
    import files.fileclient as fc
    fc.fclient()

button1 =  Button(win, text="Receive Files", command=serverbtn)
button2 =  Button(win, text="Send Files", command=clientbtn)

# button1.pack()
# button2.pack()

button1.place(relx=0.5, rely=0.3, anchor=CENTER)
button2.place(relx=0.5, rely=0.7, anchor=CENTER)

win.mainloop()

# -----------------------------------------------

# # input()
#
# # os.system('pip install requirements.txt')
