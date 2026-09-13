import random

class RandomizedSet:

    def __init__(self):
        self._set = {} #val to index in _list
        self.length = 0
        self._list = []
        

    def insert(self, val: int) -> bool:
        if val in self._set: 
            return False
        else: 
            self._list.append(val)
            self.length += 1 
            self._set[val] = self.length - 1
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self._set:
            return False
        else:
            self._set[self._list[-1]] = self._set[val]

            self._list[self._set[val]], self._list[-1] = self._list[-1], self._list[self._set[val]] 
            
            self._list.pop()
            del self._set[val]

            self.length -= 1

            return True
        

    def getRandom(self) -> int:
        return self._list[random.randint(0, self.length-1)]
