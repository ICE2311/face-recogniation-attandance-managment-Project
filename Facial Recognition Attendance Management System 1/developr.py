from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x790+0+0')
        self.root.title('Face Recognition System')

        title_lbl = Label(self.root, text='Developer', font=('times new roman', 35, 'bold'), bg='white',fg='blue')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r'Face Images\college_images\dev.jpg')
        img_top = img_top.resize((1530, 750), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=55, width=1530, height=750)

        # Frame
        main_frame = Frame(f_label, bd=2, bg='white')
        main_frame.place(x=980, y=0, width=500, height=600)

        img_top1 = Image.open(r'Face Images\college_images\sush.jpg')
        img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_label = Label(main_frame, image=self.photoimg_top1)
        f_label.place(x=300, y=0, width=200, height=200)

        # Developer Info
        dev_label = Label(main_frame, text='Hello my name is Sushant', font=('times new roman', 19, 'bold'), fg='blue', bg='white')
        dev_label.place(x=0, y=5)

        dev_label=Label(main_frame, text='I am a Developer', font=('times new roman', 20, 'bold'), fg='blue', bg='white')
        dev_label.place(x=0, y=40)

        img2 = Image.open(r'Face Images\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg')
        img2 = img2.resize((500, 390), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label = Label(main_frame, image=self.photoimg2)
        f_label.place(x=0, y=210, width=500, height=390)


if __name__ == '__main__':
    root = Tk()
    obj = Developer(root)
    root.mainloop()