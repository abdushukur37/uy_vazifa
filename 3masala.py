# 3--------
class User:
    def __init__(self,ism,username,email,yosh,telefon):
        self.ism=ism
        self.username=username
        self.email=email
        self.yosh=yosh
        self.telefon=telefon
    def get_info(self):
        print("Foydalanuvchi:", self.username)
        print("Ismi:", self.ism)
        print("Email:", self.email)
        print("Yoshi:", self.yosh)
        print("Telefon:", self.telefon)
user1=User("Alijon Valiyev", "alijon1994", "alijon1994@gmail.com", 32, "+998901112233")
user2=User("Ali Karimov", "alikarimov", "ali@gmail.com", 25, "+998935556677")
user3=User("Vali Xasanov", "valixasanov", "vali@gmail.com", 28, "+998977778899")
user1.get_info()
print("----------------")
user2.get_info()
print("----------------")
user3.get_info()