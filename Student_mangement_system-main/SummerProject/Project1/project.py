from tkinter import *
from tkinter import ttk
import time

class Student:
    def __init__(self,root):
       self.root =root
       self.root.geometry("1400x800+10+10")
       self.root.title("RDJ Student Management")
    #  self.root.config(bg="white")
 
    #  self.root.resizable(FALSE,FALSE)
if __name__ == "__main__":
    root = Tk()
    obj =Student(root)
    root.mainloop()