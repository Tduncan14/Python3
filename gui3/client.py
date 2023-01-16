#client side gui chatroom

import tkinter, threading,socket


#define the root window


root = tkinter.Tk()
root.title('Client Chat')
root.iconbitmap("gui3\message.ico")
root.geometry('600x600')
root.resizable(0,0)


#define the fonts and collors 


my_font = ('SimSun',14)
black="#010101"
light_green="#1fc742"
root.config(bg=black)


#Define Functions



#Define Gui Layout

info_frame = tkinter.Frame(root, bg=black)
output_frame = tkinter.Frame(root,bg=black)
input_frame = tkinter.Frame(root,bg=black)

#Run the root windows mainloop()

root.mainloop()