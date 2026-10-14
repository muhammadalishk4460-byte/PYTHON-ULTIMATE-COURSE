a1 = {1,2,3,4,5}
a2 = {1,6,7,5,9}

print(a1.union(a2)) #union:adds two sets
print(a1.intersection(a2))  #intersection:takes common between sets
print(a1.difference(a2))    #print elements that are not common
print(a1.symmetric_difference(a2))  #print elements that are not commom from both sets.
print(a1.issubset(a2))
'''
{1} is a subset of a2,because 1 is in a2.
{1,2} is not a subset of a2
'''
print(a1.issuperset(a2))
'''
a1 is a supersubset of a2 
if its subset contains all 
the elements in a2 '''
print(a1.isdisjoint(a2))    #check that if both sets have no common elements.
