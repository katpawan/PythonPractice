import tkinter as tk


def doNothing():
    print('Do Nothing!!')

# **** Main Menu ******


root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)

fileMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=doNothing)
fileMenu.add_command(label="Open", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=doNothing)

editMenu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# *** Toolbar ****


toolbar = tk.Frame(root, bg="Blue")
insertButton = tk.Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=tk.LEFT, padx=2, pady=2)
printButton = tk.Button(toolbar, text="print", command=doNothing)
printButton.pack(side=tk.LEFT, padx=2, pady=2)

toolbar.pack(side=tk.TOP, fill=tk.X)

# ******** Status Bar***********
status = tk.Label(root, text="Preparing to do Nothing!!", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)
root.mainloop()
