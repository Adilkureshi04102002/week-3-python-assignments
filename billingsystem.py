class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=18):
        self.products = []
        self.tax_rate = tax_rate

    # Add product to bill
    def add_product(self, product):
        self.products.append(product)

    # Calculate subtotal
    def calculate_subtotal(self):
        subtotal = 0

        for product in self.products:
            subtotal += product.get_total()

        return subtotal

    # Calculate tax
    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.tax_rate / 100

    # Calculate final total
    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()

        return subtotal + tax

    # Display final bill
    def display_bill(self):
        print("\n" + "=" * 60)
        print("                    BILLING SYSTEM")
        print("=" * 60)

        print(f"{'Product':<20}{'Price':>10}{'Qty':>8}{'Amount':>12}")
        print("-" * 60)

        for product in self.products:
            amount = product.get_total()

            print(
                f"{product.name:<20}"
                f"{product.price:>10.2f}"
                f"{product.quantity:>8}"
                f"{amount:>12.2f}"
            )

        print("-" * 60)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print(f"{'Subtotal':<45}{subtotal:>12.2f}")
        print(f"{'Tax (18%)':<45}{tax:>12.2f}")
        print(f"{'Final Total':<45}{total:>12.2f}")

        print("=" * 60)


# Create products
product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 800, 2)
product3 = Product("Keyboard", 1500, 1)

# Create bill
bill = Bill()

# Add products to bill
bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

# Display bill
bill.display_bill()