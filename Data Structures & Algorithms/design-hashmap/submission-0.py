class MyHashMap:

    def __init__(self):
        self.n = 1000
        self.r = 100
        self.arr = [[] for _ in range(self.n)]
        # self.arr1 = [self.arr for _ in range(self.n)]
        # print(self.arr1)
        
        

    def put(self, key: int, value: int) -> None:
        index_r = key%self.n 
        # index_c = key%self.r 
        # print(self.arr[index_r])
        for i, (k,v) in enumerate(self.arr[index_r]):
            if k == key:
                self.arr[index_r][i] = (key, value)
                return 
        self.arr[index_r].append((key,value))
            
        

    def get(self, key: int) -> int:
        index_r = key%self.n 

        for i, (k,v) in enumerate(self.arr[index_r]):
            if k==key:
                return self.arr[index_r][i][1]

        return -1
  

    def remove(self, key: int) -> None:
        index_r = key%self.n
        for i, (k,v) in enumerate(self.arr[index_r]):
            if k==key:
                del self.arr[index_r][i]
                
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)