#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):

    # the two shorter sides together must be longer than the longest side.
    # otherwise geometrically it makes no sense.
    (aa, bb, cc) = sorted([a, b, c])
    if aa + bb <= cc:
        raise TriangleError

    sides = set([a, b, c])
    if len(sides) == 1:
        return 'equilateral'
    elif len(sides) == 2:
        return 'isosceles'
    else:
        return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
