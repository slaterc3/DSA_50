def fibonacci(n):
  if not isinstance(n, int):
    raise TypeError("Must error an integer value")
  if n < 0:
    raise ValueError("Input 0 or greater only!")
  if n in (0, 1):
    return n 
  a, b = 0, 1 
  for _ in range(2, n+1):
    a, b = b, a + b 
  return b 
    

# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)