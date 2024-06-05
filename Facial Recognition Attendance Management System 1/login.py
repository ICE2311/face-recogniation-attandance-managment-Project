from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.root = root
        self.root.title("Login")
        self.root.geometry('1550x800+0+0')

        self.bg = ImageTk.PhotoImage(file=r'Face Images\college_images\1900857.webp')
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg='black')
        frame.place(x=610, y=170, width=340,height=450)

        img1 = Image.open(r'Face Images\college_images\LoginIconAppl.png')
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg = "black", borderwidth=0)
        lblimg1.place(x = 730, y = 175, width = 100, height = 100)

        get_str = Label(frame, text='Get Started', font=('times new roman', 20, 'bold'), fg='white', bg='black')
        get_str.place(x=95, y=100)

        # Label
        username = lbl = Label(frame, text='Username', font=('times new roman', 15, 'bold'), fg='white', bg='black')
        username.place(x=70, y=155)

        self.txtusr = ttk.Entry(frame, font=('times new roman', 15, 'bold'))
        self.txtusr.place(x=40,y=180, width=270)

        password = lbl = Label(frame, text='Password', font=('times new roman', 15, 'bold'), fg='white', bg='black')
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=('times new roman', 15, 'bold'))
        self.txtpass.place(x=40, y=250, width=270)

        # ============================= Icon Images =============================

        img2 = Image.open(r'Face Images\college_images\LoginIconAppl.png')
        img2 = img1.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r'Face Images\college_images\lock-512.png')
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=392, width=25, height=25)

        # =================== Login Button ===================
        loginbtn = Button(frame, text='Login', command=self.login ,font=('times new roman', 15, 'bold'), bd=3, relief=RIDGE, fg='white', bg='red', activeforeground='white', activebackground='red')
        loginbtn.place(x=110 ,y=300, width=120, height=35)

        # =================== Registration Button ===================

        registerbtn = Button(frame, text='New User Register', command=self.register_window ,font=('times new roman', 10, 'bold'), borderwidth=0, fg='white', bg='black', activeforeground='white', activebackground='black')
        registerbtn.place(x=15, y=350, width=160)

        # Forget password

        forgrtpassbtn = Button(frame, text='Forget Password', command=self.forget_password_window, font=('times new roman', 10, 'bold'), borderwidth=0, fg='white',bg='black', activeforeground='white', activebackground='black')
        forgrtpassbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtusr.get() == '' or self.txtpass.get() == '':
            messagebox.showerror('Error','All Field Required')
        elif self.txtusr.get() == 'sushant' and self.txtpass.get() == '1234':
            messagebox.showinfo('Success','Welcome to Student Management System')
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='mydata')
            my_cursor = conn.cursor()
            my_cursor.execute('select * from register where email = %s and password = %s',(self.var_email.get(), self.var_pass.get()))
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Invalid User Name Or Password')
            else:
                open_main = messagebox.askyesno('YesNo', 'Access Only Admin')
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ============================= Reset Password ====================
    def reset_pass(self):
        if self.combo_securiy_q.get()=='Select':
            messagebox.showerror('Error','Select The Security Question')
        elif self.txt_security.get()=='':
            messagebox.showerror('Error','Please Enter The Answer')
        elif self.txt_new_password.get()=='':
            messagebox.showerror('Error','Please Enter The New Password')
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='mydata')
            my_cursor = conn.cursor()
            query = 'select * from register where email=%s and securityq=%s and securityA=%s'
            value = (self.txtusr.get(),self.combo_securiy_q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror('Error','Please Enter Correct Answer',parent=self.root2)
            else:
                query = 'update register set password = %s where email = %s'
                value=(self.txt_new_password.get(),self.txtusr.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo('Info','Your Password Has Been Reset, Please Login New Password',parent=self.root2)
                self.root2.destroy()


    # ============================= Forget Password ===================
    def forget_password_window(self):
        if self.txtusr.get()=='':
            messagebox.showerror('Error','Please Enter The Email Address To Reset Password')
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='mydata')
            my_cursor = conn.cursor()
            query = 'select * from register where email = %s'
            value = (self.txtusr.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            #print(row)

            if row == None:
                messagebox.showerror('My Error','Please Enter The Valid Username')
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title('Forget Password')
                self.root2.geometry('340x400+610+170')

                l = Label(self.root2, text='Forget Password',font=('times new roman',20,'bold'),fg='red',bg='white')
                l.place(x=0,y=10,relwidth=1)

                security_q = Label(self.root2, text='Select Security Questions', font=('times new roman', 15, 'bold'), bg='white', fg='black')
                security_q.place(x=50, y=80)

                self.combo_securiy_q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_securiy_q["values"] = ("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
                self.combo_securiy_q.place(x=50, y=110, width=250)
                self.combo_securiy_q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_password.place(x=50, y=220)

                self.txt_new_password = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_new_password.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass,font=("times new roman", 15, "bold"), bg="green",fg="white")
                btn.place(x=120,y=290)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Register')
        self.root.geometry('1600x900+0+0')

        # =============== variable ================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityq = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file = '2184693.webp')
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1,relheight=1)

        # Left Image
        self.bg1 = ImageTk.PhotoImage(file='thought-good-morning-messages-LoveSove.jpg')
        bg_lbl1 = Label(self.root, image=self.bg1)
        bg_lbl1.place(x=100, y=100, width=470, height=550)

        # Main Frame
        frame = Frame(self.root, bg='white')
        frame.place(x=570, y=100, width=800, height=550)

        register_lbl = Label(frame,text = 'Register Here', font = ('times new roman', 20, 'bold'), fg='darkgreen', bg='white')
        register_lbl.place(x=20, y=20)

        # Label and Entry

        # ---------- Row1
        fname = Label(frame,text = 'First Name', font = ('times new roman', 20, 'bold'), bg='white')
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname ,font = ('times new roman', 20, 'bold'))
        self.fname_entry.place(x = 50, y = 130, width=250)

        l_name = Label(frame, text='Last Name', font=('times new roman', 20, 'bold'), bg='white')
        l_name.place(x=370, y=100)

        self.txt_l_name = ttk.Entry(frame, textvariable=self.var_lname, font=('times new roman', 20, 'bold'))
        self.txt_l_name.place(x=370, y=130, width=250)

        # ------------ Row2
        contact = Label(frame, text='Contact', font=('times new roman', 20, 'bold'), bg='white')
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=('times new roman', 20, 'bold'))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text='Email', font=('times new roman', 20, 'bold'), bg='white')
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=('times new roman', 20, 'bold'))
        self.txt_email.place(x=370, y=200, width=250)

        # ------------ Row3

        security_q = Label(frame, text='Select Security Questions', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        security_q.place(x=50, y=240)

        self.combo_securiy_q = ttk.Combobox(frame, textvariable=self.var_securityq, font = ("times new roman", 15, "bold"), state="readonly")
        self.combo_securiy_q["values"] = ("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_securiy_q.place(x=50, y = 270, width=250)
        self.combo_securiy_q.current(0)


        security_A = Label(frame, text="Security Answer", font = ("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x = 378, y=278, width=250)

        # ------------- Row4

        pswd = Label(frame, text="Password ",font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        pswd.place(x = 50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font = ("times new roman", 15))
        self.txt_pswd.place(x = 50, y=348, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font = ("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font = ("times new roman", 15))
        self.txt_confirm_pswd.place(x = 370, y=340, width=250)

        # Check Button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text='I Agree The Terms and Conditions', font = ("times new roman", 12, 'bold'), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=390)

        # Buttons
        img = Image.open('register-now-button1.jpg')
        img = img.resize((200,50),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0, cursor='hand2', fg='white')
        b1.place(x=50,y=420, width=200)

        img1 = Image.open('loginpng.png')
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor='hand2', fg='white')
        b1.place(x=370, y=420, width=200)

    # =================================== Function Declaration ==============================
    def register_data(self):
        if self.var_fname.get() == '' or self.var_email.get() == '' or self.var_securityq.get() == '':
            messagebox.showerror('Error','All Field Are Required')
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror('Error','Password And Confirm Password Must Be Same')
        elif self.var_check.get() == 0:
            messagebox.showerror('Error','Please Agree Our Terms and Condition')
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='mydata')
            my_cursor = conn.cursor()
            query = 'select * from register where email=%s'
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'User Already Exist Please Try Another Email')
            else:
                my_cursor.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s)',(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityq.get(),self.var_securityA.get(),self.var_pass.get()))

            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Register Successfull')


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Register')
        self.root.geometry('1600x900+0+0')

        # =============== variable ================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityq = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r'Face Images\college_images\2184693.webp')
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1,relheight=1)

        # Left Image
        self.bg1 = ImageTk.PhotoImage(file=r'Face Images\college_images\thought-good-morning-messages-LoveSove.jpg')
        bg_lbl1 = Label(self.root, image=self.bg1)
        bg_lbl1.place(x=100, y=100, width=470, height=550)

        # Main Frame
        frame = Frame(self.root, bg='white')
        frame.place(x=570, y=100, width=800, height=550)

        register_lbl = Label(frame,text = 'Register Here', font = ('times new roman', 20, 'bold'), fg='darkgreen', bg='white')
        register_lbl.place(x=20, y=20)

        # Label and Entry

        # ---------- Row1
        fname = Label(frame,text = 'First Name', font = ('times new roman', 20, 'bold'), bg='white')
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname ,font = ('times new roman', 20, 'bold'))
        self.fname_entry.place(x = 50, y = 130, width=250)

        l_name = Label(frame, text='Last Name', font=('times new roman', 20, 'bold'), bg='white')
        l_name.place(x=370, y=100)

        self.txt_l_name = ttk.Entry(frame, textvariable=self.var_lname, font=('times new roman', 20, 'bold'))
        self.txt_l_name.place(x=370, y=130, width=250)

        # ------------ Row2
        contact = Label(frame, text='Contact', font=('times new roman', 20, 'bold'), bg='white')
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=('times new roman', 20, 'bold'))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text='Email', font=('times new roman', 20, 'bold'), bg='white')
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=('times new roman', 20, 'bold'))
        self.txt_email.place(x=370, y=200, width=250)

        # ------------ Row3

        security_q = Label(frame, text='Select Security Questions', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        security_q.place(x=50, y=240)

        self.combo_securiy_q = ttk.Combobox(frame, textvariable=self.var_securityq, font = ("times new roman", 15, "bold"), state="readonly")
        self.combo_securiy_q["values"] = ("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_securiy_q.place(x=50, y = 270, width=250)
        self.combo_securiy_q.current(0)


        security_A = Label(frame, text="Security Answer", font = ("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x = 378, y=278, width=250)

        # ------------- Row4

        pswd = Label(frame, text="Password ",font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        pswd.place(x = 50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font = ("times new roman", 15))
        self.txt_pswd.place(x = 50, y=348, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font = ("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font = ("times new roman", 15))
        self.txt_confirm_pswd.place(x = 370, y=340, width=250)

        # Check Button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text='I Agree The Terms and Conditions', font = ("times new roman", 12, 'bold'), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=390)

        # Buttons
        img = Image.open(r'Face Images\college_images\register-now-button1.jpg')
        img = img.resize((200,50),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0, cursor='hand2', fg='white')
        b1.place(x=50,y=420, width=200)

        img1 = Image.open(r'Face Images\college_images\loginpng.png')
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, command=self.return_login ,borderwidth=0, cursor='hand2', fg='white')
        b1.place(x=370, y=420, width=200)

    # =================================== Function Declaration ==============================
    def register_data(self):
        if self.var_fname.get() == '' or self.var_email.get() == '' or self.var_securityq.get() == '':
            messagebox.showerror('Error','All Field Are Required')
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror('Error','Password And Confirm Password Must Be Same')
        elif self.var_check.get() == 0:
            messagebox.showerror('Error','Please Agree Our Terms and Condition')
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='mydata')
            my_cursor = conn.cursor()
            query = 'select * from register where email=%s'
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'User Already Exist Please Try Another Email')
            else:
                my_cursor.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s)',(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityq.get(),self.var_securityA.get(),self.var_pass.get()))

            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Register Successfull')

    def return_login(self):
        self.root.destroy()


if __name__ == '__main__':
    main()