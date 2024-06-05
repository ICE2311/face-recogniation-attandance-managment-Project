import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance
from developr import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x790+0+0')
        self.root.title('Face Recognition System')

        # First Image
        img = Image.open(r'Face Images\college_images\BestFacialRecognition.jpg')
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x = 0,y=0,width = 500,height = 130)

        # Second Image
        img1 = Image.open(r'Face Images\college_images\facialrecognition.png')
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r'Face Images\college_images\images.jpg')
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open(r'Face Images\college_images\wp2551980.jpg')
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img,text='Face Recognition Attendance System',font = ('times new roman',35,'bold'),bg = 'white',fg = 'red')
        title_lbl.place(x = 0, y = 0, width = 1530,height = 45)

        # Student Button
        img4 = Image.open(r'Face Images\college_images\gettyimages-1022573162.jpg')
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details,cursor = 'hand2')
        b1.place(x = 200, y = 100, width = 220, height = 220)

        b1_1 = Button(bg_img, text = 'Students Details', command=self.student_details, cursor='hand2',font = ('times new roman',15,'bold'),bg = 'darkblue',fg = 'white')
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect Face Button
        img5 = Image.open(r'Face Images\college_images\face_detector1.jpg')
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor='hand2', command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text='Face Detector', cursor='hand2', command=self.face_data, font=('times new roman', 15, 'bold'),bg='darkblue', fg='white')
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance Face Button
        img6 = Image.open(r'Face Images\college_images\attendance.jpg')
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor='hand2', command=self.Attendance_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text='Attendance', cursor='hand2', command=self.Attendance_data, font=('times new roman', 15, 'bold'), bg='darkblue',fg='white')
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help Desk Button
        img7 = Image.open(r'Face Images\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg')
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor='hand2', command=self.Help)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text='Help Desk', cursor='hand2', command=self.Help, font=('times new roman', 15, 'bold'), bg='darkblue',fg='white')
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train Face Data Button
        img8 = Image.open(r'Face Images\college_images\Train.jpg')
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor='hand2', command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text='Train Data', cursor='hand2', command=self.train_data, font=('times new roman', 15, 'bold'), bg='darkblue',fg='white')
        b1_1.place(x=200, y=580, width=220, height=40)

        # Face Photo Button
        img9 = Image.open(r'Face Images\college_images\opencv_face_reco_more_data.jpg')
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor='hand2', command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text='Photos', cursor='hand2', command=self.open_img, font=('times new roman', 15, 'bold'), bg='darkblue',fg='white')
        b1_1.place(x=500, y=580, width=220, height=40)

        # Developer Button
        img10 = Image.open(r'Face Images\college_images\Team-Management-Software-Development.jpg')
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor='hand2', command=self.developer)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text='Developer', cursor='hand2', command=self.developer, font=('times new roman', 15, 'bold'), bg='darkblue',fg='white')
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit Button
        img11 = Image.open(r'Face Images\college_images\exit.jpg')
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor='hand2', command=self.Iexit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text='Exit', cursor='hand2', command=self.Iexit, font=('times new roman', 15, 'bold'), bg='darkblue',fg='white')
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile('data')

    def Iexit(self):
        self.Iexit = tkinter.messagebox.askyesno('Face Recognition', 'Are You Sure You Want To Exit This Project', parent= self.root)
        if self.Iexit > 0:
            self.root.destroy()
        else:
            return


    # ==================== Function Button ===================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def Attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def Help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
