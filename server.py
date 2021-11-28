import socket
from tkinter import *


def send(entry,listbox):
    message = entry.get()
    listbox.insert("end","Server : "+message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))

def recieve(listbox):
    msgrecv = client.recv(50)
    listbox.insert('end',HOST_NAME+" : "+msgrecv.decode('utf-8'))

root = Tk()
root.title("ChatApp(Server)")
root.geometry('330x350')
root.resizable(False,False)
root.config(bg="black")

serverlabel = Label(root,text='Server : ',bg='black',fg='white',font=('Calibre',12,'normal'))
serverlabel.place(relx=0.0,rely=1.0,anchor='sw')

entry = Entry(width=15,font=('Calibre',19,'normal'),text="Server: ")
entry.pack(side=BOTTOM)

listbox = Listbox(root,height=12,width=29,selectmode=SINGLE,bg="grey",activestyle="dotbox",font='Helvetica',fg="yellow")
listbox.pack()

button = Button(root,text="Send",width=22,bg="orange",command= lambda:send(entry,listbox))
button.pack(side=RIGHT)

buttonr = Button(root,text="Recieve",width=22,bg="green",command= lambda:recieve(listbox))
buttonr.pack(side=LEFT)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
Port = 12345

s.bind((HOST_NAME,Port))

s.listen(4)
client,address = s.accept()
print(HOST_NAME + " is connected to the address ")
print(address)

root.mainloop()
