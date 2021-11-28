import socket
from tkinter import *

def send(entry,listbox):
    message = entry.get()
    if len(message)!=0:
        listbox.insert("end", "Me : " + message)
        entry.delete(0, END)
        s.send(bytes(message, "utf-8"))
        recieve(listbox)

def recieve(listbox):
    message = s.recv(50)
    listbox.insert('end',"Server : "+message.decode('utf-8'))

root = Tk()
root.title("ChatApp(Client)")
root.geometry('330x350')
root.resizable(False,False)
root.config(bg="black")


serverlabel = Label(root,text='Client : ',bg='black',fg='white',font=('Calibre',12,'normal'))
serverlabel.place(relx=0.0,rely=1.0,anchor='sw')

entry = Entry(width=15,font=('Calibre',19,'normal'))
entry.pack(side=BOTTOM)

listbox = Listbox(root,height=12,width=29,selectmode=SINGLE,bg="grey",activestyle="dotbox",font='Helvetica',fg="yellow")
listbox.pack()

button = Button(root,text="Send",height=10,width=20,bg="orange",command= lambda:send(entry,listbox))
button.pack(side=BOTTOM)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
Port = 12345

s.connect((HOST_NAME,Port))

root.mainloop()
# while True:
#     message = ''
#     while True:
#         msg = s.recv(10)
#         if len(msg)<=0:
#             break
#         message+=msg.decode('utf-8')
#
#     if len(message):
#         print(message)