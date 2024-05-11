import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import StringVar





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

wo











lol = Tk()
lol.geometry('1020x1050')# grandeur de la fenèetre



lol.title('Dating Simulator') #titre de la page


nom = Label(lol, text= 'Your crush '+nom2) #mettre du text
nom.place(x=450, y=10)


Label(lol, text='entrer').place(x=0, y=1000)# boite de texte
e1 = Entry(lol, width=138)

e1.place(x=50, y=1000)

send = Button(lol, text='send', width=15, command=lol.destroy).place(x=885, y=1000)#button



scrollbar = Scrollbar(lol)               #scrollBar
scrollbar.pack(side="right", fill="y")
mylist = Listbox(lol, yscrollcommand=scrollbar.set)


    

mylist.place(width=1000, height=950, y=50)    #  list box
scrollbar.config(command=mylist.yview)

progress = ttk.Progressbar(lol, orient="horizontal", length=300, mode="determinate") #progresse bar
progress.place(x=700, y=10)


msg = Message(lol, text='Current Day: ', width=100)

msg.config(bg='red')
msg.place(y=10)


lol.mainloop()









