import tkinter
from tkinter import *

from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
#import numpy as np
#import matplotlib.pyplot as plt
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os, sys

img= "global"
def open_imag():
    top.filename = filedialog.askopenfilename(initialdir="/User/ismilsyspriede", title="Select Image",
                                              filetypes=(("png files", (".png")), ("JPG files",(".JPG")), ("All files", "*.*")));
    inclusion = top.filename
    Entry.insert(E1, 0, inclusion)
    print(inclusion)

def save_imag():
    global img
    file= filedialog.asksaveasfile(mode='w',defaultextension= ".png", filetypes=(("png files", (".png")), ("JPG files",(".JPG")), ("All files", "*.*")))
    if file:
        path= os.path.abspath(file.name)
        img.save(path)
    print("Hello")

# read_entry will load a picture and performance loop to read Red scale of every pixel. If the pixel value is inside
# the threshold value of one of the inclusions, it will colored the pixel with a specific color
def read_entry():
    global img  ;   #global variable which hold the manipulated image

    inclusion = top.filename
    Entry.insert(E4, 0, inclusion)
    print(inclusion)
    original = Image.open(inclusion)
    img = Image.open(inclusion)
    img = img.convert('RGB')   # convert the image to RGB format

    width = img.size[0]
    height = img.size[1]

    for y in range(0, height):    # loop to go scan all pixel
        row = " "
        for x in range(0, width):
            rgb = img.getpixel((x, y))
            R, G, B = rgb
            # print (R)
            if (R < 99) and (R > 81):  # threshold value for Graphite
                point = ImageDraw.Draw(img)
                point.point((x, y), fill="rgb(200,0,0)")  # red= Graphite
            elif (R < 135) and (R > 98):  # threshold value for Troilite
                point = ImageDraw.Draw(img)
                point.point((x, y), fill="rgb(0,0,200)")  # blue= Troilite
            elif (R < 135) and (R > 134):  # threshold value for Schreibersite
                point = ImageDraw.Draw(img)
                point.point((x, y), fill="rgb(0,200,0)")  # green= Schreibersite
            elif (R < 155) and (R > 134):    # threshold value for Nickel-Iron allow
                point = ImageDraw.Draw(img)
                point.point((x, y), fill="rgb(200,200,0)")  # yellow= Nickel-Iron allow
    newOriginal = original.resize((300, 300))  # making a copy to display image
    newImag = img.resize((300, 300))
    photo = ImageTk.PhotoImage(newOriginal)
    photoInclusion = ImageTk.PhotoImage(newImag)
    lab= Label(top, image=photo)
    lab.image = photo
    lab.place(x=400, y=10)
    lab1 = Label(top, image=photoInclusion)
    lab1.image = photoInclusion
    lab1.place(x=800, y=10)




top = tkinter.Tk()
top.title("Meteorites inclusion")
top.geometry('1500x500')         # this method creates the dimensions of the Tk Widget
top.resizable(width= TRUE, height= TRUE)
L1 = Label(top, text="Name of the Meteorite sample",).grid(row=0,column=1)
L2 = Label(top, text="Inclusions: ",).grid(row=1,column=0)

L3 = Label(top, text="Graphite ",bg="red").grid(row=7,column=0)
L4 = Label(top, text="Troilite ", bg="blue").grid(row=8,column=0)
L5 = Label(top, text="Schreibersite ",bg="green").grid(row=9,column=0)
L5 = Label(top, text="Nickel-Iron alloy ",bg="yellow").grid(row=10,column=0)

# L4 = Label(top, text="Answer",).grid(row=4,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)


B=Button(top, text ="Submit",command= read_entry).grid(row=5,column=1,)
B1= Button(top, text= "Open", command = open_imag).grid(row=1, column=2)
B2=Button(top, text ="Reset").grid(row=5,column=2,)
B3=Button(top, text ="Save", command=save_imag).grid(row=5,column=3,)






top.mainloop()

