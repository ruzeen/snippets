# Collatz Conjecture
''' Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. '''

def collatz(n):
  if n < 2:
    return 'Please input a number greater than 1.'
  else:
    steps = 0
    while n > 1:
      if n%2 == 0:
        n/=2
        steps += 1
      else:
        n = (n*3) + 1
        steps += 1
        n/=2
        steps += 1
    return steps
