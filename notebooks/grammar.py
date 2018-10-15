#!/usr/bin/env python

"""
Filename: grammar.py
Author: Damir Cavar
Date: 19. Sept. 2005

(C) 2005 by Damir Cavar

	This code is free; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 2 of the License, or
	(at your option) any later version.

This is a simple implementation of a context free grammar parser that
reads in files of the format:

-----------  begin file example  -----------

# my small example grammar
S -> NP VP

NP -> N
NP -> Art N
NP -> Art Adj N

VP -> V
VP -> V NP

# lexical rules
Art -> the
Art -> a
Adj -> green
Adj -> big
N -> dog
N -> cat
N -> mouse
V -> chase
V -> ignore

------------  end file example  ------------
"""

import sys

class PSG:
	"""
	Grammar class:
	Internal data structures:
	
	LHS: dictionary with left-hand-side symbols as keys and a list
	of possible right-hand-sides as values.
	
	RHS: dictionary with right-hand-side symbol tuples as keys and a list
	of possible left-hand-sides.
	"""

	def __init__(self, filename):
		"""Constructor."""
		self.LHS   = {}
		self.RHS   = {}
		self.__read__(filename)

	def __str__(self):
		"""Generates a string representation of the grammar such that the grammar
		is dumped in a phrase structure rule format."""
		text = ""
		for i in self.LHS.keys(): # self.rules:
			if len(text) > 0:
				text += "\n"
			for x in self.LHS[i]:
				text += i + " -> " + " ".join(x) + "\n"
		return text

	def __read__(self, filename):
		"""Read in a CFG and return a grammar representation. This is a
		hidden method."""
		try:
			file = open(filename)
			for i in file.readlines():
				i = i.split("#")[0].strip() # cut off comment string and strip
				if len(i) > 0:   # rule line, expected -> somewhere
					tokens = i.split("->")
					if len(tokens) == 2: # we need exactly two tokens
						lhs = tokens[0].split()
						if len(lhs) == 1: # we need exactly one token on LHS
							rhs = tuple(tokens[1].split())
							value = self.LHS.get(lhs[0], [ ])
							if rhs not in value:  value.append(rhs)
							self.LHS[lhs[0]] = value
							value = self.RHS.get(rhs, [ ])
							if lhs[0] not in value:  value.append(lhs[0])
							self.RHS[rhs] = value
			file.close()
		except IOError:
			pass

	def getRHS(self, left):
		"""Return the RHS for a LHS."""
		return self.LHS.get(left, [])

	def getLHS(self, right):
		"""Return LHS for a RHS."""
		return self.RHS.get(right, [])


if __name__ == "__main__":
	if len(sys.argv) > 1:
		myGrammar = PSG(sys.argv[1])
		print myGrammar
