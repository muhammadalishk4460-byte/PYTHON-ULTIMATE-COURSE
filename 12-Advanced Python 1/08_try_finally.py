def rain():

    try:
        a = int(input("enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("hey i am inside of finally.")
rain()
#finally mainly use in functions , where there is a return statement .
#return statement stop the further code but finally allows.