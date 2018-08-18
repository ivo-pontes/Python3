#!/usr/bin/env python3
# -*- coding: utf-8 -*

from threading import Thread
import time


class Threads():

	def __init__(self):
		for i in range(10):
			t = Thread(target=self.funcao, args = (i,))
			t.start()

	def funcao(self, i):
		print('Iniciando a thread {}'.format(i))
		time.sleep(5)
		print('Thread {} finalizada'.format(i))
