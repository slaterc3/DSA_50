def sum_digits(n):
  if n < 0:
    raise ValueError("inputs greater than 0 only")
  if n == 0:
    return n 
  running_total = (n % 10)
  print(f'running total = {running_total}')
  
  return running_total + sum_digits(n//10)

# test cases
print(sum_digits(123))
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)