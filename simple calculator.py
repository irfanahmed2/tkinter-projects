
import math
from tkinter import *


root =  Tk()
root.title("Simple Calculator")
#e = entey variable 
e = Entry(root,width=35, borderwidth=5)
# mapping buttons
e.grid(row=0, column=0,columnspan=3,pady=10,padx=10)


#fuction to work numbers
def button_click(number):#<-- passing parameters
    current=e.get()
    e.delete(0,END)
    
    e.insert(0,str(current)+str(number))
# fuction for clear button    
def button_clear():
    e.delete(0,END)
    

#fuction for add button
def button_add():
    first_number=e.get()# return the text
    global f_num   #creating global variable
    global math
    math = 'addition'
    f_num = int(first_number) #converting 1no into integer & assign f_num to first no    
    e.delete(0,END)# to clean the screen
    
    
def button_substract():
    first_number=e.get()# return the text
    global f_num   #creating global variable
    global math
    math = 'substract'
    f_num = int(first_number) #converting 1no into integer & assign f_num to first no    
    e.delete(0,END)
    return


def button_multiply():
    first_number=e.get()# return the text
    global f_num   #creating global variable
    global math
    math = 'multiply'
    f_num = int(first_number) #converting 1no into integer & assign f_num to first no    
    e.delete(0,END)



def button_divide():
    first_number=e.get()# return the text
    global f_num   #creating global variable
    global math
    math = 'divide'
    f_num = int(first_number) #converting 1no into integer & assign f_num to first no    
    e.delete(0,END) 
  
def button_equal1():
    second_number=e.get()  
    e.delete(0,END)
    if math == 'addition':
      e.insert(0, f_num + int(second_number))
      
    if math == 'substract':
      e.insert(0, f_num - int(second_number))
      
    if math == 'multiply':
      e.insert(0, f_num * int(second_number))
      
    if math == 'divide':
      e.insert(0, f_num / int(second_number))      
    
# labeling button 
button_1=Button(root,text='1',padx=40,pady=20 ,command=lambda: button_click(1)) #lambda is use for () parameter to work no 1
button_2=Button(root,text='2',padx=40,pady=20 ,command=lambda: button_click(2))
button_3=Button(root,text='3',padx=40,pady=20 ,command=lambda: button_click(3))
button_4=Button(root,text='4',padx=40,pady=20 ,command=lambda: button_click(4))
button_5=Button(root,text='5',padx=40,pady=20 ,command=lambda: button_click(5))
button_6=Button(root,text='6',padx=40,pady=20 ,command=lambda: button_click(6))
button_7=Button(root,text='7',padx=40,pady=20 ,command=lambda: button_click(7))
button_8=Button(root,text='8',padx=40,pady=20 ,command=lambda: button_click(8))
button_9=Button(root,text='9',padx=40,pady=20 ,command=lambda: button_click(9))
button_0=Button(root,text='0',padx=40,pady=20 ,command=lambda: button_click(0))
button_add=Button(root,text='+',padx=40,pady=20,command=button_add)
button_equal1=Button(root,text='=',padx=40,pady=20,command= button_equal1)
button_clear1=Button(root,text='Clear',padx=40,pady=20,command= button_clear)

button_substract=Button(root,text='-',padx=40,pady=20,command=button_substract)
button_multiply=Button(root,text='*',padx=40,pady=20,command=button_multiply)
button_divide=Button(root,text='/',padx=40,pady=20,command=button_divide)


#Displaying button on scree0
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear1.grid(row=6, column=1)
button_add.grid(row=4, column=2)
button_equal1.grid(row=6, column=2 )

button_substract.grid(row=5, column=2)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=5, column=0)


root.mainloop()

