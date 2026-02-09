from collections import Counter, deque
class FrequencyTracker:

    def __init__(self):
        self.arr=deque([])
        

    def add(self, number: int) -> None:
        self.arr.append(number)
        

    def deleteOne(self, number: int) -> None:
        if len(self.arr)>0 and number in self.arr:
            self.arr.remove(number)
        

    def hasFrequency(self, frequency: int) -> bool:
        dect=Counter(list(self.arr))

        for i in self.arr:
            if dect[i]==frequency:
                return True
        return False

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)