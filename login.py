from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk,ImageDraw #pip install pillow
import pymysql #pip install pymysql
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")

        self.root.config(bg="white")
        ## ================Bg Image======
        self.bg=ImageTk.PhotoImage(file="images/main_pic.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        ##============Left Image=====
        self.left=ImageTk.PhotoImage(file="images/1.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        ##=========Register Frame============
        frame2=Frame(self.root,bg="white")
        frame2.place(x=480,y=100,width=500,height=500)

        title=Label(frame2,text="Admin Login",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=130,y=30)
        ###Registration Number
        f_reg=Label(frame2,text="Email*",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=100)
        self.txt_email=Entry(frame2,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=100,y=130,width=250)


        ##Password
        password=Label(frame2,text="Password*",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=170)
        self.txt_password=Entry(frame2,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=100,y=200,width=250)


        ## Login Button
        btn=Button(frame2,text="Sign In",font=("times new roman",15,"bold"),bg="yellow",fg="green",bd=0,cursor="hand2",command=self.login_data).place(x=150,y=260,width=160,height=50)


    def clear(self):
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
       


    def register_window(self):
        self.root.destroy()
        import register



    def login_data(self):
        if self.txt_email.get()==""  or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()
                cur.execute("select * from admin where email_id=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid EMAIL & PASSWORD",parent=self.root)
                    # self.root.destroy()
                    # import register
                else:
                    messagebox.showinfo("Success","Congratulation,Login Sucessful",parent=self.root)
                    self.root.destroy()
                    import Student
                con.close()   
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)



root=Tk()
obj=Login(root)
root.mainloop()