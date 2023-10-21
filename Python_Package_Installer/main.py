from os import system
from sys import exit
from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

w = Tk()
w.title('Python Package installer for windows V1.0')
w.geometry('+100+100')
w.resizable(False, False)
Sc = Scrollbar(w)
Sc.pack(side=RIGHT, fill=Y)
F = Frame(w)
F.pack(side=TOP)
L = Label(F, text='Package:', font=("Cascadia Code SemiBold", 10))
L.grid(row=0, column=0)
Lb = Label(F, text='Download source:', font=("Cascadia Code SemiBold", 10))
Lb.grid(row=0, column=2)
Ld = Label(F, text=strftime('%H:%M:%S'), font=("Cascadia Code SemiBold", 10))
Ld.grid(row=1, column=1)
E = Entry(F, font=("Cascadia Code SemiBold", 10))
Eb = ttk.Combobox(F, font=("Cascadia Code SemiBold", 10))
Eb.grid(row=0, column=3)
Eb['value'] = ("https://pypi.org/simple",
               "https://pypi.tuna.tsinghua.edu.cn/simple",
               "https://mirrors.aliyun.com/pypi/simple/",
               "http://pypi.douban.com/simple/",
               "https://pypi.mirrors.ustc.edu.cn/simple/",
               "http://pypi.hustunique.com/simple/",
               "https://mirror.sjtu.edu.cn/pypi/web/simple/")
Eb.set("https://pypi.org/simple") 
E.grid(row=0, column=1)
T = Text(w, height=30, width=85, yscrollcommand=Sc.set)
T.pack(side=LEFT)
T.tag_config('S', foreground='green', font=("Cascadia Code SemiBold", 12))
T.tag_config('F', foreground='red', font=("Cascadia Code SemiBold", 12))
T.config(state=DISABLED)


def call(cmd):
    return(system(cmd))


def install():
    name = str(E.get())
    if name == "":
        messagebox.showinfo("INFO", "You must give at least one requirement to install.")
        return
    oth = str(Eb.get())
    cmd = str('pip install' + ' ' + name + ' ' + '--trusted-host ' + oth)
    msg = call(cmd)
    if msg == 0:
        T.config(state=NORMAL)
        T.insert(INSERT, ('<{0}>Install package "{1}" successfully.\n'.format(strftime('%H:%M:%S'), name)), 'S')
        T.config(state=DISABLED)
    else:
        T.config(state=NORMAL)
        T.insert(INSERT, ('<{0}>Install package "{1}" failedly.\n'.format(strftime('%H:%M:%S'), name)), 'F')
        T.config(state=DISABLED)


def show_time():
    Ld.config(text=strftime('%H:%M:%S'))
    Ld.after(1000, show_time)


def upgrade_pip():
    oth = str(Eb.get())
    cmd = str('python -m pip install --upgrade pip {0}'.format('--trusted-host ' + oth))
    print(cmd)
    msg = call(cmd)
    if msg == 0:
        T.config(state=NORMAL)
        T.insert(INSERT, '<{0}>Upgrade pip successfully.\n'.format(strftime('%H:%M:%S')), 'S')
        T.config(state=DISABLED)
    else:
        T.config(state=NORMAL)
        T.insert(INSERT, '<{0}>Upgrade pip failedly.\n'.format(strftime('%H:%M:%S')), 'F')
        T.config(state=DISABLED)


def Exit(event):
    if event.keycode == 27:
        exit(0)

def Clear():
    T.config(state=NORMAL)
    T.delete("1.0", "end")
    T.config(state=DISABLED)


B = Button(F, text='Install', command=install, width=11, font=("Cascadia Code SemiBold", 10))
B.grid(row=1, column=0)
Bb = Button(F, text='Clear', command=Clear, width=11, font=("Cascadia Code SemiBold", 10))
Bb.grid(row=1, column=3)
Bc = Button(F, text='Upgrade pip', command=upgrade_pip, width=11, font=("Cascadia Code SemiBold", 10))
Bc.grid(row=1, column=2)
Sc.config(command=T.yview)
show_time()
w.bind('<Key>', Exit)
w.mainloop()
