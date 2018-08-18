#!/usr/bin/env python3
# -*- coding: utf-8 -*

class Lambda():
	'''
	Métodos que utilizam lambda, para programação funcional
	'''
	def __init__(self):
		print("Classe Lambda")
		print("2**2: {}.".format(self.pot2(2)))
		print("2**2: {}. (lambda)".format(self.pot2_lambda(2)))
		print("Fatorial de {}: {}.".format(5,self.fatorial(5)))
		print("Fatorial de {}: {}. (lambda)".format(5,self.fatorial_lambda(5)))

		#Map é aplicar uma função em todos os itens de uma sequência
		l = [1,2,3,4,5]	
		print("Função Quadrática com Map:")
		x = self.quadradoMap(l)
		for i in x:
			print(i)

		print("Valores filtrados de um array:")
		#Filtará os valores True da função lambda
		f = self.filterLambda()
		for i in f:
			print(i)

	def pot2(self, x):
		return x**2

	pot2_lambda = lambda self, x: x**2

	def fatorial(self, n):
		if n == 0:
			return 1
		else:
			return (n*self.fatorial(n-1))
	
	fatorial_lambda = lambda self, n: n*self.fatorial_lambda(n-1) if n > 1 else 1

	def quadradoMap(self,lista):
		return map(lambda x: x**2, lista)

	def filterLambda(self):
		#Selecionará somente valores da função(se é par), e adicionará em f
		return filter(lambda x: x%2==0, range(10))