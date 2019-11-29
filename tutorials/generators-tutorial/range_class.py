# range function using a class

class Myrange:
    def __init__(self, start, end, by=1):
        self.start = start
        self.end = end
        self.cur = self.start
        self.by = by
        
    def __iter__(self):
        return(self)
    
    def __next__(self):
        if self.cur + self.by < self.end:
            cur = self.cur
            self.cur += self.by
            return(cur)
        
        raise(StopIteration)


if __name__ == "__main__":
    r = MyRange(1, 15, 2)
    for i in r:
        print(i)