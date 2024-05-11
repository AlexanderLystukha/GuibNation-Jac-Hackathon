import tkinter
from tkinter import *




lol = Tk()
lol.geometry('1920x1250')# grandeur de la fenèetre



lol.title('Dating Simutor') #titre de la page


#lab = Label(lol, text= 'hello').grid(row=1) #mettre du text
#lab.pack()


Label(lol, text='entrer').place(x=10, y=1200)# boite de texte
e1 = Entry(lol, width=50)
#e1.grid(row=9, column=1)
e1.place(x=50, y=1200)

button = Button(lol, text='send', width=25, command=lol.destroy).place(x=1000, y=1200)#button



scrollbar = Scrollbar(lol)
scrollbar.place(x=200, y=200)
mylist = Listbox(lol, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
    
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)






lol.mainloop()









