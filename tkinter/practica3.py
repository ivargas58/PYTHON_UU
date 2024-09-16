from tkinter import*

'''
Existen 3 metodos para desplegar nuestros objetos en el window pack,place,grid
Para pack se debe desplegar en el orden que quieres que priorice y ademas identicar con left,right,botom,top 
Para place se utiliza la ubicacion en pixeles("OJO eso basado en el tamaño de tu window")
Para grid se despliega en el window utilizando colum y row. Colum = X y Row = Y

'''
window= Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I Am a Label",font=("Arial",24,"bold"))
my_label.config(text="new text")
#my_label.place(x=100, y=200)
my_label.grid(column=0,row=0)

#Button
button = Button(text="Button")
button.grid(column=1,row=2)

button1 = Button(text="New Button")
button1.grid(column=2,row=0)
#Entry 
input= Entry(width=10)
input.grid(column=4,row=3)


window.mainloop()