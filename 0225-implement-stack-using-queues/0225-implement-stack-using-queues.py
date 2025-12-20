class MyStack:

    def __init__(self):  
        self.items=[]

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        if not self.empty==0:
            return self.items.pop()
        else:
            return "empty"

    def top(self) -> int:
        if not self.empty():
            return self.items[-1]
        else:
            return "empty"
        

    def empty(self) -> bool:
        return len(self.items)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()