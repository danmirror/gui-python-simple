# Import module 
from tkinter import *

from PIL import ImageTk, Image

root = Tk()
# Adjust size 
root.geometry("800x600") 

# Add image file 
canv = Canvas(root, width=800, height=600, bg='white')
canv.grid(row=2, column=3)

image1 = Image.open("bg.png")
image1 = image1.resize((600, 450), Image.ANTIALIAS)

test = ImageTk.PhotoImage(image1)
canv.create_image(0, 0, anchor=NW, image=test)


label1 = Label( root,text='lower left') 
label1.place(x = 100, y = 0) 

# Execute tkinter 
root.mainloop() 
