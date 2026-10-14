class employee:
    languge = "python"  #this is a class attribute
    salary = 100000

harry = employee()
print(harry.languge,harry.salary)

rohan = employee()
rohan.name = "rohan"    #this is an object or instance attribute
print(rohan.name,rohan.languge,rohan.salary)

#here name is object attribute and salary
#and language are class attributesas they directly belong to the class