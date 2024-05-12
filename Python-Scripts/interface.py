import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import StringVar
import AI
import Functionality



tlol = Tk()
tlol.title('Dating Simulator')
tlol.geometry('300x150')
tuto = Label(tlol, text= 'Welcome to rizzler university, your goal?\n rizz up the ai.\n you have 5 days to get a date gl')
tuto.pack()

ok = Button(tlol, text='OK', width=15, command=tlol.destroy).place(x=95, y=110)



tlol.mainloop()


slol = Tk()
slol.title('Dating Simulator')
slol.geometry('300x250')
msg='Choose the name for your crush!'
choix = Label(slol, text= msg)
choix.pack()

Label(slol, text='Name').place(x=30, y=50)
nom= StringVar()
e2 = Entry(slol, width=25, textvariable=nom)

e2.place(x=80, y=50)

nom2=''
caractere=1
def getNom():
    global nom2
    nom2 = nom.get()
    global caractere
    caractere = carac.get()
    slol.destroy()
    
carac = IntVar()
Checkbutton(slol, text='Random', variable=carac, onvalue=1).place(x=100, y=100)
Checkbutton(slol, text='Emo/Shy', variable=carac, onvalue= 2).place(x=100,y=125)
Checkbutton(slol, text='Extrovert', variable=carac, onvalue=3).place(x=100, y=150)
Checkbutton(slol, text='distant/affectionate',variable=carac, onvalue= 4).place(x=100, y=175)




nameb= Button(slol, text='Ready', width=15, command=getNom).place(x=95, y=210)


slol.mainloop()




def send():
    global txt2
    txt2 = txt.get()
    wordList = txt2.split()
    yo = ''
    counter = 1

    for x in wordList:
        if (counter % 5 == 0):
            Box2.insert(END, yo)
            Box.insert(END,'')
            yo = ''
        else:
            yo += x + ' '
        counter += 1
    if (counter % 5 != 0):
        Box2.insert(END, yo)

    #Box2.insert(END, txt2)
    Box.insert(END,'')
    Box.insert(END,'')

    Box.insert(END,AI.AIPrint(txt2))
    Box2.insert(END,'')
    Box2.insert(END,'')


    Functionality.LovePointsFinder
    barup['value']=Functionality.LovePoints
    lol.update_idletasks()
    





    










lol = Tk()
lol.geometry('1020x800')# grandeur de la fenèetre
txt2= ''
txt = StringVar()

lol.title('Dating Simulator') #titre de la page


nom = Label(lol, text= 'Your crush '+nom2) #mettre du text
nom.place(x=450, y=10)


Label(lol, text='entrer').place(x=0, y=700)# boite de texte
e1 = Entry(lol, width=138, textvariable=txt)

e1.place(x=50, y=700)

send = Button(lol, text='send', width=15, command=send).place(x=885, y=700)#button



scrollbar = Scrollbar(lol)               #scrollBar
scrollbar.pack(side="right", fill="y")
Box = Listbox(lol, yscrollcommand=scrollbar.set)
Box2 =Listbox(lol, yscrollcommand= scrollbar.set)

    

Box.place(width=500, height=650, y=50)    #  list box
Box2.place(width=500, height=650, y=50, x=500)
scrollbar.config(command=Box.yview)
scrollbar.config(command= Box2.yview)




barup = ttk.Progressbar(lol, orient="horizontal", length=300, mode="determinate") #progresse bar
barup.place(x=700, y=10)

day= 'Monday'


d=0

def days():
    global msg
    global day
    global d
    d= d+ 1
    
    match d:
        case 1:
            day = 'Monday    '
            msg = Message(lol, text=f'Current Day: {day}', width=300)
        case 2:
            day='Tuesday   '
            msg = Message(lol, text=f'Current Day: {day}', width=300)
        case 3:
            day='Wednesday '
            msg = Message(lol, text=f'Current Day: {day}', width=300)
        case 4:
            day= 'Thursday  '   
            msg = Message(lol, text=f'Current Day: {day}', width=300)
        case 5:
            day='Friday    '
            msg = Message(lol, text=f'Current Day: {day}', width=300)
        case _:
            if (Functionality.LovePoints>99):
                lol.destroy()
            else:
                lol.destroy()
    msg.config(bg='red')
    msg.place(y=10)



days()




end = Button(lol, text='End day', width=15, command=days).place(x=885 ,y=730)



lol.mainloop()









