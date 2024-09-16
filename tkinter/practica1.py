import tkinter
#Primera practica desplegando el objeto window y un label con la libreria tkinter
window=tkinter.Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)


#Label 
my_label = tkinter.Label(text="Im Am a label", font=("Arial",20,"bold"))
my_label.pack()


window.mainloop()