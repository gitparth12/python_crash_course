class NumberRange:  # target class
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.curr = start # stores state of the iterator

    def __iter__(self):  # returns iterator instance
        return self
    
    def __next__(self): # returns the object for every iteration
        if self.curr > self.end:
            raise StopIteration()
        
        return_val = self.curr
        self.curr += 1
        return return_val
    

if __name__ == '__main__':

    for i in NumberRange(0, 10):
        print(i)