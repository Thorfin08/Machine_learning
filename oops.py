class bank_management_system:
    def __init__(self,Account_name,Account_number,Balance):
        self.Account_name=Account_name
        self.Account_number=Account_number
        self.Balance=Balance
    def credit(self,ammount,Account_number):
        self.Balance += ammount
        print(f"The ammount of {ammount} has been credited to {Account_number}")
        print(f"Your New Balance is {self.Balance}")
    def debit(self,ammount,Account_number):
        self.Balance -= ammount
        print(f"The ammount of {ammount} has been debited from {Account_number}")
        print(f"Your New Balance is {self.Balance}")
    def get_New_Balance(self):
        return self.Balance
    
Account1=bank_management_system("Subha Katuwal", "00504020604420", 1000)
Accout2=bank_management_system("Sambodan Ghorasaini", "00504020604421", 2000)    
Account1.credit(500,Account1.Account_number)
Account1.debit(200,Account1.Account_number) 
    

    



