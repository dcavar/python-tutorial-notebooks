#/usr/bin/env
# -*- coding: utf-8 -*-

"""
worker.py

(C) 2023 by Damir Cavar (http://damir.cavar.me/)

This is a worker function that can be imported from a Jupyter notebook and serve as a
multiprocess function.
"""

import itertools


def get_combinations(elements):
	"""Returns a tuple of unique tuples of the length of 2 generated from the elements sequence."""
	return tuple(itertools.combinations(elements, 2))


def get_combinations_n(elements, n):
	"""Returns a tuple of unique tuples of the length of n generated from the elements sequence."""
	return tuple(itertools.combinations(elements, n))

