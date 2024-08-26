# -*- coding: utf-8 -*-

"""
This algorithm calculates the average quadratic error (mean squared error) of a list of values provided by the user.
Author: Felipe Andrade
"""

import math

def avg_quadratic_error(values):
  n = len(values)
  medium = sum(values) / n
  errors = []
  for value in values:
    errors.append((value - medium)**2)
  return sum(errors) / n

def main():
  while True:
    try:
      n = int(input())
      if n <= 0:
        raise ValueError("O número de testes deve ser um inteiro positivo.")
      for _ in range(n):
        values = input().split()
        values = [float(value) for value in values]
        eqm = avg_quadratic_error(values)
        # precisao de ponto flutuante no OSX
        floor_eqm = math.floor(eqm * 100) / 100 
        print(f"{floor_eqm:.2f}")
    except ValueError as e:
      print(e)
    except EOFError:
      break

if __name__ == "__main__":
  main()
