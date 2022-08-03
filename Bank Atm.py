class Atm:
    def __init__(self,cardNo,pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo
    
    language = input("Select your Language: ")
    pinNo = int(input("Enter 4-digit Pin Number: "))
    cardNo = int(input("Enter your Card Number: "))
    balance = 25000
    def balanceEnquiry():
        balance = 25000
        print("Your Balance:- ",balance)
    
    def moneyWithdraw():
        amount = int(input("Enter your Amount: "))
        print("Successfuly Money Withdraw!")

    print("Choose Action by enter a or b")
    print("a. Money Withdraw")
    print("b. Balance Enquiry")
    action = input()

    if(action == "a"):
        moneyWithdraw()
    elif(action == "b"):
        balanceEnquiry()
    else:
        print("Error!")
