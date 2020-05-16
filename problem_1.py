class LRU_Cache(object):

    def __init__(self, capacity):
             self.cache=dict({})
             self.size=capacity
             self.lru=[]

    def get(self, key):
             if key not in self.cache:
                      return -1
             else:
                      self.lru.remove(key)
                      self.lru.append(key)
                      return self.cache[key]

    def set(self, key, value):
             if self.size== 0:
                 print("The cache capacity is zero")
                 return
             if key in self.cache:
                      self.cache[key]=value
                      if key in self.lru:
                               self.lru.remove(key)
                               self.lru.append(key)
                      else:
                               self.lru.append(key)
             else:
                      if len(self.cache)==self.size:
                               p=self.lru[0]
                               self.lru.remove(p)
                               del self.cache[p]
                               self.cache[key]=value
                               self.lru.append(key)
                      else:
                               self.cache[key]=value
                               self.lru.append(key)


# Given Test Case:
test_cache = LRU_Cache(5)
test_cache.set(1, 1)
test_cache.set(2, 2)
test_cache.set(3, 3)
test_cache.set(4, 4)

print(test_cache.get(1))
# Output:- returns 1
print(test_cache.get(2))
# Output:- returns 2
print(test_cache.get(9))
# Output:- returns -1 because 9 is not present in the cache

test_cache.set(5, 5)
test_cache.set(6, 6)

print(test_cache.get(3))
# output:- returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Test Case:
edge_cache = LRU_Cache(2)
edge_cache.set(1, 1)
edge_cache.set(2, 2)
edge_cache.set(1, 10)
print(edge_cache.get(1))
# Output:- return 10
print(edge_cache.get(2))
# Output:- return 2

edge_cache1 = LRU_Cache(0)
edge_cache1.set(1, 1)
# Output:- print "The cache capacity is zero"
print(edge_cache1.get(1))
# Output:- return -1
