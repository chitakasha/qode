def factorial(n):
  # Check if n is a positive integer
  if not isinstance(n, int) or n < 0:
    raise ValueError("n must be a positive integer")
  # Base case: 0! = 1
  if n == 0:
    return 1
  # Recursive case: n! = n * (n-1)!
  else:
    return n * factorial(n-1)

