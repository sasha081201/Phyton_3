class BinTree:
    def __init__(self, value, pre=None):
        self.value = value
        self.pre = pre
        
    def get_value(self):
        return self.value
    
    def get_pre(self):
        return self.pre
    
class LinkedLiset:
    def __init__(self):
        self.start = None
        self.length = 0
        self.last = None
        
    def add(self, value):
        elem = BinTree(value)
        if self.last is None:
            self.start = elem
            self.last = elem
        else:
            self.last.pre = elem
            self.last = elem
        self.length += 1
    
    def __len__(self):
        return self.length
    
    def __getitem__(self, idx):
        if idx >= self.length:
            raise IndexError("Index out of range")
        current = self.last
        for i in range(idx):
            #current = current.get_pre()
            current.get_value()
            current = current.get_pre()
        
    def __iter__(self):
        self.__curr = self.start
        return self
        
    def __next__(self):
        if self.__curr is None:
            raise StopIteration()
        val = self.__curr.get_value()
        self.__curr = self.__curr.get_pre()
        #val = self.__curr.get_value()
        return val


lst = LinkedLiset()
for i in range(10):
    lst.add(i*i)
    
for i in lst:
    print(i)