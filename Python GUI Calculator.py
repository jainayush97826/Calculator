from tkinter import*

me=Tk()
me.geometry("276x460")
me.title("CALCULATOR")
melabel = Label(me,text="CALCULATOR",bg='yellow',font=("courier",31,'bold'),relief=SUNKEN,bd=1)
melabel.pack(side=TOP)
me.config(background='Black')

textin=StringVar()
operator=""

def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''
def equlbut():
     global operator
     mod=str(eval(operator))
     textin.set(mod)
     operator=''
def clrbut():
     textin.set('')

     
metext=Entry(me,font=("Courier New",20,'bold'),textvar=textin,width=15,bd=7,bg='Silver',relief=SUNKEN)
metext.pack()

but1=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but1.place(x=10,y=170)

but2=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but2.place(x=10,y=240)

but3=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but3.place(x=10,y=310)

but4=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but4.place(x=75,y=170)

but5=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=240)

but6=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but6.place(x=75,y=310)

but7=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but7.place(x=140,y=170)

but8=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but8.place(x=140,y=240)

but9=Button(me,padx=14,pady=14,bd=4,bg='orange',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but9.place(x=140,y=310)

but0=Button(me,padx=47,pady=14,bd=4,bg='yellow',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=380)

butdot=Button(me,padx=14,pady=14,bd=4,bg='yellow',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=140,y=380)

butpl=Button(me,padx=14,pady=14,bd=4,bg='yellow',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butpl.place(x=205,y=170)

butsub=Button(me,padx=14,pady=14,bd=4,bg='yellow',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=240)

butml=Button(me,padx=14,pady=14,bd=4,bg='yellow',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butml.place(x=205,y=310)

butdiv=Button(me,padx=14,pady=14,bd=4,bg='yellow',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=100)

butclear=Button(me,padx=44,pady=14,bd=4,bg='light green',text="AC",command=clrbut,font=("Courier New",14,'bold'))
butclear.place(x=10,y=100)

butmod=Button(me,padx=14,pady=14,bd=4,bg='light green',text="%",command=lambda:clickbut("%"),font=("Courier New",16,'bold'))
butmod.place(x=140,y=100)

butequal=Button(me,padx=14,pady=14,bd=4,bg='yellow',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=205,y=380)

me.mainloop()
