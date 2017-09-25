import tkinter as tk
root = tk.Tk()
# theLabel = tk.Label(root, text='I am label!')
# theLabel.pack()

# topFrame = tk.Frame(root)
# topFrame.pack()
# bottomFrame = tk.Frame(root)
# bottomFrame.pack(side=tk.BOTTOM)

# button1 = tk.Button(topFrame, text="Button1", fg="red")
# button2 = tk.Button(topFrame, text="Button2", fg="green")
# button3 = tk.Button(topFrame, text="Button3", fg="blue")
# button4 = tk.Button(bottomFrame, text="Button4", fg="purple")

# button1.pack(side=tk.LEFT)
# button2.pack(side=tk.LEFT)
# button3.pack(side=tk.LEFT)
# button4.pack(side=tk.BOTTOM)

# label1 = tk.Label(root, text='label1', fg='red', bg='white')
# label1.pack()
# label2 = tk.Label(root, text='label2', fg='green', bg='yellow')
# label2.pack(fill=tk.X)
# label3 = tk.Label(root, text='label3', fg='blue', bg='pink')
# label3.pack(side =tk.LEFT, fill=tk.Y)

# label1 = tk.Label(root, text='NAME')
# label2 = tk.Label(root, text='PASSWORD')
# entry_1 = tk.Entry(root)
# entry_2 = tk.Entry(root, show="*")
# label1.grid(row=0, sticky=tk.E)
# label2.grid(row=1)
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
# c = tk.Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)


def Left(event):
    print('Left')


def Right(event):
    print('Right')


frame = tk.Frame(root, width=300, height=250)
frame.bind("<Button-1>", Left)
frame.bind("<Button-3>", Right)
# button1 = tk.Button(root, text='PressMe')
# button1.bind("<Button-1>", printName)
# button1.pack()
frame.pack()
root.mainloop()
