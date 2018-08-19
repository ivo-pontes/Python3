#!/usr/bin/env python3
# -*- coding: utf-8 -*

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Gui():

	def __init__(self):

		self.window = Tk()
		self.window.title('Interface Gráfica')

		menu = Menu(self.window)
		self.window.config(menu=menu)
		menuArquivo = Menu(menu)
		menu.add_cascade(label="Arquivo", menu=menuArquivo)
		menuArquivo.add_command(label="Novo", command=self.novoArquivo)
		menuArquivo.add_command(label="Abrir...", command=self.abrirArquivo)
		menuArquivo.add_separator()
		menuArquivo.add_command(label="Sair", command=self.window.quit)

		sobre = Menu(menu)
		menu.add_cascade(label="Sobre", menu=sobre)
		sobre.add_command(label="Sobre", command=self.menuSobre)


		self.entry_text = Entry(self.window, width=30)
		self.entry_text.pack(padx=10, pady=10)
		self.entry_text.focus_set()

		btn = Button(self.window, text='Clique Aqui', width=10, command=self.click_button)
		btn.pack(padx=10, pady=10)

		self.label = Label(self.window, text="",width=30)
		self.label.pack(padx=10, pady=10)

		message = "Escolha o Método de Reconstrução de Árvore Filogenética:"
		self.chooseLabel = Label(self.window, text=message, width=30)

		self.radio_value = IntVar()
		self.radio_value.set(0) #escolhe a posição 0

		self.opcoes = [
			"UPGMA",
			"Neighbor Joining",
			"Fast Neighbor Joining",
			"Maximum Parsimony"
		]

		m = "Escolha o Método de Reconstrução de Árvore Filogenética"
		self.radio_button = Label(self.window, text=m, width=45)
		self.radio_button.pack(padx=10, pady=10)

		for i in range(len(self.opcoes)):
			Radiobutton(self.window, text=self.opcoes[i],padx=10,variable=self.radio_value,command=self.mostrar_valor,value=i).pack(anchor=W)


		tree_view = ttk.Treeview(self.window, columns=('coluna 2', 'coluna 3'))
		tree_view.heading('#0', text='Item')
		tree_view.heading('#1', text='Coluna 2')
		tree_view.heading('#2', text='Coluna 3')
		tree_view.column('#1', stretch='YES')
		tree_view.column('#2', stretch='YES')
		tree_view.column('#0', stretch='YES')
		#tree_view.grid(row=4,columnspan=4,sticky='nsew')
		for i in range(4):
			tree_view.insert('','end',text='Item_'+str(i),values=(str(i)+" mg", str(i)))

		tree_view.pack(padx=10, pady=10)

		self.window.geometry('650x400')
		self.window.mainloop()

	def click_button(self):
		self.label.config(text=self.entry_text.get())
		self.label.pack(padx=10, pady=10)

	def mostrar_valor(self):
		print(self.radio_value.get())
		messagebox.showinfo('Valor Selecionado', self.opcoes[self.radio_value.get()])

	def novoArquivo(self):
		messagebox.showinfo('Novo Arquivo', "Tudo certo!")

	def abrirArquivo(self):
		print('Abrir Arquivo')
		name = filedialog.askopenfilename(initialdir = '/', title='Abrir arquivo', filetypes=(('jpeg files', '*.jpg'),("all files","*.*")))
		print(name)
		self.window.filename = name
		print(self.window.filename)
	def menuSobre(self):
		messagebox.showinfo('Sobre Mim', "Eu sou eu.")