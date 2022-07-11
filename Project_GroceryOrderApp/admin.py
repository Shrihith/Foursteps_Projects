admin_keys = {"Shri": "Shri@0930"}

inven = {1: {'ItemName': 'Aashirvad Ata', 'ItemID': 1, 'Price': 250, 'Stock': 14},
        2: {'ItemName': 'Surf Excel', 'ItemID': 2, 'Price': 150, 'Stock': 20},
        3: {'ItemName': 'Cake', 'ItemID': 3, 'Price': 300, 'Stock': 5}}
#nested dict

def add_new_item():
    itemname = input("Enter the Item name: ")
    itemid = int(input("Enter the item id: "))
    price = int(input("Enter the price of the item: "))
    stock = int(input("Enter the stock value of item: "))
    inven[itemid] = {
        "ItemName": itemname,
        "ItemID": itemid,
        "Price": price,
        "Stock": stock
    }
    print("The Item"+itemname+ "is successfully added")
    return inven


def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the price of item"))
    d = int(input("Enter the stock of the item"))
    inven[item]["ItemName"] = a
    inven[item]["Price"] = b
    inven[item]["Stock"] = d
    print("*****Edited item successfully*****")
    return inven

def show_inven():
    print("*****HERE IS THE INVENTORY OF RAKSHAK MART*****")
    for i in inven:
        print("Item Name: ",inven[i]["ItemName"])
        print("Price: ",inven[i]["Price"],"INR")
        print("Item ID: ",inven[i]["ItemID"])

def remove_item():
    d = int(input("Enter the Item id which you want to exit"))
    inven.pop(d)
    print("Remove item successfully ")
    return inven
