marks = {"maths":90,    #{"key":value}
         "urdu":99,     #{value:"key"}
         "english":80,
         50:"eng"}
print(marks.items())    #print both keys and values
print(marks.keys())     #print only keys
print(marks.values())   #print only values
marks.update({"urdu":100})
print(marks.get("maths1"))  #returns none
# print(marks["maths1"])  #returns an error
p = marks.pop("maths")
print(p)
p1 = marks.pop()
print(p1)