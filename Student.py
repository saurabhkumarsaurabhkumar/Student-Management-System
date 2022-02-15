import imp
from operator import imod
from random import random
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from click import command #pip install pillow
import pymysql #pip install pymysql

import string
import random

import smtplib

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Home")
        self.root.geometry("1350x700+0+0")
        # self.root.config(bg="green")
        title=Label(self.root,text="Employee Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="grey",fg="yellow")
        title.pack(side=TOP,fill=X)


    ##########----All Variables---##########
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()


        self.search_by=StringVar()
        self.search_txt=StringVar()
    #######--Manage Frame--#########
        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_frame.place(x=20,y=100,width=450,height=590)

        m_title=Label(manage_frame,text="Manage Employee",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(manage_frame,text="Roll No",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll=Entry(manage_frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name=Label(manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(manage_frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_email=Entry(manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20)

        lbl_contact=Label(manage_frame,text="Contact No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_contact=Entry(manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB=Label(manage_frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_DOB=Entry(manage_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txt_address=Text(manage_frame,width=30,height=3,font=(" ",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

     #######--Button Frame--#########
        btn_frame=Frame(manage_frame,bd=4,relief=RIDGE,bg="crimson")
        btn_frame.place(x=0,y=500,width=460)

        Addbtn=Button(btn_frame,text="Add",width=10,command=self.add_employee).grid(row=0,column=0,padx=5,pady=10)
        Updatebtn=Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=5,pady=10)
        deletebtn=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=5,pady=10)
        clearbtn=Button(btn_frame,text="Clear",command=self.clear,width=10).grid(row=0,column=3,padx=5,pady=10)
        mailsend=Button(btn_frame,text="Mail",command=self.sendEmpMail,width=10).grid(row=0,column=4,padx=5,pady=10)


    



    #######--Details Frame--#######

        details_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        details_frame.place(x=500,y=100,width=800,height=590)

        lbl_search=Label(details_frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(details_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20)


        txt_search=Entry(details_frame,width=20,textvariable=self.search_txt,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(details_frame,text="Search",command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showbtn=Button(details_frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#######--- Table Frame -----###############
        Table_Frame=Frame(details_frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=510)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_employee(self):

        if self.Roll_No_var==" " or self.name_var==" " or self.email_var==" " or self.gender_var==" " or self.contact_var==" " or self.dob_var==" " or self.txt_address==" ":
            messagebox.showerror("Error","All Fields are required")

        elif self.Roll_No_var!=" " and self.name_var!=" " and self.email_var!=" " and self.gender_var!=" " and self.contact_var!=" " and self.dob_var!=" " and self.txt_address!=" ":

            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.name_var.get(),
                                                                                self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),
                                                                                self.txt_address.get('1.0',END)
            ))

        print(''.join([random.choice(string.ascii_letters+string.digits) for i in range(6)])) ## Generate a random unique Id upto 6 digit

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def sendEmpMail(self):
        address_info=self.email_var.get()
        subject="Credentials Details "+self.name_var.get()
        email_body="Congratulation :)\nYou details given below\n"+"Emp id :"+self.Roll_No_var.get()+"\n"+"Emp Name :"+self.name_var.get()+"\n"+"Emp Mail :"+self.email_var.get()+"\n"+"Emp Gender :"+self.gender_var.get()+"\n"+"Emp Mobile No :"+self.contact_var.get()+"\n"+"Emp DOB :"+self.dob_var.get()+"\n"+"Emp Address :"+self.txt_address.get("1.0",'end-1c')+"\n"+"Thanks & Regards :\n"+"Saurabh Kumar"+"\n"+"Software Developer at Agatsa Software\n"+"Contact No :"+"7355794240"
        sub_and_body_msg = 'Subject: {}\n\n{}'.format(subject, email_body)
        sender_email="nitiansk@gmail.com"
        send_pass="7237084256"


        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,send_pass)

        print("Login Sucessfully")
        server.sendmail(sender_email,address_info,sub_and_body_msg)
        messagebox.showinfo("Success","Congratulation,Details have been sent Sucessfully on your registered mail i'd")
        print("Messeges have been sent")



    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def clear(self):
        self.Roll_No_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.txt_address.delete("1.0",END)

    def get_cursor(self,env):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name_var=%s,email_var=%s,gender_var=%s,contact_var=%s,dob_var=%s,txt_address=%s where Roll_No_var=%s",(self.name_var.get(),
                                                                            self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END),
                                                                            self.Roll_No_var.get()
        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where Roll_No_var=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()



    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where"+"str(self.search_by.get())"+ "LIKE '%'+str(self.search_txt.get()) + '%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    

root=Tk()
obj=Register(root)
root.mainloop()
