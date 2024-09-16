#Mile to Kilometers Converter Project
from tkinter import*

#Funcion que hace los calculo del evento click en el objeto Button
def converte():
    miles= float(miles_input.get())
    km= miles *1.609
    kilometer_result.config(text=f'{km}')

#Objeto Window ,titulo, padding
window= Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

#Objeto Entry
miles_input= Entry(width=7)
miles_input.grid(column=1,row=0)

#Objeto Label miles
miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

#Objeto Label is equal to
equal_label=Label(text="is equal to")
equal_label.grid(column=0,row=1)

#Objeto donde se envia el resultado de la funcion
kilometer_result=Label(text="0")
kilometer_result.grid(column=1,row=1)

#Objeto Label
kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)

#Objeto Button 
button= Button(text="Calculate",command=converte)
button.grid(column=1,row=2)


#Para que la pantalla no cierre 
window.mainloop()