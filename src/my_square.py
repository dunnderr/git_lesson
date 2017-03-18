#!/usr/bin/env python
def my_square(y):
  """
  my_square(y): Returns the square of arg y. Uses the python ** operator.
  """
  return(y**2)

def my_square2(x):
  """
  my_squre2(x): Returns the square of x by multiplying x by x.
  """
  return(x*x)

if __name__ == "__main__":
  print("The square of 42 is {0:6.2f}".format(my_square(42)))
  print("The square of 42 is {0:6.2f}".format(my_square2(42)))

