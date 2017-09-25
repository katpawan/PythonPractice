import tkinter as tk


class MyClass:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        button1 = tk.Button(frame, text="Print Button", command=self.PrintMessage)
        button1.pack(side=tk.LEFT)
        button2 = tk.Button(frame, text="QUIT", command=frame.quit)
        button2.pack(side=tk.LEFT)

    def PrintMessage(self):
        print('In PrintMessage function')


root = tk.Tk()
b = MyClass(root)
root.mainloop()
