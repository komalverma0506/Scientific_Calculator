from tkinter import *
from math import *

root = Tk()

exp = ''

def press(num):
    global exp
    exp = exp+num 
    inp.set(exp)

def result():
    global exp
    
    try:
        exp = str(eval(exp))
    except:
        exp = 'Error'
       
    inp.set(exp)

def delete():
    global exp
    exp = ''
    inp.set(exp)
    
def del1():
    global exp
    exp = exp[:-1]
    inp.set(exp)
    
def percent():
    global exp
    exp = str(eval(exp)*100)
    inp.set(exp)

def angle():
    global exp
    
    try:
        exp = str(degrees(eval(exp))) 
    except:
        exp = 'Error'
       
    inp.set(exp)
    
inp = StringVar()
inp.set('')

ent = Entry(root,width=40,textvariable=inp)
ent.grid(row=0,columnspan=3)

bt1 = Button(root,text='1',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('1'))
bt1.grid(row=1,column=0)

bt2 = Button(root,text='2',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('2'))
bt2.grid(row=1,column=1)

bt3 = Button(root,text='3',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('3'))
bt3.grid(row=1,column=2)

bt4 = Button(root,text='4',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('4'))
bt4.grid(row=2,column=0)

bt5 = Button(root,text='5',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('5'))
bt5.grid(row=2,column=1)

bt6 = Button(root,text='6',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('6'))
bt6.grid(row=2,column=2)

bt7 = Button(root,text='7',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('7'))
bt7.grid(row=3,column=0)

bt8 = Button(root,text='8',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('8'))
bt8.grid(row=3,column=1)

bt9 = Button(root,text='9',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('9'))
bt9.grid(row=3,column=2)

bt0 = Button(root,text='0',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('0'))
bt0.grid(row=4,column=1)

bt = Button(root,text='.',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('.'))
bt.grid(row=4,column=0)

equal = Button(root,text='=',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = result)
equal.grid(row=4,column=2)

clear = Button(root,text='c',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = delete)
clear.grid(row=5,column=0)

cross = Button(root,text='x',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = del1)
cross.grid(row=5,column=1)

div = Button(root,text='/',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('/'))
div.grid(row=5,column=2)

add = Button(root,text='+',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('+'))
add.grid(row=6,column=0)

sub = Button(root,text='-',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('-'))
sub.grid(row=6,column=1)

mul = Button(root,text='*',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('*'))
mul.grid(row=6,column=2)

pi = Button(root,text='π',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('3.141592653589793238'))
pi.grid(row=7,column=0)

sin = Button(root,text='asin',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('asin'))
sin.grid(row=7,column=1)

cos = Button(root,text='acos',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('acos'))
cos.grid(row=7,column=2)

sqrt = Button(root,text='√',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('**0.5'))
sqrt.grid(row=8,column=0)

per = Button(root,text='%',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = percent)
per.grid(row=8,column=1)

tan = Button(root,text='atan',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('atan'))
tan.grid(row=8,column=2)

br1 = Button(root,text='(',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press('('))
br1.grid(row=9,column=0)

br2 = Button(root,text=')',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = lambda:press(')'))
br2.grid(row=9,column=1)

degree = Button(root,text='=°',height=2,width=10,font=('Times',10,'bold'),bg='black',fg='lightblue',relief='sunken',command = angle)
degree.grid(row=9,column=2)


root.title('Calculator')
root.mainloop()
