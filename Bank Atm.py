class Atm:
    def __init__(self,cardNo,pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo

    def cashWithDrowl(self):
        print("Cash WithDrowl")

    def balanceEnquiry(self):
        print("Balance Enquiry")

user1 = Atm(100,200)
user2 = Atm(300,400)

user1.cashWithDrowl()
user2.balanceEnquiry()