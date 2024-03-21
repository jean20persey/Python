import tkinter

Ventana = tkinter.Tk() #Contenedor de graficas 
Ventana.geometry("400x400") 

Etiqueta = tkinter.Label (Ventana, text="Hola mundo", bg="Blue")
Etiqueta.pack(fill=tkinter.X)#Colocar el label en pantalla 

Caja1= tkinter.Entry(Ventana, font="Helvetica 20")
Caja1.pack()
Caja2=tkinter.Entry(Ventana, font="Helvetica 20")
Caja2.pack()

def Numeros_Caja():
    Numero1=int(Caja1.get())
    Numero2=int(Caja2.get())
    Resultado = Numero1*Numero2
    EtiquetaResult["text"]=Resultado
    #print("El resultado de la multiplicacion es : ", Resultado)


Boton = tkinter.Button(Ventana,text="Multiplicar", command=Numeros_Caja)
Boton.pack()

EtiquetaResult = tkinter.Label(Ventana,text ="",bg="pink",font="Helvetica 20")
EtiquetaResult.pack(fill=tkinter.X)

Ventana.mainloop()