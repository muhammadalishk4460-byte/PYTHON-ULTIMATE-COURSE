import random
class train():
    def __init__(self,train_no):
        self.train_no = train_no
    def book(self,fro,to):
        print(f"ticket is booked in train number: {self.train_no}")
    def getstatus(self):
        print(f"train no :{self.train_no} is on time")
    def getfare(self,fro,to):
        print(f"Ticket fare in train no: {self.train_no} from {fro} to {to} is {random.randint(222,555)}")
t = train(123456)
t.book("gujranwla","lahore")
t.getstatus()
t.getfare("gujranwla","lahore")
    