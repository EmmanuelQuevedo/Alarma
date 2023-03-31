from tkinter import*
import time
from tkinter import ttk
import pygame
from pygame.locals import*
from tkinter import messagebox as MessageBox
from tkinter import filedialog


pygame.init()


def abrirArchivo():
    cancion= filedialog.askopenfilename() 
    print(cancion)
    pygame.mixer.music.load(cancion)
    
def musica():
	pygame.mixer.music.play()
    

def clock():

	hora =  time.strftime('%H')
	minutos = time.strftime('%M')

	segundos = time.strftime('%S')

	horaActual = (hora + ' : '+ minutos+ ' : '+ segundos)
	textoHora.config(text=horaActual, font = ("Roboto", 20))

	hrs = combobox1.get()
	minu = combobox2.get()
	horaAlarma = hrs +' : '+ minu +' : '+ '00'
	
	alarma['text']= horaAlarma


	if int(hora) == int(hrs):
		if int(minutos) == int(minu):
			musica()
			

	textoHora.after(1000, clock)

def guardarAlarma():
	hrs = combobox1.get()
	minu = combobox2.get()
	horaAlarma = hrs +' : '+ minu +' : '+ '00'
	alarma['text']= horaAlarma
	MessageBox.showinfo(message=f'Alarma establecida a las {horaAlarma}', title="Alarma")

def detenerAlarma():
    MessageBox.showinfo("Informacion", "La alarma se ha detenido")
    pygame.mixer.music.stop()
    root.destroy()

    
    
root = Tk()
root.geometry("400x400")
root.title("ALARMA")
root.config(bg='black')
root.iconbitmap("alarma.ico")

lista_horas = []
lista_minutos = []


for  i in range(0,24):
	lista_horas.append(i)
for  i in range(0,60):
	lista_minutos.append(i)



titulo = Label(root, text="ALARMA", font=("Roboto",18,"bold"), bg="#000000", fg="#fff")
titulo.grid(row=1,column=2, rowspan=2, columnspan=4)


titulo2 = Label(root, text="H:", font=("Roboto",18,"bold"), bg="#000000", fg="#fff")
titulo2.grid(row=8,column=1,)

combobox1 = ttk.Combobox(root, values = lista_horas, justify='center',width='12', font=("Roboto",15))
combobox1.grid(row=8, column=2)
combobox1.current(0)

titulo3 = Label(root, text="M:", font=("Roboto",18,"bold"), bg="#000000", fg="#fff")
titulo3.grid(row=10,column=1)

combobox2 = ttk.Combobox(root, values = lista_minutos, justify='center',width='12', font=("Roboto",15))
combobox2.grid(row=10, column=2)
combobox2.current(0)

alarma = Label(root,  bg="#000000", fg="#fff", font = ('Roboto', 20))
alarma.grid(row=17, column=2)

titulo4=Label(root, font=("Roboto",18,"bold"), bg="#000000", fg="#fff", text="Hora Actual")
titulo4.grid(row=13,column=1)

titulo5=Label(root, font=("Roboto",18,"bold"), bg="#000000", fg="#fff", text="Alarma: ")
titulo5.grid(row=17,column=1)


textoHora = Label(root,  bg="#000000", fg="#fff",)

textoHora.grid(row=13,column=2)

titulo6 = Label(root, text="-------------------------------------------------------", font=("Roboto",10,"bold"),bg="#000", fg="#fff")
titulo6.grid(row=24, column=2)


botonGuardar= Button(root, text="Guardar alarma", bg="#fff", fg="#000", font=("Roboto", 12, "bold"), width=15, height=2, command=guardarAlarma)
botonGuardar.grid(row=15,column=2)

botonOpensong= Button(root, text="Seleccionar sonido", bg="#fff", fg="#000", font=("Roboto", 12, "bold"), width=15, height=1, command=abrirArchivo)
botonOpensong.grid(row=23,column=2)

botonDetener = Button(root, text="Detener alarma", font=("Roboto",12, "bold"), command=detenerAlarma).grid(row=25, column=2)

clock()

root.mainloop()