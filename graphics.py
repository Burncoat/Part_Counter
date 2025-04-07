from tkinter import *
from tkinter import ttk
from greatswords import *

import sv_ttk

class PartCounter:
    def __init__(self, root):
        root.title("MonHun: Wilds Part Counter")
        content = ttk.Frame(root, padding=(3, 3, 12, 12))
        weaponname = StringVar()
        name = ttk.Entry(content, textvariable=weaponname)
        namelabel = ttk.Label(content, text="Weapon Name")

        gsvar = StringVar(value=gs_names)
        weaponlst = Listbox(content, listvariable=gsvar, borderwidth=3, relief="solid", width=20, height=40)
        selectlst = ttk.Frame(content, borderwidth=10, relief="groove", width=300, height=400)

        content.grid(column=0, row=0, sticky=(N, S, E, W))
        weaponlst.grid(column=0, row=1, columnspan=2, rowspan=2, sticky=(W), padx=10, pady=10)
        selectlst.grid(column=3, row=1, columnspan=2, rowspan=1, sticky=(E,W), padx=10)
        namelabel.grid(column=0, row=0, sticky=(N,W,S,E), padx=5, pady=5)
        name.grid(column=1, row=0, columnspan=2, sticky=(N,E,W,S), padx=5, pady=5)











root = Tk()
PartCounter(root)
root.mainloop()