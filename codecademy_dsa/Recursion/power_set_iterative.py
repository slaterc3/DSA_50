def power_set(set):
  power_set_size = 2**len(set)
  result = []

  for bit in range(0, power_set_size):
    sub_set = []
    for binary_digit in range(0, len(set)):
    #   print(bit)
      if((bit & (1 << binary_digit)) > 0):
        sub_set.append(set[binary_digit])
    result.append(sub_set)
  return result

if __name__ == "__main__":
    
    lst = ['a','b','c']
    print(power_set(lst))