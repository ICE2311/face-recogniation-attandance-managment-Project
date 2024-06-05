from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1500x790+0+0')
        self.root.title('Face Recognition System')

        # =================== Text Variable ===================

        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # First Image
        img = Image.open(r'Face Images\college_images\smart-attendance.jpg')
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second Image
        img1 = Image.open(r'Face Images\college_images\iStock-182059956_18390_t12.jpg')
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # Background Image
        img3 = Image.open(r'Face Images\college_images\wp2551980.jpg')
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text='Attendance Management System', font=('times new roman', 35, 'bold'), bg='white',fg='darkgreen')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg='white')
        main_frame.place(x=10, y=55, width=1480, height=600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Student Attendance Details',font=('times new roman', 12, 'bold'))
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r'Face Images\college_images\AdobeStock_303989091.jpeg')
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_label = Label(left_frame, image=self.photoimg_left)
        f_label.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE ,bg='white')
        left_inside_frame.place(x=4, y=135, width=718, height=370)

        # ==================== Label And Entry ====================

        # Attendance Id
        Attendanceid_label = Label(left_inside_frame, text='Attendance ID:', font=('times new roman', 12, 'bold'),bg='white')
        Attendanceid_label.grid(row=0, column=0, padx=10, sticky=W)

        Attendanceid_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=('times new roman', 12, 'bold'))
        Attendanceid_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student Roll No
        name_label = Label(left_inside_frame, text='Roll:', font=('times new roman', 12, 'bold'),bg='white')
        name_label.grid(row=0, column=2, padx=4, pady=8)

        name_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name,font=('times new roman', 12, 'bold'))
        name_entry.grid(row=0, column=3, pady=8)

        # Student Name
        name_label = Label(left_inside_frame, text='Name:', font=('times new roman', 12, 'bold'), bg='white')
        name_label.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_name, font=('times new roman', 11, 'bold'))
        atten_name.grid(row=1,column=1, pady=8)

        # Department
        deplabel = Label(left_inside_frame, text='Department:', font=('times new roman', 12, 'bold'), bg='white')
        deplabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=('times new roman', 12, 'bold'))
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timelabel = Label(left_inside_frame, text='Time:', font=('times new roman', 12, 'bold'), bg='white')
        timelabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=('times new roman', 12, 'bold'))
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        datelabel = Label(left_inside_frame, text='Date:', font=('times new roman', 12, 'bold'), bg='white')
        datelabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=('times new roman', 12, 'bold'))
        atten_date.grid(row=2, column=3, pady=8)

        # Attendance
        attendancelabel = Label(left_inside_frame, text='Attendance Status:', font=('times new roman', 12, 'bold'), bg='white')
        attendancelabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance, font=('times new roman', 12, 'bold'), state='readonly')
        self.atten_status['values'] = ('Status', 'Present', 'Absent')
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=300, width=710, height=38)

        save_btn = Button(btn_frame, text='Import CSV', command=self.importCsv, width=19, font=('times new roman', 12, 'bold'),bg='blue', fg='white')
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text='Export CSV', command=self.exportCsv, width=19,font=('times new roman', 12, 'bold'), bg='blue', fg='white')
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text='Update', width=19,font=('times new roman', 12, 'bold'), bg='blue', fg='white')
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text='Reset', command=self.reset_data, width=19,font=('times new roman', 12, 'bold'), bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)


        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Attendance Details',font=('times new roman', 12, 'bold'))
        right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=5, y=5, width=705, height=455)

        # ==================== Scroll Bar Table ====================

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=('Id','Roll','Name','Department','Time','Date','Attendance'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('Id',text='Attendance ID')
        self.AttendanceReportTable.heading('Roll', text='Roll')
        self.AttendanceReportTable.heading('Name', text='Name')
        self.AttendanceReportTable.heading('Department', text='Department')
        self.AttendanceReportTable.heading('Time', text='Time')
        self.AttendanceReportTable.heading('Date', text='Date')
        self.AttendanceReportTable.heading('Attendance', text='Attendance')

        self.AttendanceReportTable['show'] = 'headings'

        self.AttendanceReportTable.column('Id', width=100)
        self.AttendanceReportTable.column('Roll', width=100)
        self.AttendanceReportTable.column('Name', width=100)
        self.AttendanceReportTable.column('Department', width=100)
        self.AttendanceReportTable.column('Time', width=100)
        self.AttendanceReportTable.column('Date', width=100)
        self.AttendanceReportTable.column('Attendance', width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind('<ButtonRelease>',self.get_cursor)

        # ==================== Fetch Data ====================

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert('', END, values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open CSV', filetypes=(('CSV File','*csv'), ('AL1 File','*.*')), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=',')
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror('No Data','No Data To Export',parent=self.root)
                return False
            fl = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Open CSV', filetypes=(('CSV File','*csv'), ('AL1 File','*.*')), parent=self.root)
            with open(fl,mode='w',newline='') as myfile:
                exp_write = csv.writer(myfile, delimiter= ',')
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo('Data Export','Your Data Exported To'+os.path.basename(fl)+'Successfully')

        except EXCEPTION as es:
            messagebox.showerror('Error',f'Due To :{str(es)}',parent=self.root)

    # Get Cursor
    def get_cursor(self, event=''):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    # Reset

    def reset_data(self):
        self.var_atten_id.set('')
        self.var_atten_roll.set('')
        self.var_atten_name.set('')
        self.var_atten_dep.set('')
        self.var_atten_time.set('')
        self.var_atten_date.set('')
        self.var_atten_attendance.set('')


if __name__ == '__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop()