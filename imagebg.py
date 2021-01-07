# Import module 
from tkinter import * 
from PIL import ImageTk, Image

def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label

def data():
   data = input_data.get()
   print(data)
   label2.config(text=data)

root = Tk()

# Adjust size 
root.geometry("800x600") 
image1 = Image.open("bg.png")
image1 = image1.resize((600, 450), Image.ANTIALIAS)

test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)


label2 = Label( root,text='data masuklan') 
label2.place(x = 300, y = 200) 

# button = Button(root, 
#                    text="QUIT", 
#                    fg="red",
#                    command=quit)

input_data = Entry(root, bd =5)
input_data.place(x=350, y=400)
button = Button(root, 
                   text="SEND", 
                   fg="red",
                   command=data)

button.place(x = 500, y = 400) 

# kalo set lebar  & tinggi
make_label(root, 10, 10, 100, 40, text='xxx')
make_label(root, 30, 40, 10, 30, text='yyy', background='blue')


root.mainloop()
