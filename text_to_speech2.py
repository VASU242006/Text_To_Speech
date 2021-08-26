from tkinter import *
import tkinter as tk
import os

from gtts import gTTS 

from playsound import playsound



def convert_audio():
    
    address_info = address.get()
    language = 'hi'
    
    myobj = gTTS(text=address_info, lang=language, slow=False)
    #myobj.save("welcome.mp3") 
    #playsound("welcome.mp3")
    os.system("welcome.mp3")
    
        
    print(address_info)
    
    address_entry.delete(0,END)    

def exit():
    app.destroy() 
#def reset(): 
    #inputEdit.delete("1.0",tk.END)    
    #text.delete(1.0,END) 


app = Tk()

app.geometry("500x500")
app.maxsize(600,600)
app.minsize(600,600)
app.title("Python Text to Audio App")

heading = Label(text="Welcome to Text to Audio App",bg="yellow",fg="magenta",font="10",width="50",height="3")

heading.pack()

address_field = Label(text="The text which u want to hear, PLZ WRITE DOWN....")

address_field.place(x=15,y=70)

address = StringVar()


address_entry = Entry(textvariable=address,width="10")

address_entry.place(x=15,y=100)

btn1 = Button(app,text="Convert to Audio",command=convert_audio,fg="magenta",width="20",height="4",bg="yellow")

btn1.place(x=15,y=140)
# button.pack()

btn2 = Button(app, text='Delete', command=lambda: address_entry.delete(0,END),fg="magenta",width="20",height="4",bg="yellow")
btn2.place(x=200, y=140)
# btn.pack()

btn3 = Button(app , text="Exit",command=exit,fg="magenta",width="20",height="4",bg="yellow")
btn3.place(x=380,y=140)


mainloop()