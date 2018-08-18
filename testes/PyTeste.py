#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Recursividade import Recursividade


recursividade = Recursividade()

def test_fatorial():
	assert recursividade.fatorial(4) == 24

def par(n):
	if n % 2 == 0:
		return True
	return False

def test_par():
	assert par(4) == True