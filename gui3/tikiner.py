#Tkiner intro
import tkinter
from tkinter import BOTH, StringVar


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
stored_message_color = '#5A5A5A'
root.config(bg=root_color)



#define function



# Define GUI Layout
#Define frame 
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root,bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10,pady=(0,10),fill=BOTH, expand = True)


#Define Widgets

message_entry = tkinter.Entry(input_frame, text="Enter a message", width = 30)
send_button = tkinter.Button(input_frame, text="Send")

message_entry.grid(row=0,column=0, columnspan=3,padx=10, pady=10)
send_button.grid(row=0,rowspan = 2,column=3,padx=10,pady=10,ipadx=20,ipady=5)



text_color = StringVar()
text_color.set('#ff0000')
red_button = tkinter.Radiobutton(input_frame, text="Red", variable=text_color,value="#ff0000",bg=input_color)
green_button = tkinter.Radiobutton(input_frame, text="Green", variable=text_color,value="#00ff00",bg=input_color)
blue_button = tkinter.Radiobutton(input_frame, text="Blue", variable=text_color,value="#0000ff",bg=input_color)

# grid system

red_button.grid(row=1,column=0)
green_button.grid(row=1,column=1)
blue_button.grid(row=1,column=2)


output_label = tkinter.Label(output_frame,text='--- Stored Messages ---', fg=stored_message_color, bg=output_color, font=('Helevtica bold',18))
output_label.pack(pady=15)


#run the roow window's mainloop

root.mainloop()