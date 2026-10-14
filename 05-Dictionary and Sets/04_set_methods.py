s = {1,2,3,4,5,6}
print(s,type(s))
s.add(7)    #adds an element at the end
print(s,type(s))
s.update([7,8,9])   #adds some elements at the end
print(s)
s.remove(9) #remove by name if it does'nt exist gives an error
print(s)
s.discard(8)    #remove by name and does not give error if does'nt exist
t = s.copy() #crates a shallow copy
t.clear()   #clear the whole set
a = s.pop()    #remove by index
print(a)
print(s)

