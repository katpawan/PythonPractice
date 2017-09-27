import tkinter as tk
import tkinter.messagebox


root = tk.Tk()

tk.messagebox.showinfo('Window Title', 'Text to display')
answer = tkinter.messagebox.askquestion('Question', 'Do you like it!')
if(answer == "yes"):
    print("yes")
else:
    print("no")
root.mainloop()
