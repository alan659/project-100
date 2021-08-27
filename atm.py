class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance(self):
        print('ur balance is 500000')
    def withdrawal(self,amount):
        new_amount=50000-amount
        print('u have withdrawn amount'+str(amount)+'ur remaining balance is '+ str(new_amount))

def main():
    card_number=input('insert ur card number ')
    pin_number=input('insert ur pin number ')
    new_user=Atm(card_number,pin_number)
    print('choose ur activity')
    print('1.balance 2.withdrawal')
    activity=int(input('enter activity number'))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")
        
if __name__ == "__main__":
      main()