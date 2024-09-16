from tkinter import*

#Segunda practica añadimos el objeto Button y Entry
#Se le añadio una funcion al evento click del objeto Button que imprime lo que esta en el Entry
window= Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I Am a Label",font=("Arial",24,"bold"))
my_label.pack()

my_label["text"]="New Text"
my_label.config(text="New Text")

#Button 

def button_clicked():
    print("I got clicked")
    new_text =input.get()
    my_label.config(text=new_text)
    #Mi manera
    #my_label.config(text=input.get())

button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry
input= Entry(width=10)
input.pack()
input.get()
print(input.get())



window.mainloop()