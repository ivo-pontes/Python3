#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
Classe Deque - Double Ended Queue
'''
class Deque:
	
	def __init__(self):
		self.deque = []
		self.size = 0

	'''
	Insere ao fim da fila
	'''
	def push_back(self, item):
		self.deque.insert(self.size, item)
		self.size += 1


	'''
	Insere ao início da fila
	'''
	def push_front(self, item):
		self.deque.insert(0,item)
		self.size += 1

	'''
	Remove o primeiro item da fila
	'''
	def pop_front(self):
		if not self.empty():
			self.deque.pop(0)
			self.size -= 1
		else:
			print("Fila Vazia!")

	'''
	Remove o último item da fila
	'''
	def pop_back(self):
		if not self.empty():
			self.deque.pop()
			self.size -= 1
		else:
			print("Fila Vazia!")


	'''
	Verifica se a fila está vazia
	'''
	def empty(self):
		return True if self.size == 0 else False

	'''
	Retorna o tamanho da fila
	'''
	def length(self):
		return self.size

	'''
	Retorna o primeiro Item da fila
	'''
	def front(self):
		if not self.empty():
			return self.deque[0]

	'''
	Retorna o último Item da fila
	'''
	def back(self):
		if not self.empty():
			return self.deque[-1]

	'''
	Imprime o deque
	'''
	def print(self):
		for i in self.deque:
			print(i, end=' ') #Imprime todos os índices com espaço ao invés de '\n'
		print("\n")

#Deque
'''
print("Deque")
d = Deque()
#Inserção
d.push_front(10)
d.push_front(5)
d.print()
d.push_back(20)
d.push_front(7) #Deve ficar 7,5,10,20
d.push_back(40) #Deve ficar 7,5,10,20,40
d.print()
print("Primeiro elemento: {}".format(d.front()))
print("Último elemento: {}".format(d.back()))
#Remoção
d.pop_back()	#Deve ficar 7,5,10,20
d.pop_back()	#Deve ficar 7,5,10
d.pop_front()	#Deve ficar 5,10
d.pop_front()	#Deve ficar 10
d.pop_front()	#Deve ficar vazio
d.print()
'''