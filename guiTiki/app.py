# from tkinter import *
# from random import randint


# #creates an tkinter window
# App = Tk()
# App.title('Random Generator')
# #builds the web application
# App.geometry('350x250')


# Display = Label(App, text="Application Window")
# Display.pack()


# def show_msg():
#     msg = Label(App,text=randint(1,100))
#     msg.pack()



# B = Button(App,text = 'Generateo', command=show_msg)
# B.pack()

# # shows the python window
# App.mainloop()

from tkinter import *
from random import choices


App = Tk()
App.title('Element picker')
App.geometry('350x100')



inp = Entry(App)
inp.pack()


def show():
    Inp = inp.get()
    msg = Label(App, text=Inp)
    msg.pack()

B = Button(App, text="Show", command=show)
B.pack()

App.mainloop()