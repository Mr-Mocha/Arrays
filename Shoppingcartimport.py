class ShoppingCart:
    #Attributes
    total = 0
    itemCount = 0
    promoCode = ""
    cart = []
    payment = ""

    # Methods
    # Add/remove Items, Display Cart, Checkout, Enter Code, Enter Form of Payment

    # Edit method allow user to enter quantity of item of selected
    def AddItems(self):
        print("Shirt - $15.....Press 1")
        print("Shoes - $60.....Press 2")
        print("Pants - $45.....Press 3")
        option = int(input("Enter your selection: "))
        quantity = int(input("How many?...."))
        for num in range (quantity):
            if option == 1:
                self.cart.append("Shirt")
            if option == 2:
                self.cart.append("Shoes")
            if option == 3:
                self.cart.append("Pants")
        print("Item Added")

    # Remove Items method
    def RemoveItems(self):
        self.DisplayItems()
        print("Shirt - $15.....Press 1")
        print("Shoes - $60.....Press 2")
        print("Pants - $45.....Press 3")
        option = int(input("Enter your selection: "))
        if option == 1:
            self.cart.remove("Shirt")
        if option == 2:
            self.cart.remove("Shoes")
        if option == 3:
            self.cart.remove("Pants")
        print("Item Removed")


    def DisplayItems(self):
        print(f'{self.cart.count("Shirt")} Shirts........${self.cart.count("Shirt") * 15}')
        print(f'{self.cart.count("Pants")} Shirts........${self.cart.count("Pants") * 45}')
        print(f'{self.cart.count("Shoes")} Shirts........${self.cart.count("Shoes") * 60}')

    def Checkout(self):
        discount = 0
        self.DisplayItems()
        self.payment = input("Enter your payment type: ")
        self.promoCode = input("Enter a Promo Code: ")
        if self.promoCode == "I'm broke man":
            discount += 10
        elif self.promoCode == "Crispy Dib":
            discount += 25

        if len(self.cart) >= 5:
            discount += 30

        shirtTotal = self.cart.count("Shirt") * 15
        shoesTotal = self.cart.count("Shoes") * 60
        PantsTotal = self.cart.count("Pants") * 45

        print(f"Final Total: ${shirtTotal + PantsTotal + shoesTotal - discount}")
        print(f"Payment Method: {self.payment}")