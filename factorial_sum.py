# -*- coding: utf-8 -*-

"""
This algorithm calculates the sum of the factorials of a list of integers provided by the user
Author: Felipe Andrade
"""

def factorial_sum(values):
  sum = 0
  for value in values:
    sum += factorial(value)
  return sum

def factorial(value):
  if value == 0:
    return 1
  else:
    return value * factorial(value - 1)

def main():
  while True:
    try:
      values = input()
      values = values.split()
      values = [int(value) for value in values]
      sum = factorial_sum(values)
      print(sum)
    except EOFError:
      break

if __name__ == "__main__":
  main()
