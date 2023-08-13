from tkinter import *
from tkinter import ttk
import time
import mysql.connector 
from tkinter import messagebox

class Student:
 def __init__(self,root):
   self.root =root
   self.root.title("RDJ Student Management")
   self.root.config(bg="white")
   self.root.geometry("1400x800+10+10")
   self.root.resizable(FALSE,FALSE)
    # root.iconbitmap("a.png")

   self.var_dep = StringVar
   self.var_sem = StringVar
   self.var_course = StringVar
   self.var_name = StringVar
   self.var_gender = StringVar
   self.var_year = StringVar
   self.var_roll = StringVar
   self.var_father = StringVar
   self.var_mob = StringVar
   self.var_dob = StringVar






   Label(text="Ram devi Jindal Group Of Institutions",font="arial 35 bold",bg="red",fg="black",padx=20).pack()
   Label(text="Welcome to My Project",font="areal 25 bold",bg="White").pack(padx=35,fill=X)
   Label(text="Ready",bg="orange",borderwidth=2,relief=SOLID).pack(fill=X,side=BOTTOM)

######################################################## Frames

   dataEntryFrame = LabelFrame(text="Student Information",bg="cyan3",borderwidth= 4,relief=SOLID ,font="comicsansms 20 bold",fg="red3")
   dataEntryFrame.place(x=30,y=110,width=700,height=660)

   ShowEntryFrame = LabelFrame(text="Student data",bg="cyan3",borderwidth= 4,relief=SOLID ,font="comicsansms 20 bold",fg="red3")
   ShowEntryFrame.place(x=740,y=110,width=940,height=660)

   ####################################################### Slider


   ################################# Dataentry framne lable
   department_lable = LabelFrame(dataEntryFrame,text="Course",borderwidth=3,relief=SUNKEN,fg="green3",bg="white",font="comicsansms 20 bold")
   department_lable.place(x=10,y=10,width=655,height=120)
   #Lables
   #Department
   l_dpartment = Label(department_lable,text="Department",fg="Black",bg="white",font="arial 15 bold")#variable used
   l_dpartment.grid(row=0,column=0,padx=2,sticky=W)
   combo_department = ttk.Combobox(department_lable,font = ("comicsans",10),width = 17,state="readonly",textvariable=self.var_dep)
   combo_department["value"]=("Select Department","Civil","Mechanical","Computer Science","BMLS","BHMC","BBA")
   combo_department.grid(row = 0,column =1,padx=5,pady=5,sticky=W)

   #Year
   l_year = Label(department_lable,text="Year",fg="Black",bg="white",font="arial 15 bold",)
   l_year.grid(row=0,column=3,padx=10,sticky=W)
   combo_year = ttk.Combobox(department_lable,font ="comicsans 12",width = 15,state="readonly",textvariable=self.var_year)
   combo_year["value"]=("Select Year","1st","2nd","3rd","4th(B.tech/BHMC)")
   combo_year.grid(row = 0,column =4,padx=2,pady=2,sticky=W)

   #semester

   l_semester = Label(department_lable,text="Semester",fg="black",bg="white",font="arial 15 bold")
   l_semester.grid(row=2,column=0,padx=5,pady=5,sticky=W)
   combo_sem =ttk.Combobox(department_lable,font="comicsans 12",width=14,state ="readonly",textvariable=self.var_sem)
   combo_sem["value"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
   combo_sem.grid(row = 2,column =1,padx=5,pady=5,sticky=W)


   ################################# Studdddent info frame
   student_info_lable = LabelFrame(dataEntryFrame,text="Details",borderwidth=3,relief=SUNKEN,fg="green3",bg="white",font="comicsansms 20 bold")
   student_info_lable.place(x=10,y=140,width=655,height=470)

   ####### details lable
   #Name Lable
   name_lable = Label(student_info_lable,text="Name :",bg="white",font="arial 15 bold")
   name_lable.grid(row=0, column=0,sticky=W,padx=10)
   name_entry = ttk.Entry(student_info_lable,font="comicsans 12",width=16,textvariable=self.var_name)
   name_entry.grid(row=0,column=1,sticky=W,padx=9)

   #roll no. Lable
   RollNo_lable = Label(student_info_lable,text="RollNo :",bg="white",font="arial 15 bold")
   RollNo_lable.grid(row=0, column=2,sticky=W,padx=6,pady=20)
   RollNo_entry = ttk.Entry(student_info_lable,font="comicsans 12",width=16,textvariable=self.var_roll)
   RollNo_entry.grid(row=0,column=3,sticky=W,padx=6,pady=20)

   #Gender Lable
   Gender_lable = Label(student_info_lable,text="Gender :",bg="white",font="arial 15 bold")
   Gender_lable.grid(row=1, column=0,sticky=W,padx=6,pady=20)
   Gender_combo = ttk.Combobox(student_info_lable,font="comicsans 12",width=15,textvariable=self.var_gender)
   Gender_combo["value"]=("Select Gender","Male","Female","Other")
   Gender_combo.grid(row=1,column=1,sticky=W,padx=6,pady=20)

#DOB Lable
   dob_lable = Label(student_info_lable,text="DOB :",bg="white",font="arial 15 bold")
   dob_lable.grid(row=1, column=2,sticky=W,padx=10,pady=20)
   dob_entry = ttk.Entry(student_info_lable,font="comicsans 12",width=16,textvariable=self.var_dob)
   dob_entry.grid(row=1,column=3,sticky=W,padx=9,pady=20)

   #Father Name Lable
   Father_name_lable = Label(student_info_lable,text="Father Name :",bg="white",font="arial 15 bold")
   Father_name_lable.grid(row=2, column=0,sticky=W,padx=6,pady=20)
   Father_name_entry = ttk.Entry(student_info_lable,font="comicsans 12",width=16,textvariable=self.var_father)
   Father_name_entry.grid(row=2,column=1,sticky=W,padx=6,pady=20)

   #mob Lable
   mob_lable = Label(student_info_lable,text="Phone. No:",bg="white",font="arial 15 bold")
   mob_lable.grid(row=2, column=2,sticky=W,padx=10,pady=20)
   mob_entry = ttk.Entry(student_info_lable,font="comicsans 12",width=16,textvariable=self.var_mob)
   mob_entry.grid(row=2,column=3,sticky=W,padx=9,pady=20)

   #button Frame

   buttonFrame = Frame(dataEntryFrame,bg="cyan3",borderwidth= 2,relief=GROOVE)
   buttonFrame.place(x=35,y=500,width=600,height=40)

   # save button
   saveButton = Button(buttonFrame,text="save",bg="blue",fg="white",height=1,width=5,command=self.addData)
   saveButton.grid(row=0,column=0,padx=20,pady=3)


   # update button
   updatebutton = Button(buttonFrame,text="update",bg="blue",fg="white",height=1,width=5)
   updatebutton.grid(row=0,column=1,padx=20,pady=3)


   # delete button
   Deletebutton = Button(buttonFrame,text="delete",bg="blue",fg="white",height=1,width=5)
   Deletebutton.grid(row=0,column=2,padx=20,pady=3)


   # reset button
   resetbutton = Button(buttonFrame,text="reset",bg="blue",fg="white",height=1,width=5)
   resetbutton.grid(row=0,column=3,padx=20,pady=3)

   #Search Frame################################33
   SearchFrame = LabelFrame(ShowEntryFrame,text="Search",bg="white",borderwidth= 2,relief=GROOVE)
   SearchFrame.place(x=30,y=0,width=600,height=60)

   #search lable
   Search_lable = Label(SearchFrame,text="Search By :",bg="black",fg="red",font="arial 15 bold")
   Search_lable.grid(row=0, column=0,sticky=W,padx=6,pady=2)
   Search_combo = ttk.Combobox(SearchFrame,font="comicsans 12",width=15)
   Search_combo["value"]=("Select Option","Name","Roll. no.","Semester","Course","Year")
   Search_combo.grid(row=0,column=1,sticky=W,padx=1,pady=2)

   search_entry = ttk.Entry(SearchFrame,font="comicsans 12",width=16,background="blue")
   search_entry.grid(row=0,column=2,sticky=W,padx=9,pady=2)

   # Search button
   Searchbutton = Button(SearchFrame,text="Search",bg="blue",fg="white",height=1,width=5)
   Searchbutton.grid(row=0,column=3,padx=10,pady=2)

   # Show button
   Showbutton = Button(SearchFrame,text="Show All",bg="blue",fg="white",height=1,width=6)
   Showbutton.grid(row=0,column=4,padx=10,pady=2)

   ######################## Student Table and Scroll Bar########################
   table_frame = Frame(ShowEntryFrame,bd=4,relief=RAISED)
   table_frame.place(x=10,y=70,width=635,height=540)

   #############Scroll Bar
   scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)

   scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
   self.student_table=ttk.Treeview(table_frame,columns=("name","gender","roll","fathername","course","sem","ph.no.","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
   scroll_x.pack(side=BOTTOM,fill=X)
   scroll_y.pack(side=RIGHT,fill=Y)

   scroll_x.config(command=self.student_table.xview)
   scroll_y.config(command=self.student_table.yview)

   self.student_table.heading("name",text="Name")
   self.student_table.heading("gender",text="Gender")
   self.student_table.heading("roll",text="Roll.No.")
   self.student_table.heading("fathername",text="Father Name")
   self.student_table.heading("course",text="Course")
   self.student_table.heading("sem",text="Semester")
   self.student_table.heading("ph.no.",text="Mobile no.")
   self.student_table.heading("email",text="Email")

   self.student_table["show"]="headings"

   self.student_table.column("name",width=100)
   self.student_table.column("gender",width=50)
   self.student_table.column("roll",width=100)
   self.student_table.column("fathername",width=100)
   self.student_table.column("course",width=100)
   self.student_table.column("sem",width=70)
   self.student_table.column("ph.no.",width=100)
   self.student_table.column("email",width=100)

   self.student_table.pack(fill=BOTH,expand=1)


 def addData(self):
   if(self.var_dep.get() or self.var_roll.get() or self.var_dob.get()==""):
      messagebox.showerror("Error","All Fields are requires")
   else:
      try:
         conn = mysql.connector.connect(host="localhost",username="root",password ="faroj",database="python3pm")
         my_cursor=conn.cursor()
         my_cursor.execute("insert into student_management values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                               self.var_gender.get(),
                                                                               self.var_roll.get(),
                                                                               self.var_gender.get(),
                                                                               self.var_father.get(),
                                                                               self.var_course.get(),
                                                                               self.var_mob.get(),
                                                                               self.var_dob.get(),))
         conn.commit()
         conn.close()
         messagebox.showinfo("Success","Student has been adde!",parent=root)
      except Exception as es:
         messagebox.showerror('Error',f"Due to:(str(es))",parent =self.root)


if __name__ =="__main__":
      root = Tk()
      obj =Student(root)
      root.mainloop()