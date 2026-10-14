class employee:
    language = "python"  #this is a class attribute
    salary = 100000

harry = employee()
harry.language = "javascript"  #this is an object or instance attribute
print(harry.language,harry.salary)
