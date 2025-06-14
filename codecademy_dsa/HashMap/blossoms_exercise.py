from linked_list import Node, LinkedList
from flowers import flower_definitions 


class HashMap:
  def __init__(self, size):
    self.array_size = size 
    self.array = [LinkedList() for x in range(size)]

  def hash(self, key):
    return sum(key.encode())
  
  def compress(self, hash):
    return hash % self.array_size
  
  def assign(self, key, value):
    payload = Node([key, value])
    array_idx = self.compress(self.hash(key))
    list_at_array = self.array[array_idx]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return 
    list_at_array.insert(payload)
    # self.array[array_id] = [key, value]
  
  def retrieve(self, key):
    array_idx = self.compress(self.hash(key))
    list_at_index = self.array[array_idx]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None      


if __name__ == '__main__':
  blossom = HashMap(len(flower_definitions))
  for flower_def in flower_definitions:
    blossom.assign(flower_def[0], flower_def[1])
  
  print(blossom.retrieve('daisy'))
