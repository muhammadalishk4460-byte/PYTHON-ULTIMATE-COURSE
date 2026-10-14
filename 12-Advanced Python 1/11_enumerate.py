l = [12,43,65,7,5,344,23]
# index = 0
# for item in l:
#     print(f"the item at index {index} is {item}")
#     index += 1
#this can be simplified by enumerate function
for index,item in enumerate(l):
    print(f"the item at index {index} is {item}")
    