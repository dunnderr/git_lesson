#!/usr/bin/env python
def my_square(y):
  """
  my_square(y): calculates the square of arg y. Uses the python ** operator.
  """
  return(y**2)

def my_square2(x):
  return(x*x)

if __name__ == "__main__":
  print("The square of 42 is {0:6.2f}".format(my_square(42)))
  print("The square of 42 is {0:6.2f}".format(my_square2(42)))

