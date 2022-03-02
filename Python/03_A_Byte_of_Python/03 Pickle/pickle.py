''' Picle 

консервация объектов Python в файл'''

import pickle

my_object = [[1,2,3],[5,6,7]]
dumpfilename = 'my_object_dump.data'

print(my_object)


with open(dumpfilename, 'wb') as f:
    pickle.dump(my_object, f)

''' 
f = open(dumpfilename, 'wb')        # idk why this didn't work ¯\_( ͡° ͜ʖ ͡°)_/¯
pickle.dump(my_object, f)
'''

f.close()

del my_object


ff = open(dumpfilename, 'rb')
my_object = pickle.load(ff)
print(my_object)

