from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x790+0+0')
        self.root.title('Face Recognition System')

        title_lbl = Label(self.root, text='Help Desk', font=('times new roman', 35, 'bold'), bg='white',fg='blue')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r'Face Images\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg')
        img_top = img_top.resize((1530, 750), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=55, width=1530, height=750)

        dev_label = Label(f_label, text='Email : sush.bft@gmail.com', font=('times new roman', 19, 'bold'), fg='blue',bg='white')
        dev_label.place(x=590, y=220)


if __name__ == '__main__':
    root = Tk()
    obj = Help(root)
    root.mainloop()