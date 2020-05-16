import os
def find_files(suffix, path):
         file_path=[]
         if suffix == '':
                  return []

         if len(os.listdir(path)) == 0:
                  return []
         else:
                  for i in os.listdir(path):
                           if os.path.isfile(os.path.join(path, i)):
                                    if i.endswith('.'+suffix):
                                             file_path.append(os.path.join(path, i))
                           else:
                                    for j in find_files(suffix,os.path.join(path, i)):
                                             file_path.append(j)
         return file_path



# Testing preparation	
path_base = os.getcwd()

print(find_files('c','testdir'))
# Output:- ['a.c', 'b.c', 'a.c', 't1.c']

print(find_files('',path_base))
#Output:- []

print(find_files('z',path_base))
#Output:-[]

print(find_files('h',path_base))
# Output:- ['a.h', 'b.h', 'a.h', 't1.h']
