#!/usr/bin/env python
# coding: utf-8

# In[1]:


table_size = 2063


# In[2]:


class Node:
    def __init__(self, key , value ):
        #this is an initial function that every class should have
        # the properties is similar to constructor=> initial var when object called
        self.key = key
        self.value=value
        self.next = None # assign none is one way to reset it to original ( empty state )


# In[3]:


class Hash_table:
    def __init__(self):
        self.capacity = table_size
        self.size = 0
        self.bucket = [None]*self.capacity
    def __hash__(self, key ):
        hashsum = 0
        for idx, c in enumerate (key):
        # enumerate () function add a counter to an interation
        # we loop through each character in the key with counter idx
            #hashsum+= ( idx + len(key))**ord(c) # ord() given string return integer in unicode
            hashsum+= ( idx + len(key))

            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value ):
        self.size +=1 # increase counter when we add element
        index = self.__hash__(key) # index  return value of function Hash

        node = self.bucket[index] # assign the bucket[index] to new node
        #case 1 : if node = NULL
        if node is None:
            self.bucket[index] = Node(key, value)
            return
        # case 2 : if we have collision
        # we have to keep track of the previous node
        prev = node
        while node is not None: # using while loop here, cause we perform on linklist
            prev = node
            node = node.next # this two step run throught the end of the list
        prev.next = Node(key, value)

    def find ( self, key ):
        index = self.__hash__(key)
        node = self.bucket[index]
        #case 1 : found and not found
        while node is not None and node.key != key:
            node = node.next # run through the list and stop until Node.key == key

        if node is None:
            print ("Element not found!")
            return None
        else:
            print ("Element", key,"has value :")
            return node.value

    def remove(self, key):
        # 1. Compute hash
        index = self.hash(key)
        node = self.bucket[index]
        prev = None
        # 2. Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none
        if node is None:
            # 3. Key not found
            return None
        else:
            # 4. The key was found.
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                self.buckets[index] = node.next  # May be None, or the next match
            else:
                prev.next = prev.next.next  # LinkedList delete by skipping over
            # Return the deleted result
            return result


# In[4]:


import itertools
list_word = []
def generator (list_word):
    chrs = 'abcdf' # the list character of combination 
    #list_word=[]
    min_length, max_length = 2, 3  # thr pssword 2->3 can replace this one with multiple value 
    for n in range(min_length, max_length+1):
        for xs in itertools.product(chrs, repeat=n):
            #print (''.join(xs))
            list_word.append(''.join(xs))
            #print ( len (list_word) ) # prin
    return list_word


print (generator(list_word))

list_val =[]
# itteration the list_ward to encrypt each element: 

for index in range(len(list_word)): 
    # from here will be the encryption that encrypt each element in the list 
    key = list_word[index]
    val = [ord(key[0])] # find the asi value 
    j = len(key)
    val1 = ord(key[0])/len(key)
    k = 0 # incre counter
    # while j < len(key):
    for i in key:
        val.append(((ord(i)) * (j*j) * val1))
        k += 1 # increase the counter 
        list_val.append(val)

print()
print (list_val)  

print ( "size of the wordlist: ", len (list_word) )

my_table = Hash_table() 

for index in range ( len(list_val) and len (list_word) ):
    key_insert = list_val[index]
    value_insert = list_word[index]
    my_table.insert (list_val[index],list_word[index])
    

print ()
my_table.find (list_val[2])
    
    

        
#print (list_word)


# In[6]:


key = "kaod"
encryptedVal = [ord(key[0])]
keyLength = len(key)
val1 = ord(key[0])/len(key)
#k = 0
# while j < len(key):
for i in key:
    encryptedVal.append(((ord(i)) * (keyLength * keyLength) * val1))
   # k += 1
print(encryptedVal)

# val.append((val[k] + (ord(i)) * (j * j) * val1))

#Decryption-----------------------
val2 = (encryptedVal[0]/(len(encryptedVal)-1))
lengthSqr = ((len(encryptedVal)-1) * (len(encryptedVal)-1))

decryptedValues = []
for i in encryptedVal[1:len(encryptedVal)]:
    valToDecrypt = ((i/lengthSqr)/val2)
    decryptedValues.append(chr(int(valToDecrypt)))
    #print(chr(int(randVal)))

print(decryptedValues)


# In[ ]:




