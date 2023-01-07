#Tkiner intro
import tkinter

#Define the window


root = tkinter.Tk()
root.title("Let's chat")
root.iconbitmap('gui3/blue.ico')
root.geometry('400x600')
root.resizable(0,0)

#define the coolrs
root_color = "#535657"
input_color = "#46f4f6"
output_color = '#dee7e7'
root.config(bg=root_color)



#define function



# Define GUI Layout
#Define frame 
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root,bg=output_color)
input_frame.pack()



#run the roow window's mainloop

root.mainloop()