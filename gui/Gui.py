#!/usr/bin/env python3
# -*- coding: utf-8 -*

from tkinter import *
from tkinter import messagebox

class Gui():

	def __init__(self):

		window = Tk()
		window.title('Interface Gráfica')

		self.entry_text = Entry(window, width=30)
		self.entry_text.pack(padx=10, pady=10)
		self.entry_text.focus_set()

		btn = Button(window, text='Clique Aqui', width=10, command=self.click_button)
		btn.pack(padx=10, pady=10)

		self.label = Label(window, text="",width=30)
		self.label.pack(padx=10, pady=10)

		message = "Escolha o Método de Reconstrução de Árvore Filogenética:"
		self.chooseLabel = Label(window, text=message, width=30)

		self.radio_value = IntVar()
		self.radio_value.set(0) #escolhe a posição 0

		self.opcoes = [
			"UPGMA",
			"Neighbor Joining",
			"Fast Neighbor Joining",
			"Maximum Parsimony"
		]

		m = "Escolha o Método de Reconstrução de Árvore Filogenética"
		self.radio_button = Label(window, text=m, width=45)
		self.radio_button.pack(padx=10, pady=10)

		for i in range(len(self.opcoes)):
			Radiobutton(window, text=self.opcoes[i],padx=10,variable=self.radio_value,command=self.mostrar_valor,value=i).pack(anchor=W)


		window.geometry('450x250')
		window.mainloop()

	def click_button(self):
		self.label.config(text=self.entry_text.get())
		self.label.pack(padx=10, pady=10)

	def mostrar_valor(self):
		print(self.radio_value.get())
		messagebox.showinfo('Valor Selecionado', self.opcoes[self.radio_value.get()])