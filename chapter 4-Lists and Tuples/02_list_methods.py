friends = ["qazi", 3.1414, False, "ali"]
friends.append("hamza") #add an element to the end of the list
print(friends)
unsort = [3, 1, 4, 2]
unsort.sort(reverse=True) #sort method
print(unsort)
unsort.sort(reverse=False)
print(unsort)
unsort.insert(4,5) #insert method
print(unsort)
p1 = unsort.pop(4) #pop method
print(unsort)
print(p1)
unsort.remove(2) #remove method
print(unsort)