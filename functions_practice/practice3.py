# Create an e-commerce cart where:

# Products have name & price

# User can:

# Add items

# Remove items

# View cart

# Calculate total bill

# Apply 10% discount if bill > ₹3000


cart = {}

def add_item(name, price):
    cart[name] = price
    print(f"{name} added to cart")

def remove_item(name):
    if name in cart:
        del cart[name]
        print(f"{name} removed")
    else:
        print("Item not found")

def view_cart():
    if not cart:
        print("Cart is empty")
    else:
        for item, price in cart.items():
            print(item, ":", price)

def calculate_total():
    total = sum(cart.values())
    if total > 3000:
        total *= 0.9
    return total

add_item("Shoes", 1800)
add_item("Watch", 1500)
view_cart()
print("Total Bill:", calculate_total())