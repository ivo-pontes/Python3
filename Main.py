#!/usr/bin/env python3
# -*- coding: utf-8 -*

#Módulo Básico
'''
from basico.Lambda import Lambda
from basico.Recursividade import Recursividade
from basico.ModuloMath import ModuloMath
from Thread.Threads import Threads'''
from gui.Gui import Gui

#Módulo Estrutura de Dados
from ed.Stack import Stack
from ed.Queue import Queue
from ed.Deque import Deque
from ed.LinkedList import LinkedList
from ed.BinaryTree import BinaryTree

if __name__ == '__main__':
	'''
	Módulo Básico
	'''

	#obj = Lambda()
	#recursao = Recursividade()
	#moduloMath = ModuloMath()
	#thread = Threads()
	#gui = Gui()

	'''
	Módulo Estrutura de Dados
	'''

	#Pilha
	'''
	print("Pilha")
	s = Stack()
	s.pop()
	print("Vazia: {}".format(s.empty()))
	s.push(10)
	s.push(3)
	print("Vazia: {}\nPilha: {}".format(s.empty(), s.stack))
	print("Tamanho: {}".format(s.length()))
	print("Topo: {}".format(s.top()))
	'''

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
	
	#Lista Ligada
	'''
	lista = LinkedList()
	lista.push("Zi",0)
	lista.push("Lane", 1)
	lista.push("El",0)
	lista.push("Ivo",3)
	lista.print()
	print("Tamanho: {}".format(lista.size))
	lista.pop(0)
	lista.print()
	lista.pop(1)
	lista.print()
	'''

	#Árvore Binária
	tree = BinaryTree()
	tree.insert(8)
	tree.insert(3)
	tree.insert(1)
	tree.insert(6)
	tree.insert(4)
	tree.insert(7)
	tree.insert(10)
	tree.insert(14)
	tree.insert(13)
	
	#tree.preOrdem(tree.root)
	#print("")
	tree.remove(3)

	tree.preOrdem(tree.root)

	print("Fim execução!!")
