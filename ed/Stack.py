#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
Classe Pilha
FILO = FIRST IN LAST OUT
'''
class Stack: #Pilha
	
	def __init__(self):
		self.stack = []
		self.size = 0


	'''
	Insere ao fim da lista
	'''
	def push(self, item):
		self.stack.append(item)
		self.size += 1

	'''
	Remove o último item da pilha
	'''
	def pop(self):
		if not self.empty():
			self.stack.pop(self.size-1)
			self.size -= 1
		else:
			print("Pilha Vazia!")
		

	'''
	Retorna o topo da pilha
	'''
	def top(self):
		return self.stack[-1]

	'''
	Verifica se a pilha está vazia
	'''
	def empty(self):
		return True if self.size == 0 else False

	'''
	Retorna o tamanho da pilha
	'''
	def length(self):
		return self.size
