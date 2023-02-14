from tkinter import *
from random import choice




#runs the window for the tk
App = Tk()


#the title of the of app interface
App.title='Choices'
App.geometry('240x100')


# the input for the gui
inp = Entry(App)

#you needed to run the function of the widget
inp.grid(row = 0 , column = 0 , columnspan=2, padx=20, pady=5)


def pick():
    INP = (inp.get()).split(',')
    msg = Label(App,text=choice(INP), font=('Courier,12'))
    msg.grid(row=0, column=20, padx=20,pady=5 )
    

    if QuitB['state'] == DISABLED:
        QuitB['state'] = NORMAL

B = Button(  text='show', command=pick,background='white',foreground='black')
B.grid()


QuitB = Button(App,text='cancel',command=App.quit,state=DISABLED,background='blue',foreground='white')
QuitB.grid(row = 1, column = 1, padx=20,pady=5)



App.mainloop()