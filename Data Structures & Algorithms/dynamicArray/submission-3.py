class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity 
        self.size = 0

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Out of Bound")
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.array[i] = n
        else:
            raise IndexError("Invalid Index")

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Empty Array")
        val = self.array[self.size - 1] 
        self.array[self.size - 1] = None 
        self.size -= 1 
        return val
 

    def resize(self) -> None:
        self.capacity *= 2
        copy = self.capacity * [None]
        for i in range(self.size):
            copy[i] = self.array[i]
        self.array = copy


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
