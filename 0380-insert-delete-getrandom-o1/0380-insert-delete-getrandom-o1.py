class RandomizedSet:

    def __init__(self):
        self.rands=set()
        

    def insert(self, val: int) -> bool:
        if val not in self.rands:
            self.rands.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.rands:
            self.rands.discard(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        rev=self.rands.pop()
        self.rands.add(rev)
        return rev

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()