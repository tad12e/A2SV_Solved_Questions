class ProductOfNumbers:

    def __init__(self):
        
        self.ans=[1]
        self.size=0
        

    def add(self, num: int) -> None:
        if num==0:
            self.ans=[1]
            self.size=0
        else:
            self.ans.append(self.ans[self.size]*num)
            self.size+=1
       
        

    def getProduct(self, k: int) -> int:
        if k> self.size:
            return 0
        return self.ans[self.size]//self.ans[self.size-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)