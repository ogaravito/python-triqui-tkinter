from tkinter import *
from tkinter import messagebox

matriz = [  ['' for j in range(3) ]  for i in range(3) ]
triqui = [   ['X','X','X']   ,  ['O','O','O']    ]
lista_botones = []
ultima_letra = ''

def limpiar(gano):
	global matriz
	global ultima_letra
	if gano:
		messagebox.showinfo('TRIQUI', "Has ganado\n" + ultima_letra)
	matriz = [  ['' for j in range(3) ]  for i in range(3) ]
	for i in lista_botones:
		i['text']=''

def clic_btn(num_btn):
	print(num_btn)
	global ultima_letra
	k=0
	for i in range(3):
		for j in range(3):
			if k==num_btn and matriz[i][j] == '':
					ultima_letra = 'X' if ultima_letra != 'X' else 'O'
					matriz[i][j]=ultima_letra
					btn = lista_botones[num_btn]
					btn['text'] = ultima_letra
			k+=1

	for i in range(3):
		if matriz[i] in triqui:
			print("hiciste triqui h")

	for i in range(3):
		columna = []
		for j in range(3):
			columna.append(matriz[j][i])
		if columna in triqui: 
			print("Hiciste triqui v")

	diagonal = []
	for i in range(3):
		diagonal.append(matriz[i][i])
	if diagonal in triqui:
		print("Hiciste triqui d")

	diagonal2 = []
	for i in range(3):
		diagonal2.append(matriz[i][2-i])
	if diagonal2 in triqui:
		print("Hiciste triqui d2")

	for i in range(3): 
		if matriz[i] in triqui or [matriz[j][i] for j in range(3)] in triqui :
			limpiar(True)
			return

	if [ matriz[i][i]   for i in range(3)] in triqui or [ matriz[i][2-i]   for i in range(3)] in triqui:
		limpiar(True)
		return

ventana = Tk()
ventana.title("Triqui")

k=0
for i in range(3):
	for j in range(3):
		boton = Button(ventana, text="", command=lambda arg1=k:clic_btn(arg1), height=3, width=3)
		boton.grid(row=i, column=j)
		lista_botones.append(boton)
		k+=1

btn_limpiar = Button(ventana, text=" Iniciar ", command=lambda:limpiar(False), height=3, bg="#999", fg="#fff")
btn_limpiar.grid(row=3, column=0, columnspan=3, sticky="nsew")



ventana.mainloop()





