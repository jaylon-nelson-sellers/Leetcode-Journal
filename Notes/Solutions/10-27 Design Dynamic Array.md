
class DynamicArray:

    def __init__(self, capacity: int):

        self.arr = [0] * capacity

        self.cap = capacity

        self.size = 0

  

    def get(self, i: int) -> int:

        print(f"Get {self.arr[i]}")

        return self.arr[i]

  

    def set(self, i: int, n: int) -> None:  

        self.arr[i] = n

        print(f"Set {self.arr[i]}")

        print(f"Arr is now: {self.arr}")

  

    def pushback(self, n: int) -> None:

        if self.size == self.cap:

            self.resize()

        print(f"Push {self.arr[self.size]}")

        self.arr[self.size] = n

        self.size += 1

        print(f"Arr is now: {self.arr}")

    def popback(self) -> int:

        self.size -= 1

        print(f"Pop {self.arr[self.size]}")

        temp = self.arr[self.size]

        self.arr[self.size] = 0

        print(f"Arr is now: {self.arr}")

        return temp

  

    def resize(self) -> None:

        print(f'Resize to {self.cap*2}')

        cap = self.cap

        temp = [0] * cap

        self.arr += temp

        self.cap *= 2

        print(f"Arr is now: {self.arr}")

  

    def getSize(self) -> int:

        print(f'Size is {self.size}')

        return self.size

    def getCapacity(self) -> int:

        print(f'Cap is {self.cap}')

        return self.cap