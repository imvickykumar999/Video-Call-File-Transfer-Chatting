import os

try:
    os.mkdir('chat/chat')
except Exception as e:
    print('error in mkdir chat')
    print(e)

try:
    os.mkdir('files/files')
except Exception as e:
    print('error in mkdir files')
    print(e)

# --------------------------------------------

# from tkinter import *
#
# win = Tk()
#
# def serverbtn():
#     import files.fileserver as fs
#     fs.fserver()
#
# def clientbtn():
#     import files.fileclient as fc
#     fc.fclient()
#
# button1 =  Button(win, text="Click Me To serverbtn", command=serverbtn)
# button2 =  Button(win, text="Click Me To clientbtn", command=clientbtn)
#
# # -------------------------------------------
#
# import threading
#
# t1 = threading.Thread(target=button1.pack())
# t2 = threading.Thread(target=button2.pack())
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# # --------------------------------------------
#
# # button1.pack()
# # button2.pack()
#
# win.mainloop()
#
# # input()
#
# # os.system('pip install requirements.txt')
