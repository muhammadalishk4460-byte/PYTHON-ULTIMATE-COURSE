import random
choices = {"snake":1,"water":2,"gun":3}
reverse = {1:"snake",2: "water",3: "gun"}
player = input("enter your choice: ").lower()
if player not in choices:
    print("invalid syntax!.")
else:
    p = choices[player]
    comp = random.randint(1,3)
    c_choices = reverse[comp]
    print(f"you chose: {player}")
    print(f"computer chooses: {c_choices}")
    if (comp == p):
        print("its a draw!.")
    else:
        if(comp==1 and p == 2):
            print("you lose!.")
            print("Try next time.")
        elif(comp==1 and p ==3):
            print("you win!.")
        elif(comp==2 and p ==3):
            print("you lose!.")
            print("Try next time.")
        elif(comp==2 and p ==1):
            print("you win!.")
        elif(comp==3 and p ==1):
            print("you lose!.")
            print("Try next time.")
        elif(comp==3 and p ==2):
            print("you win!.")
        