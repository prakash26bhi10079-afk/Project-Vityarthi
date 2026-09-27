# ============================================
#               CAFE BILLING SYSTEM
# ============================================

# Menu definition using data structures (dictionaries) for scalable management
MENU = {
    "Burger": 250,
    "Pizza": 300,
    "Pasta": 200,
    "Fries": 150,
    "Coke": 100,
}

print("\n" + "=" * 44)
print("             WELCOME TO OUR CAFE")
print("=" * 44)

# Dynamic order collection with input validation
order_summary = []
subtotal = 0.0

for item, price in MENU.items():
    while True:
        try:
            qty_input = input(f"Enter quantity of {item:7s} (Price: ₹{price}): ")
            quantity = int(qty_input) if qty_input.strip() else 0
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")

    if quantity > 0:
        item_total = quantity * price
        subtotal += item_total
        order_summary.append({
            "item": item,
            "qty": quantity,
            "price": price,
            "total": item_total,
        })

# Calculations
discount = subtotal * 0.10 if subtotal > 1000 else 0.0
taxable_amount = subtotal - discount

sgst = taxable_amount * 0.09
cgst = taxable_amount * 0.09
final_amount = taxable_amount + sgst + cgst

# ============================================
#                  FINAL BILL
# ============================================

print("\n" + "=" * 44)
print("                  CAFE BILL")
print("=" * 44)
print(f"{'Item':<12} {'Qty':<6} {'Price':<10} {'Total':<10}")
print("-" * 44)

if not order_summary:
    print("No items ordered.")
else:
    for entry in order_summary:
        print(
            f"{entry['item']:<12} "
            f"{entry['qty']:<6} "
            f"₹{entry['price']:<9.2f} "
            f"₹{entry['total']:<9.2f}"
        )

print("-" * 44)
print(f"{'Subtotal':<28}: ₹{subtotal:8.2f}")
if discount > 0:
    print(f"{'Discount (10%)':<28}: -₹{discount:7.2f}")
print(f"{'SGST (9%)':<28}: ₹{sgst:8.2f}")
print(f"{'CGST (9%)':<28}: ₹{cgst:8.2f}")
print("-" * 44)
print(f"{'FINAL AMOUNT':<28}: ₹{final_amount:8.2f}")
print("=" * 44)
print("          THANK YOU! VISIT AGAIN")
print("=" * 44)