import tkinter
from tkinter import *
from tkinter import ttk



lol = Tk()
lol.geometry('1020x1050')# grandeur de la fenèetre



lol.title('Dating Simutor') #titre de la page


lab = Label(lol, text= 'Your Girlfriend Zhiao') #mettre du text
lab.place(x=450, y=10)


Label(lol, text='entrer').place(x=0, y=1000)# boite de texte
e1 = Entry(lol, width=138)

e1.place(x=50, y=1000)

button = Button(lol, text='send', width=15, command=lol.destroy).place(x=885, y=1000)#button



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









