from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

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









if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()