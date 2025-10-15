class account:
    def __init__(self,name,password):
        self.name=name
        self.__password=password
    
    def get_password(self):
        return self.__password
    def update_password(self,new_password):
        self.__password = new_password
    
    
ob1=account("subha","@lasjdiehf")
Change_password = input("Do you want to change your password? (yes/no): ").strip().lower()
if Change_password=="yes":
    new_password=input("Enter your new password:")
    ob1.update_password(new_password)

print(f"Your new password is:{ ob1.get_password()}")