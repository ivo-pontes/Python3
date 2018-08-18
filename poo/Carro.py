#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Transporte import Transporte

class Carro(Transporte):
	'''
	
	'''
	def __init__(self, nome, peso, preco, preco_seguro):
		Transporte.__init__(self, nome, peso, preco)
		self.preco_seguro = preco_seguro
