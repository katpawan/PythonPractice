import tkinter as tk
import tkinter.messagebox as tm

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()
blackline = canvas.create_line(0, 0, 200, 50)
redline = canvas.create_line(0, 100, 200, 50, fill="red")
green_box = canvas.create_rectangle(25, 25, 130, 60, fill="green")

answer = tm.askquestion('Question', 'Do you want to delete red line?')
if(answer == "yes"):
    canvas.delete(redline)
    tm.showinfo("Choice", "You opted to delete the red line")
else:
    tm.showinfo("Choice", "You opted not to delete the red line")
root.mainloop()
