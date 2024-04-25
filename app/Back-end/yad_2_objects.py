import datetime



class Yad_2_User:
    def __init__(self, FirstName, LastName, Email, PhoneNumber, UserName, UserPassword, City, UserId=None):
        self.UserId = UserId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.UserName = UserName
        self.UserPassword = UserPassword
        self.City = City


    def __str__(self):
        if self.UserId == None:
            return f"'{self.FirstName}', '{self.LastName}', '{self.Email}', '{self.PhoneNumber}', '{self.UserName}', '{self.UserPassword}', '{self.City}'"
        else:
            return f"{self.UserId}, '{self.FirstName}', '{self.LastName}', '{self.Email}', '{self.PhoneNumber}', '{self.UserName}', '{self.UserPassword}', '{self.City}'"



class Item_For_Sale:
    def __init__(self, ItemId, User: Yad_2_User, ItemName, ItemDescription, ItemPrice, CreationDate):
        self.ItemId = ItemId
        self.User = User
        self.ItemName = ItemName
        self.ItemDescription = ItemDescription
        self.ItemPrice = ItemPrice
        self.CreationDate = CreationDate


