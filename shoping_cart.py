class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product):
        if product.name in self.cart:
            self.cart[product.name].quantity += product.quantity
        else:
            self.cart[product.name] = product
        print(f"Added {product.quantity} kg of {product.name} to the cart.")

    def remove_product(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]
            print(f"Removed {product_name} from the cart.")

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.cart.values())
        return total

cart = ShoppingCart()
cart.add_product(Product("Apple", 300, 1.5))
cart.add_product(Product("Banana", 250, 4))
cart.add_product(Product("Grapes", 600, 2))
print(f"Total: Rs.{cart.calculate_total():.2f}")
