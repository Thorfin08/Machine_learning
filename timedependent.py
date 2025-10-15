import time

class bank:
    def __init__(self,account_number,password):
        self.account_number=account_number
        self.__password=password
    def access_password(self):
        return self.__password
        
    def update_password(self,new_password):
        print(f"Your new password is{new_password}")
        
    
ob1=bank("0050508010356", "@prashan123")
print(ob1.account_number)
print(ob1.access_password())  
time.sleep(10)
change_password=input("Change your password.(now/remind me later)").strip().lower()
if change_password=="now":
    new_password=input("Enter your new password:")
    ob1.update_password(new_password)
elif change_password=="remind me later":
    print("We will remind you later")

