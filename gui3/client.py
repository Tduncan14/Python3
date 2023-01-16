#client side gui chatroom

import tkinter, threading,socket
from tkinter import DISABLED

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
#Create frames

info_frame = tkinter.Frame(root, bg=black)
output_frame = tkinter.Frame(root,bg=black)
input_frame = tkinter.Frame(root,bg=black)


info_frame.pack()

output_frame.pack(pady=10)



#Info frame layout
name_label = tkinter.Label(info_frame, text="Client Name :", font=my_font, fg=light_green, bg=black)
name_entry = tkinter.Entry(info_frame, borderwidth = 3, font=my_font)
ip_label = tkinter.Label(info_frame, text="Host Ip :", font=my_font, fg=light_green, bg=black)
ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)

port_label = tkinter.Label(info_frame, text="Port Num:" , font=my_font, fg=light_green, bg=black)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)

connect_button = tkinter.Button(info_frame,text="Connect", font=my_font, bg=light_green,borderwidth=5,width=10)
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=my_font, bg=light_green, borderwidth=5,width=10, state=DISABLED)


name_label.grid(row =0, column = 0, padx=2, pady=10)
name_entry.grid(row =0, column = 1, padx=2, pady=10)
port_label.grid(row =0, column = 2, padx=2, pady=10)
port_entry.grid(row =0, column = 3, padx=2, pady=10)
ip_label.grid(row =1, column = 0, padx=2, pady=5)
ip_entry.grid(row =1, column = 1, padx=2, pady=10)

connect_button.grid(row=1,column=2,padx=4,pady=5)
disconnect_button.grid(row=1,column=3,padx=4,pady=5)









#Run the root windows mainloop()

root.mainloop()