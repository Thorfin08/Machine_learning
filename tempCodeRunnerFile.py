class Account:
    def __init__(self,Account_Number,Account_Password):
        self.Account_Number=Account_Number
        self.__Account_Password=Account_Password
    #Creating a method that can access the private Attributes
    def access_password(self):
        return self.__Account_Password

object1=Account("00504020604420", "Subha@123")

print(object1.access_password())  # Accessing the private attribute using the method
        
 