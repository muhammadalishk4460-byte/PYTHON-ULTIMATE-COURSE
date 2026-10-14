from typing import List,Union,Tuple,Dict
#list of integers
numbers : list[int] = [1,2,3,4,5]
#tuples of string and tuples
persons : str[str,int] = ["ali",22]
#dictionary of str keys and int values
scores : dict[str,int] = ["hamza",23]
#union type for variables that cn hold multiple typles.
identifiers : Union[str,int] = "ic123"
print(numbers)