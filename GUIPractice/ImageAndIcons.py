import tkinter as tk


root = tk.Tk()

photo = tk.PhotoImage(file="me.png")
label = tk.Label(root, image=photo)
label.pack()
root.mainloop()
