from tkinter import *
from tkinter import ttk , messagebox
from db import Database
import sqlite3
import re
db = Database("employee.db")

#--------------------  ROOT ----------------- 
root = Tk()
root.geometry("1300x650")
root.title("ahmed mangement")
root.resizable(FALSE,FALSE)
root.configure(bg="gray")
#---------------- VARIABLE NAMES -------------
name  = StringVar()
job   = StringVar()
age   = StringVar()
gender =StringVar()
email  =StringVar()
phone  =StringVar()
#------------------  logo ------------------
logo = PhotoImage(file="logo.png")
label = Label(root,image=logo)
label.place(x=0,y=255)
#---------------------FRAME1----------------
frame1 = Frame(root,bg="blue")
frame1.place(x=1,y=1,width=350,height=480)
#---------------------title-----------------
title = Label(frame1,text='Company',font=('Comic sans',18,'bold'),bg="blue",fg= "white")
title.place(x=80,y=1)
#  Lables & TEXTS -- 1 ----------------------
lblname = Label(frame1,text = " Name" ,font=('Comic sans',16),bg="blue",fg= "white"  )
lblname.place(x=5,y=50)
txtname = Entry(frame1,textvariable =name, font=('Comic sans',12),)
txtname.place(x=100,y=50)
#================= 2 =========================
lbljob = Label(frame1,text = " Job" ,font=('Comic sans',16),bg="blue",fg= "white" )
lbljob.place(x=5,y=90)
txtjob = Entry(frame1,textvariable =job, font=('Comic sans',12))
txtjob.place(x=100,y=90)
#=======COMBOBOX =======3==========================
lblgender = Label(frame1,text = " Gender" ,font=('Comic sans',16),bg="blue",fg= "white" )
lblgender.place(x=5,y=130)
comb = ttk.Combobox(frame1,state= "readonly" ,textvariable =gender,width= 14,font=('Comic sans',16))
comb["values"] = ("Male" , "Female")
comb.place(x=100,y=130)
#===================== 4 ======================
lblage = Label(frame1,text = " Age" ,font=('Comic sans',16),bg="blue" ,fg= "white")
lblage.place(x=5,y=170)
txtage = Entry(frame1, font=('Comic sans',12),textvariable =age)
txtage.place(x=100,y=170)
#====================== 5 ====================
lblemail = Label(frame1,text = " Email" ,font=('Comic sans',16),bg="blue" ,fg= "white")
lblemail.place(x=5,y=210)
txtemail = Entry(frame1,textvariable =email, font=('Comic sans',12),)
txtemail.place(x=100,y=210)
#====================== 6 ====================
lblphone = Label(frame1,text = " Phone",font=('Comic sans',16),bg="blue",fg= "white")
lblphone.place(x=5,y=250)
txtphone = Entry(frame1,textvariable =phone, font=('Comic sans',12))
txtphone.place(x=100,y=250)
#====================== 7 ====================
lbladdress = Label(frame1,text = " Address",font=('Comic sans',16),bg="blue",fg= "white")
lbladdress.place(x=5,y=290)
txtaddress = Text(frame1, font=('Comic sans',12),width= 35 , height= 3)
txtaddress.place(x=15,y=320)
#---------------------DEFINE---------------------
# FUNCTION  getdata
# FUNCTION  displayAll
# FUNCTION   delete
# FUNCTION   update
# FUNCTION    clear
# FUNCTION  add_employee
# -------------------------------------------------
"""
This function is triggered when a row in the treeview is selected. 
It retrieves the data from the selected row and populates the input fields with the data.
If the selected row is empty, the input fields are cleared.
Parameters:
    event (Event): The event that triggered the function
Returns:
    None
"""
def getdata(event):
    selected_row = tree.focus()
    data = tree.item(selected_row)
    global row
    row = data["values"]
    if len(row) > 1:
        name.set(row[1])
        age.set(row[2])
        job.set(row[3])  
        gender.set(row[4])
        email.set(row[5])   
        phone.set(row[6])
    else:
        name.set("")
        age.set("")
        job.set("")
        email.set("")  
        gender.set("")   
        phone.set("")
    txtaddress.delete(1.0, END)
    txtaddress.insert(END,row[7])
# -------------------------------------------------
"""
This function is used to display all the records 
in the tree view.
Parameters:
        None
Returns:
        None
"""
def displayAll():
    tree.delete(*tree.get_children())
    rows = db.fetch()
    for row in db.fetch():
        tree.insert("",END,values=row)
# -------------------------------------------------
"""
Delete the currently selected row from the database.
Raises:
    ValueError: If no row is currently selected.
Returns:
    None
"""
def delete():
    db.remove(row[0])
    messagebox.showinfo("Success" "Employee is deleted successfully")
    clear()
    displayAll()
#-------------------------------------------------------------------
"""
Update the currently selected row in the database.

Raises:
    ValueError: If no row is currently selected.

Returns:
    None
"""     
def update():
    if txtname.get() == '' or txtage.get() == "" or txtjob.get()=="" or comb.get()=="" or txtemail.get()=="" or txtphone.get()=="" or txtaddress.get(1.0,END) == "":
        messagebox.showerror("Error","Please Fill ALL The Fields ")
        return
    db.update(row[0],txtname.get(),txtage.get(),txtjob.get(),comb.get(),txtemail.get(),txtphone.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("Success" "Employee is updated successfully")
    clear()
    displayAll()
#-------------------------------------------------------------------
"""
Clears all the input fields.
"""
def clear():
    name.set("")
    age.set("")
    job.set("")
    email.set("")
    gender.set("")
    phone.set("")
    txtaddress.delete(1.0, END)
 #--------------------------------------------------------
"""
This function adds a new employee to the database.
Parameters:
    txtname (str): The name of the employee.
    txtage (str): The age of the employee.
    txtjob (str): The job of the employee.
    comb (str): The gender of the employee.
    txtemail (str): The email of the employee.
    txtphone (str): The phone number of the employee.
    txtaddress (str): The address of the employee.
Returns:
    None
Raises:
    ValueError: If any of the input fields are empty.
"""
def add_employee():
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\d{10}$'
    if txtname.get() == '' or txtage.get() == "" or txtjob.get()=="" or comb.get()=="" or txtemail.get()=="" or txtphone.get()=="" or txtaddress.get(1.0,END) == "":
        messagebox.showerror("تنبيه","من فضلك املأكافة الحقول ")
        return
    elif not re.fullmatch(email_pattern, txtemail.get()):
        messagebox.showerror("تنبيه", "خطأ في كتابة البريد الالكتروني")
        return
    elif not re.fullmatch(phone_pattern, txtphone.get()) or not txtphone.get().isdigit():
        messagebox.showerror("تنبيه", "خطأ في كتابة رقم الهاتف")
        return
    else:
        db.insert (txtname.get(),
                   txtage.get(),
                   txtjob.get(),
                   comb.get(),
                   txtemail.get(),
                   txtphone.get(),
                   txtaddress.get(1.0,END))
        messagebox.showinfo("Success" "New Employee is added successfully")
    clear()
    displayAll()
#=============================================
#Buttons  (add details , clear details . delete  ,edit )

btnadd = Button(frame1,text = "Add",font=('Comic sans',16),width=10,bg="green",fg= "white", command = add_employee)
btnadd.place(x=25,y=385)
#------------------------------------------------------------
btnclear = Button(frame1,text = "Clear",width=10,font=('Comic sans',16),bg="yellow",fg= "black", command = clear)
btnclear.place(x=25,y=430)
#------------------------------------------------------------
btndelete = Button(frame1,text = "Delete",font=('Comic sans',16),width=10,bg="red",fg= "white",command = delete)
btndelete.place(x=200,y=385)
#------------------------------------------------------------
btnedit = Button(frame1,text = "Edit",width=10,font=('Comic sans',16),bg="orange",fg= "white",command=update)
btnedit.place(x=200,y=430)
#=============================================
 #===============Tree Frame ==================
frame2 = Frame(root,bg="#81d4fa")
frame2.place(x=355,y=1,width=950,height=650)

tree = ttk.Style()
tree.configure("mystyle.Treeview" , font = 13 , rowheight=50)
tree.configure( "mystyle.Treeview . Heading" ,font = 13)
tree = ttk.Treeview(frame2,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview" )
#------------------------Scrollbar----------------------------
scrollbarY = Scrollbar(frame2,orient='vertical')
scrollbarX = Scrollbar(frame2, orient='horizontal')
tree.configure(yscrollcommand=scrollbarY.set)
tree.configure(xscrollcommand=scrollbarX.set)
scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)
scrollbarX.config(command=tree.xview)
scrollbarY.config(command=tree.yview)
tree.pack(side=LEFT,fill=BOTH,expand=1)
#=============================================
#======headings for the tree view=============
tree.heading("1",text="ID" )
tree.column("1",width=20 ,anchor="center")
tree.heading("2",text="Name")
tree.column("2",width=150 ,anchor="center" )
tree.heading("3",text="Age")
tree.column("3",width=50,anchor="center" )
tree.heading("4",text="Job")
tree.column("4",width=90,anchor="center" )
tree.heading("5",text="Gender")
tree.column("5",width=50 ,anchor="center")
tree.heading("6",text="Email")
tree.column("6",width=150 ,anchor="center")
tree.heading("7",text="Phone")
tree.column("7",width=120 ,anchor="center")
tree.heading("8",text="Address")
tree.column("8",width=120,anchor="center" )
tree['show']='headings'
# #=============================================
tree.bind("<ButtonRelease-1>",getdata)
displayAll()
tree.pack()
root.mainloop()