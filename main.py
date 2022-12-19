import Shoppingcartimport as s

# Instantiation
myCart = s.ShoppingCart()
while True:
    print("Add Items...........Press 1")
    print("Remove Items.........Press 2")
    print("Display Items...........Press 3")
    print("Checkout:.......Press 4")
    print("Exit......Press 9")
    option = int(input("Select an option"))
    if option == 1:
        # Access AddItems method using object
        myCart.AddItems()
    elif option == 3:
        myCart.DisplayItems()
    elif option == 2:
        myCart.RemoveItems()
    elif option == 4:
        myCart.Checkout()
    elif option == 9:
        break

