#!/usr/bin/env python3
# -*- coding: utf-8 -*

from tkinter import *


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
		self.label.pack()

		message = "Escolha o Método de Reconstrução de Árvore Filogenética:"
		self.chooseLabel = Label(window, text=message, width=30)

		window.geometry('450x250')
		window.mainloop()

	def click_button(self):
		self.label.config(text=self.entry_text.get())
		self.label.pack(padx=10, pady=10)