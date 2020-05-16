import hashlib
import time

class Block:
         def __init__(self, timestamp, data, previous_hash):
                  self.timestamp = timestamp
                  self.data = data
                  self.previous_hash = previous_hash
                  self.hash = self.calc_hash(data)
                  
         def calc_hash(self,data):
                  sha = hashlib.sha256()
                  hash_str = data.encode('utf-8')
                  sha.update(hash_str)
                  return sha.hexdigest()
class Blockchain:
         def __init__(self):
                  self.head=None
                  self.length=0
                  
         def add(self,data):
                  if self.head is None:
                           self.head=Block(time.time(),data,None)
                           self.length+=1
                  else:
                           new_block=Block(time.time(),data,self.head)
                           self.head=new_block
                           self.length+=1
         def search(self,data):
                  if self.head is None:
                           print("Blockchain is empty")
                  else:
                           c=0
                           temp=self.head
                           while temp:
                                    if temp.data==data:
                                             c=c+1
                                             print('Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(temp.data, temp.timestamp, temp.hash))
                                    temp=temp.previous_hash
                           if c==0:
                                    print("Not Found")
         def size(self):
                  return self.length
         def convert_to_list(self):
                  output_list=[]
                  temp=self.head
                  while temp:
                           output_list.append([temp.data,temp.timestamp,temp.hash])
                           temp=temp.previous_hash
                  return output_list

blockchain = Blockchain()

print(blockchain.size())
# 0
print(blockchain.convert_to_list())
# []

blockchain.add('My name is First')
print(blockchain.size())
# 1
print(blockchain.convert_to_list())
#[['My name is First', 1589044995.61107, '40f2e64b2ee27489581295f59a01f49926dd0bc5eb
#  e1bfc827e933f3ad531c39']]

blockchain.add('My name is Second')
blockchain.add('My name is Third')
blockchain.add('My name is Forth')
blockchain.add('My name is Fifth')
print(blockchain.size())
# 5
print(blockchain.convert_to_list())
#[['My name is Fifth', 1589044995.6336524, '57b338696571388be3c5fbba8d33fcc6a1363a4c0
#  a4200a4962e1d1c61f41b08'], ['My name is Forth', 1589044995.6336524, '5bd0efd137cbc
#  34eee92f1f790ecbe4ec5ba30fc8fa25501a45ea65663ed5e8c'], ['My name is Third', 158904
#  4995.6336524, '291e438241fa0f58de279e0e41b82852722fc27eae76b47d82fb82e5370cf1fd'],
# ['My name is Second', 1589044995.6336524, '0a644d791011e00a6865b2354018b74f6695d594
#  2977ecb4cbbca80b382a05c3'], ['My name is First', 1589044995.61107, '40f2e64b2ee274
#  89581295f59a01f49926dd0bc5ebe1bfc827e933f3ad531c39']]

# Testing the "search function"
blockchain.search('My name is Forth')
# Block is:
# Data: My name is Forth
# Timestamp: 1589044995.6336524
# Hash: 5bd0efd137cbc34eee92f1f790ecbe4ec5ba30fc8fa25501a45ea65663ed5e8c


# Edge Cases:
blockchain.search('My name is Prateek')
# Not Found

blockchain = Blockchain()
blockchain.search('My name is Prateek')
# Blockchain is Empty
                           
      
