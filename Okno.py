import tkinter
import tkinter.messagebox


okno= tkinter.Tk()

def helloCallBack():
    tkinter.messagebox.showinfo("Začni igro!", "Oprostite, nekaj je šlo narobe!")

b= tkinter.Button(okno, text="Začni igro!", command = helloCallBack)

b.pack()
okno.mainloop()





