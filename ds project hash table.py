class HashTable():
    def __init__(self,size):
        #self.capacity=[0 for  i in range(size)]
        #print(self.capacity)
        self.size=size
        self.Capacity=[None for i in range(self.size)]
        self.buckets=[None]*self.size
        self.next=0
       # print(self.buckets)
    def Hash(self,key):
        HashSum = key % self.size
        return HashSum
    def ReHash(self,key):
        ReHashSum = (key+1) % self.size
        return ReHashSum
    def Insert(self, key, value):
        if self.next==self.size:
            raise Exception ("Array is over flow")
        HashSum=key % self.size 
        if self.buckets[HashSum ] == None:
            self.Capacity[HashSum]=key
            self.buckets[HashSum ]= value
            self.next=self.next+1
            return self.buckets
        else:
            #HashSum=(key+1)% self.size
            Hashsum=self.ReHash(HashSum)
             
            while self.Capacity[HashSum] !=None:# and self.Capacity(key)!=key:
                HashSum=self.ReHash(HashSum)
                #ReHashSum=(key+1)%self.size
            self.Capacity[HashSum]=key
            self.buckets[HashSum]= value
            self.next=self.next+1
            return  self.buckets        
       
 
    def Print(self):
           print (self.buckets)
    def Search(self,key):
        hashed=self.Hash(key)
        while self.Capacity[hashed] is not  None:
            if self.Capacity[hashed]==key:
                return self.buckets[hashed]
            mod=hashed+1%self.size
            if self.Capacity[mod]==key:
                return self.buckets[mod]
        raise Exception ("Key is not found in bucket")
    def Delete(self,key):
        hashed = self.Hash(key)
        if self.Capacity[hashed] == key:
            item = self.buckets[hashed]
            self.buckets[hashed] = None
            self.Capacity[hashed] = None
            return self.buckets
        else:
            count = 0
            hashed = self.ReHash(hashed)
            while self.Capacity[hashed] != key and count != self.size:
                hashed = self.ReHash(hashed)
                count = count+1

            if count == self.size:
                return "Key not in hash table"
            else:
                item = self.buckets[hashed]
                self.buckets[hashed] = None
                self.Capacity[hashed] = None
                return self.buckets

                
h=HashTable(10)             
(h.Insert(25,'Naufil'))
#h.Print()
(h.Insert(31,'boy'))
#h.Print()
(h.Insert(62,'Girl'))
#h.Print()
(h.Insert(32,'faiz'))
#h.Print()
(h.Insert(85,'abdulla'))
#h.Print()
(h.Insert(76,'sufiyan'))
#h.Print()
(h.Insert(50,'Nadeem'))
#h.Print()
(h.Insert(114,'ali'))
h.Print()


'''print(h.Search(25))
print(h.Search(31))
print(h.Search(62))
print(h.Search(32))
print(h.Search(85))
print(h.Search(76))
print(h.Search(50))
print(h.Search(114))'''


print(h.Delete(85))
print(h.Delete(32))
print(h.Delete(31))
print(h.Delete(76))
print(h.Delete(114))
print(h.Delete(50))
print(h.Delete(62))
print(h.Delete(25))
