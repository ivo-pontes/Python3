#!/usr/bin/env python3
# -*- coding: utf-8 -*
import sys

'''
Classe HashTable
'''
class HashTable:
	def __init__(self, table_size):
		if table_size < 1:
			print('Erro: o tamanho da tabela tem que ser positivo!')
			sys.exit(1)

		self.__table_size = table_size
		#Cria uma tabela com N listas vazias
		self.__table = [[] for i in range(table_size)]

	@property
	def table_size(self):
		return self.__table_size
	
	@table_size.setter
	def table_size(self, size):
		self.__table_size = size

	@property
	def table(self):
		return self.__table
	
	@table.setter
	def table(self, table):
		self.__table = table

	def hash(self, key):
		return key % self.table_size

	def insert(self, key):
		self.table[self.hash(key)].append(key)

	def print(self):
		for lista in self.table:
			if lista:
				for key in lista:
					print("{}".format(key), end = ' ')
				print('')

	def search(self, key):
		return True if key in self.table[self.hash(key)] else False

			
#Tabela Hash
'''
d = HashTable(9)
d.insert(19)
d.insert(28)
d.insert(20)
d.insert(5)
d.insert(33)
d.insert(15)

d.print()
'''