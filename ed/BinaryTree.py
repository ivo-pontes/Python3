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
		self.__left = None
		self.__right = None

	@property
	def label(self):
		return self.__label
	
	@label.setter
	def label(self, label):
		self.__label = label

	@property
	def left(self):
		return self.__left
	
	@left.setter
	def left(self, left):
		self.__left = left

	@property
	def right(self):
		return self.__right
	
	@right.setter
	def right(self, right):
		self.__right = right

'''
Árvore Binária
'''
class BinaryTree:
	def __init__(self):
		self.__root = None

	@property
	def root(self):
		return self.__root
	
	@root.setter
	def root(self, root):
		self.__root = root


	'''
	Verifica se a árvore está vazia
	'''
	def empty(self):
		return True if self.root == None else False

	'''
	Imprime em pré-ordem
	'''
	def preOrdem(self, no):
		if no != None:
			print("{}".format(no.label), end=' ')
			self.preOrdem(no.left)
			self.preOrdem(no.right)

	def insert(self, label):
		#Cria novo nó
		no = Node(label)

		#Verifica se a árvore está vazia
		if self.empty():
			self.root = no
		else:
			#Árvore não vaiza, insere recursivamente
			pai = None
			no_atual = self.root

			while True:
				if no_atual != None:
					pai = no_atual

					#Verifica se vai para esquerda ou direita
					if no.label < no_atual.label:
						#Esquerda <-
						no_atual = no_atual.left
					else:
						#Direita ->
						no_atual = no_atual.right
				else:
					#Se no_atual está vazio(None), inserir
					if no.label < pai.label:
						pai.left = no
					else:
						pai.right = no
					break


	'''

	'''
	def remove(self, label):
		pai = None
		no_atual = self.root

		while no_atual != None:
			#Verifica se encontrou o nó
			if label == no_atual.label:
				#Caso 1: nó a ser removido não possui filhos
				if no_atual.left == None and no_atual.right == None:
					#Verifica se é raiz
					if pai == None:
						self.root = None
					else:
						#Verifica se é filho(pela esquerda ou direita)
						if pai.left == no_atual:
							pai.left = None
						elif pai.right == no_atual:
							pai.right = None
			#Caso 2: nó a ser removido possui apenas um filho
			elif (no_atual.left == None and no_atual.right != None) \
				or (no_atual.left != None and no_atual.right == None):
				#Verifico se o nó a ser removido é a raiz
				if pai == None:
					#Verifica se o filho do no_atual é filho à esquerda
					if no_atual.left != None:
						self.root = no_atual.left
					else: #O filho de no_atual é filho à direita
						self.root = no_atual.right
				else:
					#Verifica se o filho de no_atual é filho à esquerda
					if no_atual.left != None:
						#Verifica se no_atual é filho à esquerda
						if pai.left and pai.left.label == no_atual.label:
							pai.left = no_atual.left
						else: #no_atual é filho à direita
							pai.right = no_atual.left
					else: #filho de no_atual é filho à direita
						#Verifica se no_atual é filho à esqeurda
						if pai.left and pai.left.label == no_atual.label:
							pai.left = no_atual.right
						else: #no_atual é filho à direita
							pai.right = no_atual.right
			#Caso 3: o nó a ser removido possui dois filhos
			#Menor elemento da subárvore a direita é o filho
			elif no_atual.left != None and no_atual.right != None:
				pai_menor_no = no_atual
				menor_no = no_atual.right
				proximo_menor = no_atual.right.left

				while proximo_menor != None:
					pai_menor_no = menor_no
					menor_no = proximo_menor
					proximo_menor = menor_no.left

				#Verifica se o nó a ser removido é raiz
				if pai == None:
					#Verifica se nó vai ser nova raiz é filho da raiz
					if self.root.right.label == menor_no.label:
						menor_no.left = self.root.left
					else:
					#Verifica se o menor_no é filho à esquerda ou à direita
					#Para setar None o menor nó
						if pai_menor_no.left and pai_menor_no.left.label == menor_no.label:
							pai_menor_no.left = None
						else:
							pai_menor_no.right = None

						#Seta os filhos à direita e esquerda de menor_no
						menor_no.left = no_atual.left
						menor_no.right = no_atual.right

					#O menor_no agora é raiz
					self.root = menor_no

				#O nó a ser removido não é raiz	
				else:
					'''
					Verifica se o no_atual é filho à esquerda ou à direita
					para setar o menor_no como filho do pai do no_atual
					'''
					if pai.left and pai.left.label == no_atual.label:
						pai.left = menor_no
					else:
						pai.right = menor_no
					
					'''
					Verifica se o menor_no é filho à esquerda ou à direita
					para setar None no menor_no
					'''
					if pai_menor_no.left and pai_menor_no.left.label == menor_no.label:
						pai_menor_no.left = None
					else:
						pai_menor_no.right = None

					#setar filhos à esquerda e direita do menor_no
					menor_no.left = no_atual.left
					menor_no.right = no_atual.right

			break
		pai = no_atual

		#Verifica se vai para esquerda ou direita
		if label < no_atual.label:
			no_atual = no_atual.left
		else:
			no_atual = no_atual.right
