from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1500x790+0+0')
        self.root.title('Face Recognition System')

        # ===============Variables===============
        self.var_Dep = StringVar()
        self.var_Course = StringVar()
        self.var_Year = StringVar()
        self.var_Semester = StringVar()
        self.var_Student_id = StringVar()
        self.var_Name = StringVar()
        self.var_Div = StringVar()
        self.var_Roll = StringVar()
        self.var_Gender = StringVar()
        self.var_Dob = StringVar()
        self.var_Email = StringVar()
        self.var_Phone = StringVar()
        self.var_Address = StringVar()
        self.var_Teacher = StringVar()

        # First Image
        img = Image.open(r'Face Images\college_images\face-recognition.png')
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(r'Face Images\college_images\smart-attendance.jpg')
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r'Face Images\college_images\iStock-182059956_18390_t12.jpg')
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open(r'Face Images\college_images\wp2551980.jpg')
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text='Student Management System', font=('times new roman', 35, 'bold'), bg='white', fg='darkgreen')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg='white')
        main_frame.place(x=10,y=55,width=1480,height=600)

        # left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font=('times new roman',12,'bold'))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r'Face Images\college_images\AdobeStock_303989091.jpeg')
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_label = Label(left_frame, image=self.photoimg_left)
        f_label.place(x=5, y=0, width=720, height=130)

        # Current course
        current_course_frame = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text='Current Course Information',font=('times new roman', 12, 'bold'))
        current_course_frame.place(x=5, y=135, width=715, height=120)

        # Department
        departmet_label = Label(current_course_frame,text='Department',font=('times new roman', 12, 'bold'),bg='white')
        departmet_label.grid(row=0,column=0,padx=10)

        department_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Dep,font=('times new roman', 12, 'bold'),state='read only')
        department_combo['values'] = ('Select Department','Computer Science','I.T','Data Science','Biology')
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx=2,pady=10)

        # Courses
        courses_label = Label(current_course_frame, text='Courses', font=('times new roman', 12, 'bold'),bg='white')
        courses_label.grid(row=0, column=2, padx=10,sticky=W)

        courses_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Course, font=('times new roman', 12, 'bold'), state='read only',width=20)
        courses_combo['values'] = ('Select Courses', 'Python', 'AI', 'ML', 'DP')
        courses_combo.current(0)
        courses_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text='Year', font=('times new roman', 12, 'bold'), bg='white')
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Year, font=('times new roman', 12, 'bold'), state='read only',width=20)
        year_combo['values'] = ('Select Year', '2020-2021', '2021-2022', '2022-2023', '2023-20224')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text='Semester', font=('times new roman', 12, 'bold'), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Semester, font=('times new roman', 12, 'bold'), state='read only',width=20)
        semester_combo['values'] = ('Select Semester', 'sem-1', 'sem-2', 'sem-3', 'sem-4','sem-5','sem-6')
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text='Class Student Information',font=('times new roman', 12, 'bold'))
        class_student_frame.place(x=5, y=250, width=715, height=300)

        #Student id
        studentid_label = Label(class_student_frame, text='StudentID:', font=('times new roman', 12, 'bold'), bg='white')
        studentid_label.grid(row=0, column=0, padx=10, sticky=W)

        studentid_entry = ttk.Entry(class_student_frame,textvariable=self.var_Student_id,width=20,font=('times new roman', 12, 'bold'))
        studentid_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student name
        studentname_label = Label(class_student_frame, text='Student Name:', font=('times new roman', 12, 'bold'), bg='white')
        studentname_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentname_entry = ttk.Entry(class_student_frame, textvariable=self.var_Name, width=20, font=('times new roman', 12, 'bold'))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5,sticky=W)

        # class division
        class_div_label = Label(class_student_frame, text='Class Division:', font=('times new roman', 12, 'bold'), bg='white')
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        #class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=('times new roman', 12, 'bold'))
        #class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_Div,font=('times new roman', 12, 'bold'), state='read only', width=15)
        class_div_combo['values'] = ('Select Division','A','B','C','D')
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # roll number
        roll_no_label = Label(class_student_frame, text='Roll No:', font=('times new roman', 12, 'bold'),bg='white')
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_Roll, width=20, font=('times new roman', 12, 'bold'))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text='Gender:', font=('times new roman', 12, 'bold'),bg='white')
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        #gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=20, font=('times new roman', 12, 'bold'))
        #gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_Gender,font=('times new roman', 12, 'bold'), state='read only', width=15)
        gender_combo['values'] = ('Male','Female','Other')
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text='DOB:', font=('times new roman', 12, 'bold'),bg='white')
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_Dob, width=20, font=('times new roman', 12, 'bold'))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text='Email:', font=('times new roman', 12, 'bold'),bg='white')
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_Email, width=20, font=('times new roman', 12, 'bold'))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone Number
        phone_number_label = Label(class_student_frame, text='Phone No:', font=('times new roman', 12, 'bold'),bg='white')
        phone_number_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_number_entry = ttk.Entry(class_student_frame, textvariable=self.var_Phone, width=20, font=('times new roman', 12, 'bold'))
        phone_number_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text='Address:', font=('times new roman', 12, 'bold'),bg='white')
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_Address, width=20, font=('times new roman', 12, 'bold'))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_name_label = Label(class_student_frame, text='Teacher Name:', font=('times new roman', 12, 'bold'), bg='white')
        teacher_name_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_Teacher, width=20, font=('times new roman', 12, 'bold'))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable = self.var_radio1, text='Take Photo Sample', value='Yes')
        radiobtn1.grid(row=6,column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable = self.var_radio1, text='No Photo Sample', value='No')
        radiobtn2.grid(row=6, column=1)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=200, width=710, height=38)

        save_btn = Button(btn_frame, text='Save', command=self.add_data ,width=19, font=('times new roman', 12, 'bold'), bg='blue', fg='white')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text='Update', command=self.update_data ,width=19, font=('times new roman', 12, 'bold'), bg='blue', fg='white')
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text='Delete', command=self.delete_data ,width=19, font=('times new roman', 12, 'bold'), bg='blue', fg='white')
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text='Reset', command=self.reset_data ,width=19, font=('times new roman', 12, 'bold'), bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame1.place(x=0, y=235, width=710, height=38)

        take_photo_btn = Button(btn_frame1, text='Take Photo Sample', command= self.generate_dataset,width=39, font=('times new roman', 12, 'bold'), bg='blue',fg='white')
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text='Update Photo Sample', width=39, font=('times new roman', 12, 'bold'),bg='blue', fg='white')
        update_photo_btn.grid(row=0, column=1)


        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Student Details',font=('times new roman', 12, 'bold'))
        right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r'Face Images\college_images\gettyimages-1022573162.jpg')
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_label = Label(right_frame, image=self.photoimg_right)
        f_label.place(x=5, y=0, width=720, height=130)

        # =============Search System==============
        search_frame = LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE, text='Search System',font=('times new roman', 12, 'bold'))
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text='Search By:', font=('times new roman', 15, 'bold'),bg='red',fg='white')
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=('times new roman', 12, 'bold'), state='read only',width=13)
        search_combo['values'] = ('Select ', 'Roll_no','Phone_no')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=('times new roman', 12, 'bold'))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text='Search', width=15, font=('times new roman', 12, 'bold'), bg='blue',fg='white')
        search_btn.grid(row=0, column=3, padx=4)

        showall_btn = Button(search_frame, text='Show All', width=15, font=('times new roman', 12, 'bold'), bg='blue',fg='white')
        showall_btn.grid(row=0, column=4, padx=4)

        # =============== Table Frane ===============
        table_frame = Frame(right_frame, bd=2, bg='white', relief=RIDGE,)
        table_frame.place(x=5, y=210, width=710, height=340)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=('Dep','Course','Year','Semester','Student_id','Name','Div','Roll','Gender','Dob','Email','Phone','Address','Teacher','Photo'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('Dep',text='Department')
        self.student_table.heading('Course', text='Course')
        self.student_table.heading('Year', text='Year')
        self.student_table.heading('Semester', text='Semester')
        self.student_table.heading('Student_id', text='StudentID')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Div', text='Division')
        self.student_table.heading('Roll', text='RollNo')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Dob', text='DOB')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('Phone', text='Phone')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Teacher', text='Teacher')
        self.student_table.heading('Photo', text='PhotoSampleStatus')
        self.student_table['show']='headings'

        self.student_table.column('Dep', width=100)
        self.student_table.column('Course', width=100)
        self.student_table.column('Year', width=100)
        self.student_table.column('Semester', width=100)
        self.student_table.column('Student_id', width=100)
        self.student_table.column('Name', width=100)
        self.student_table.column('Div', width=100)
        self.student_table.column('Roll', width=100)
        self.student_table.column('Gender', width=100)
        self.student_table.column('Dob', width=100)
        self.student_table.column('Email', width=100)
        self.student_table.column('Phone', width=100)
        self.student_table.column('Address', width=100)
        self.student_table.column('Teacher', width=100)
        self.student_table.column('Photo', width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()

    # ==================== Function Declarartion ====================

    def add_data(self):
        if self.var_dep.get()=='Select Department' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root',password='ROsh@1806',database='face_recogniser')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Students Details Has Been Added Successfully',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To :{str(es)}',parent=self.root)

    # =======================Fetch Data=================

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='facial_recognizer')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from Student')
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    # ======================Get Cursor==================
    def get_cursor(self,event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_dep.set(data[1]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ================= Update Function ==============

    def update_data(self):
        global conn
        if self.var_dep.get()=='Select Department' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=self.root)
        else:
            try:
                Update = messagebox.askyesno('Update','Do you want to update the student details',parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='facial_recognizer')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s',(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo('Success','Student detail updated successfully',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)

    # Delete Function
    def delete_data(self):
        if self.var_std_id.get()=='':
            messagebox.showerror('Error','Student Id must be required',parent=self.root)
        else:
            try:
                delete = messagebox.askyesno('stydent Dalete Page','Do you want to delete this student',parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='facial_recognizer')
                    my_cursor = conn.cursor()
                    sql = 'delete from student where Student_id=%s'
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Successfully deleted student details',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To: {str(es)}',parent=self.root)

    # Reset Function
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_course.set('Select Course')
        self.var_year.set('Select Year')
        self.var_semester.set('Select Semester')
        self.var_std_id.set('')
        self.var_std_name.set('')
        self.var_div.set('Select Division')
        self.var_roll.set('')
        self.var_gender.set('Male')
        self.var_dob.set('')
        self.var_email.set('')
        self.var_phone.set('')
        self.var_address.set('')
        self.var_teacher.set('')
        self.var_radio1.set('')

    # ===================== Generate Data Sets Take Photo Samples =====================

    def generate_dataset(self):
        if self.var_dep.get()=='Select Department' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='facial_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student')
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute('update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s',(self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()==id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # =================== Load Predefined Data on Face Frontals From Opencv =====================

                face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv.resize(face_cropped(my_frame),(450,450))
                        face = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
                        file_name_path = 'data/user.'+str(id)+'.'+str(img_id)+'.jpg'
                        cv.imwrite(file_name_path,face)
                        cv.putText(face,str(img_id),(50,50),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv.imshow('Cropped Face',face)

                    if cv.waitKey(1)==13 or int(img_id) == 100:
                        break

                cap.release()
                cv.destroyAllWindows()
                messagebox.showinfo('Result','Generating Dataset Completed Successfully')
            except EXCEPTION as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()