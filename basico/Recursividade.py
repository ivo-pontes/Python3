#!/usr/bin/env python3
# -*- coding: utf-8 -*

class Recursividade():
	'''
	Conhecimentos básicos sobre recursividade
	'''
	def __init__(self):
		pass
		'''
		print("Fatorial")
		print(self.fatorial(4))
		print("Fibonacci")
		print(self.fibonacci(7))
		print("Potência")
		print(self.potencia(2,10))
		'''

	def fatorial(self, n):
		if n == 0:
			return 1
		else:
			return n*self.fatorial(n-1)

	def fibonacci(self, n):
		if n == 1 or n == 2:
			return 1
		return self.fibonacci(n-1) + self.fibonacci(n-2)

	def potencia(self, base, exp):
		if exp == 0:
			return 1
		return base * self.potencia(base, exp-1)