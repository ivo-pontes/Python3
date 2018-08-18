#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Recursividade import Recursividade

import unittest

class Testes(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(Testes, self).__init__(*args, **kwargs)
		self.recursao = Recursividade()

	def testarPotencia(self):
		print("\nTeste do método de Potência Recursiva")
		self.assertEqual(1024, self.recursao.potencia(2,10))
	def testarFatorial(self):
		print("\nTeste do método de Fatorial Recursivo")
		self.assertEqual(24, self.recursao.fatorial(4))


unittest.main()