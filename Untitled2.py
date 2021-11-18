from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
root=Tk()
root.title("Canvas")
root.geometry("500x500")

canvas=Canvas(root,width=590,height=510,bg="white",highlightbackground="lightgray")
inputbox=Entry(root)
inputbox.insert(0,"black")
inputbox.place(relx=0.8,rely=0.9,anchor=CENTER)

img=ImageTk.PhotoImage(Image.open("start_point1.png"))
myimage=canvas.create_image(50,50,image=img)
label=Label(root,text="Colour")
label.place(relx=0.6,rely=0.9,anchor=CENTER)
fill_colour=["Red","blue","green","purple"]
colour_dropdown=ttk.Combobox(root,state="readonly",values=fill_colour,width=10)
colour_dropdown.place(relx=0.8,rely=0.9,anchor=CENTER)

startx=Label(root,text="start x")
startx.place(relx=0.1,rely=0.85,anchor=CENTER)
coordinate_numbers=[10,50,100,80,200,300]
d1=ttk.Combobox(root,state="readonly",values=coordinate_numbers,width=10)
d1.place(relx=0.2,rely=0.9,anchor=CENTER)

starty=Label(root,text="start y")
starty.place(relx=0.3,rely=0.85,anchor=CENTER)
coordinate_numbers2=[30,80,100,80,200,300]
d2=ttk.Combobox(root,state="readonly",values=coordinate_numbers2,width=10)
d2.place(relx=0.4,rely=0.9,anchor=CENTER)

endx=Label(root,text="end x")
endx.place(relx=0.5,rely=0.85,anchor=CENTER)
coordinate_numbers3=[30,80,100,80,200,300]
d3=ttk.Combobox(root,state="readonly",values=coordinate_numbers2,width=10)
d3.place(relx=0.5,rely=0.9,anchor=CENTER)

endy=Label(root,text="end y")
endy.place(relx=0.6,rely=0.85,anchor=CENTER)
coordinate_numbers4=[30,80,100,80,200,300]
d4=ttk.Combobox(root,state="readonly",values=coordinate_numbers4,width=10)
d4.place(relx=0.7,rely=0.9,anchor=CENTER)

direction=""
oldx=50
oldy=50
newx=50
newy=50
def rightdir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
    
def leftdir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx-5
    direction="left"
    draw(direction,oldx,oldy,newx,newy)

def topdir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy-5
    direction="top"
    draw(direction,oldx,oldy,newx,newy)

def downdir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy+5
    direction="down"
    draw(direction,oldx,oldy,newx,newy)
def circle(event):
    oldx=d1.get()
    oldy=d2.get()
    newx=d3.get()
    newy=d4.get()
    keypress='c'
    draw2(keypress,oldx,oldy,newx,newy)
    
def rectangle(event):
    oldx=d1.get()
    oldy=d2.get()
    newx=d3.get()
    newy=d4.get()
    keypress='r'
    draw2(keypress,oldx,oldy,newx,newy)    
    
def draw2(keypress,oldx,oldy,newx,newy):
         
    
    
    
    
def draw(direction,oldx,oldy,newx,newy):
    fill_color=inputbox.get()
    if(direction=="right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        
    if(direction=="left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        
    if(direction=="top"):
        top_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        
    if(direction=="down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    
canvas.pack()
root.bind("<Right>",rightdir)
root.bind("<Left>",leftdir)    
root.bind("<Up>",topdir)
root.bind("<Down>",downdir)

root.mainloop()