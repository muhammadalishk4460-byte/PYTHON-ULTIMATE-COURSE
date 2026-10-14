subject1 = int(input("enter marks 1: "))
subject2 = int(input("enter marks 2: "))
subject3 = int(input("enter marks 3: "))
p1 = (subject1/50)*100
p2 = (subject2/50)*100
p3 = (subject3/50)*100
sum = subject1+subject2+subject3
total = (sum/150)*100
print("         PERCENTAGES         ")
print("subject-1 : ,",p1)
if(p1>33):
    print("you are passed in in subject1")
else:
    print("you are failed in this subject")
print("subject-2 : ,",p2)
if(p2>33):
    print("you are passed in in subject2")
else:
    print("you are failed in this subject")
print("subject-3 : ,",p3)
if(p3>33):
    print("you are passed in in subject3")
else:
    print("you are failed in this subject")
print("total percentage : ",total)
if(total>=40):
    print("     CONGRATULATIONS!        ")
    print("     You are passed      ")
else:
    print("     you failed!, try again next year!")
