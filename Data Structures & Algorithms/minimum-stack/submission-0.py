class MinStack:

    def __init__(self):
        self.array = []
        self.minimum_hist = []

    def push(self, val: int) -> None:
        self.array.append(val)

        minimum = val
        if self.minimum_hist:
            minimum = min(self.minimum_hist[-1], val)            
        
        self.minimum_hist.append(minimum)

    def pop(self) -> None:
        result = self.array[-1]
        self.array = self.array[:-1]

        self.minimum_hist = self.minimum_hist[:-1]

        return result

    def top(self) -> int:
        result = self.array[-1]
        return result

    def getMin(self) -> int:
        return self.minimum_hist[-1]
