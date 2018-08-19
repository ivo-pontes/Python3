#!/usr/bin/env python3
# -*- coding: utf-8 -*


'''
Classe Node
Nó de uma Estrutura de Dados Abstrata
Guarda a Referência para o próximo Nó
'''
class Node:
	def __init__(self, label):
		self.__label = label
		self.__next = None
		#print(self.label)
		#print(self.next)

	@property
	def label(self):
		return self.__label
	
	@label.setter
	def label(self, label):
		self.__label = label

	@property
	def next(self):
		return self.__next
	
	@next.setter
	def next(self, next):
		self.__next = next

'''
Classe LinkedList
Lista Simplesmente Encadeada
'''
class LinkedList:
	def __init__(self):
		self.__first = None
		self.__last = None
		self.__size = 0

	@property
	def first(self):
		return self.__first
	@property
	def last(self):
		return self.__last
	@property
	def size(self):
		return self.__size
	
	@first.setter
	def first(self, no):
		self.__first = no

	@last.setter
	def last(self, no):
		self.__last = no

	@size.setter
	def size(self, size):
		self.__size = size

	'''
	Insere na lista o label e o índice
	'''
	def push(self, label, index):
		if index >= 0:
			#Cria novo nó
			no = Node(label)
			#Verifica se a lista está vazia
			if self.empty():
				self.first = no
				self.last = no
			else:
				if index == 0:
					#Inserção no início
					no.next = self.first
					self.first = no
				elif index >= self.size:
					#Inserção no final
					self.last.next = no
					self.last = no
				else:
					#Inserção no meio
					no_anterior = self.first
					no_atual = self.first.next
					indice_atual = 1

					while no_atual != None:
						if indice_atual == index:
							#Seta o no_atual como próximo do nó
							no.next = no_atual
							#Seta o no como próximo do no_anterior
							no.anterior.next = no
							break
						no_anterior = no_atual
						no_atual = no_atual.next
						indice_atual += 1

				#Atualiza o tamanho da lista
				self.size += 1


	def pop(self, index):
		if not self.empty() and index >= 0 and index < self.size:
			flag_remove = False

			if self.first.next == None:
				#Possui 1 elemento
				self.first = None
				self.last = None
				flag_remove = True
			elif index == 0:
				#Remove o primeiro, quando possui 2 elementos
				self.first = self.first.next
				flag_remove = True
			else:
				'''
				Tem vários elementos, logo a remoção não é do 1º Elemento
				'''
				no_anterior = self.first
				no_atual = self.first.next
				indice_atual = 1

				while no_atual != None:
					#O próximo do anterior aponta para o próximo do nó atual
					if index == indice_atual:
						no_anterior.next = no_atual.next
						no_atual.next = None
						flag_remove = True
						break

					no_anterior = no_atual
					no_atual = no_atual.next
					no_atual += 1

			if flag_remove:
				#Atualiza o tamanho da lista(decrementa)
				self.size -= 1

	'''
	Verifica se a lista está vazia
	'''
	def empty(self):
		return True if self.first == None else False

	'''
	Retorna o tamanho da lista
	'''
	def length(self):
		return self.size

	'''
	Imprime a lista
	'''
	def print(self):
		no_atual = self.first

		while no_atual != None:
			print(no_atual.label, end=' ')
			no_atual = no_atual.next
		print("")