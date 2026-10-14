list = [" apple "," banana "," orange ","  kiwi ","  cherry         "]
new_list = []
remove_word = input("enter the word to remove: ")
for word in list:
    striped_word = word.strip() #stip() removes the extra spaces from both ends.
    if striped_word!=remove_word:
        new_list.append(striped_word)
print("original list: ",list)
print("updated list: ",new_list)
