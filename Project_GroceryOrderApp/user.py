
import admin as ad

#a=User(,,,,)#
#b=User(,,,)
#after a -login_info={"a":'a'}
#after b -login_info={"a":'a','b':'b'}

class User:
    login_info = {"Sagar": "Sagar@0810"}

    def __init__(self, name, phoneno, email, address, password):
        self.name = name
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.name] = self.password
        self.profile={"Name":name}
        self.order_history = {}

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("You're are successfully logged in.....")
            return True
        else:
            print("SORRY! These are the Wrong Credentials")
            return False


    def place_order(self):
        print("What you want to order here in the Inventory")
        print(ad.show_inven())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            n=int(input("Enter how many items do you want to Order"))
            x=0
            for i in range(n):
             
             itemid = int(input("Enter the Item id here: "))
             quan = int(input("Enter the quantity of the item: "))
             x += ad.inven[itemid]["Price"] * quan
            again_ask = input("Are you still want to order this Enter YES or NO")
            if again_ask == "YES":
                print(f'''Your item name is {ad.inven[itemid]["ItemName"]}''')
                print(f'''Price of your Item is {ad.inven[itemid]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.order_history[itemid] = {
                    "Item Name": ad.inven[itemid]["ItemName"],
                    "Price": ad.inven[itemid]["Price"],
                    "Quantity": quan
                }
                final_stock = ad.inven[itemid]["Stock"] - quan
                ad.inven[itemid]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

#def cnu()
       

