#!/usr/bin/env python3
# -*- coding: utf-8 -*


'''
Classe Entidade, pode ser qualquer tipo de objeto
que tenha prioridade(pessoa, automóvel, impressora)
'''
class Entidade:

	def __init__(self, name, prior):
		self.name = name
		self.prior = prior

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name
	
	@property
	def prior(self):
		return self.__prior

	@prior.setter
	def prior(self, prior):
		self.__prior = prior



'''
Classe Fila de Prioridades
Com lista ordenada
'''
class PriorityQueue: #Fila de prioridades
	
	def __init__(self):
		self.__queue = []
		self.__size = 0

	@property
	def queue(self):
		return self.__queue
	
	@queue.setter
	def queue(self, queue):
		self.__queue = queue

	@property
	def size(self):
		return self.__size
	

	@size.setter
	def size(self, size):
		self.__size = size

	'''
	Insere decrescentemente pela prioridade
	'''
	def push(self, item):
		if self.empty():
			self.queue.append(item)
		else:
			flag_push = False
			#Procura-se onde inserir para manter a fila ordenada
			for i in range(self.size):
				if self.queue[i].prior < item.prior:
					self.queue.insert(i, item)
					flag_push = True
					break

			if not flag_push:
				#Insere-se ao fim
				self.queue.insert(self.size, item)
		
		self.size += 1

	'''
	Remove o item da fila
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
	Imprime a fila
	'''
	def print(self):
		for p in self.queue:
			print('Nome: {}\nPrioridade: {}\n'.format(p.name, p.prior))


#Fila de Prioridade
'''
lista = PriorityQueue()
item1 = Entidade('M', 28)
item2 = Entidade('C', 3)
item3 = Entidade('P', 20)
item4 = Entidade('J', 35)

lista.push(item1)
lista.push(item2)
lista.push(item3)
lista.push(item4)

lista.print()

lista.pop()
lista.pop()

print("--------Remoções--------")
lista.print()
'''