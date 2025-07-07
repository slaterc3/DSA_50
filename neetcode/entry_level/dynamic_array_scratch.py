class DynamicArray:

    def __init__(self, capacity: int):
        if capacity <= 0:
            # It's good practice to prevent non-positive capacity
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        # Corrected condition: Valid indices are from 0 up to length - 1
        if 0 <= i < self.length:
            return self.arr[i]

        raise IndexError("DynamicArray index out of range") # This is often preferred

    def set(self, i: int, n: int) -> bool: # Changed type hint to bool for clarity
        if 0 <= i < self.length: # Ensure index is valid for existing elements
            self.arr[i] = n
        #     return True # Indicate successful set
        # return False # Indicate failure (index out of current bounds)

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
            return self.arr[self.length] # Return the element that was at the new self.length
        # If popback is called on an empty array, it often raises an IndexError
        raise IndexError("pop from empty DynamicArray")
        # Alternatively, return a specific sentinel value if an int is always expected
        # return -1 # Example if a specific int must always be returned

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity