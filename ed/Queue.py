#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
Classe Fila
FIFO = FIRST IN FIRST OUT
'''
class Queue: #Fila
	
	def __init__(self):
		self.queue = []
		self.size = 0

	'''
	Insere ao fim da fila
	'''
	def push(self, item):
		self.queue.append(item)
		self.size += 1

	'''
	Remove o primeiro item da fila
	'''
	def pop(self):
		if not self.empty():
			self.queue.pop(0)
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
			return self.queue[0]

#Fila
'''
print("Fila")
q = Queue()
q.push(10)
q.push(2)
q.push(4)
print("Vazia: {}".format(q.empty()))
print("Tamanho: {}".format(q.length()))
print("Frente: {}".format(q.front()))
q.pop()
print("Frente: {}".format(q.front()))
q.pop()
print("Frente: {}".format(q.front()))
q.pop()
print("Vazia: {}".format(q.empty()))
'''
