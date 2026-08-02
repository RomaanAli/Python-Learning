class Product:

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("----------------------------------------------")
        print(f"ID       : {self.product_id}")
        print(f"Name     : {self.name}")
        print(f"Price    : {self.price}")
        print(f"Quantity : {self.quantity}")

class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self):

        product_id = int(input("Enter Product ID: "))

        for product in self.products:
            if product.product_id == product_id:
                print("Product ID already exists.")
                return

        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))

        product = Product(product_id, name, price, quantity)
        self.products.append(product)

        print("Product Added Successfully.")

    def display_products(self):

        if not self.products:
            print("Inventory Empty.")
            return

        for product in self.products:
            product.display()

    def search_product(self):

        product_id = int(input("Enter Product ID: "))

        for product in self.products:

            if product.product_id == product_id:
                print("Product Found")
                product.display()
                return

        print("Product Not Found.")

    def update_product(self):

        product_id = int(input("Enter Product ID: "))

        for product in self.products:

            if product.product_id == product_id:

                product.name = input("New Name: ")
                product.price = float(input("New Price: "))
                product.quantity = int(input("New Quantity: "))

                print("Product Updated.")
                return

        print("Product Not Found.")

    def delete_product(self):

        product_id = int(input("Enter Product ID: "))

        for product in self.products:

            if product.product_id == product_id:
                self.products.remove(product)
                print("Product Deleted.")
                return

        print("Product Not Found.")

    def sell_product(self):

        product_id = int(input("Enter Product ID: "))
        amount = int(input("Quantity to Sell: "))

        for product in self.products:

            if product.product_id == product_id:

                if amount > product.quantity:
                    print("Insufficient Stock.")
                    return

                product.quantity -= amount

                print("Sale Successful.")
                return

        print("Product Not Found.")

    def total_inventory_value(self):

        total = 0

        for product in self.products:
            total += product.price * product.quantity

        print(f"Total Inventory Value = {total}")


inventory = Inventory()

while True:

    print("\n------------ Inventory Management -------------")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Sell Product")
    print("7. Total Inventory Value")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        inventory.add_product()

    elif choice == "2":
        inventory.display_products()

    elif choice == "3":
        inventory.search_product()

    elif choice == "4":
        inventory.update_product()

    elif choice == "5":
        inventory.delete_product()

    elif choice == "6":
        inventory.sell_product()

    elif choice == "7":
        inventory.total_inventory_value()

    elif choice == "8":
        print("------Program Finished---------")
        break

    else:
        print("Invalid Choice.")