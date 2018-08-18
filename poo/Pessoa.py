
#!/usr/bin/env python3
# -*- coding: utf-8 -*

class Pessoa():

	def __init__(self, nome):
		self.__nome = nome

	'''
	Annotation property para retornar o nome: 'getNome()'
	'''
	@property
	def nome(self):
		return self.__nome
	
	'''
	Annotation @variavel.setter para alterar o nome: 'setNome(valor)'
	'''
	@nome.setter
	def nome(self, nome):
		self.__nome = nome

'''
p = Pessoa('Ivo')
print(p.nome)
p.nome = 'Aivow'
print(p.nome)
'''