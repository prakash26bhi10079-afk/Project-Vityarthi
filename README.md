# Cafe Billing System

## Project Description

The **Cafe Billing System** is a simple Python-based project designed to calculate the total bill for items ordered in a cafe.

The program takes the quantity of different food items from the user, calculates the cost of each item, applies a discount if applicable, calculates SGST and CGST, and finally displays the total payable amount.

## Features

* Takes quantity of different cafe items as input.
* Calculates the cost of each individual item.
* Calculates the total cost of the order.
* Provides a 10% discount for orders above ₹1000.
* Calculates 9% SGST.
* Calculates 9% CGST.
* Displays a properly formatted final bill.

## Menu

| Item   | Price |
| ------ | ----: |
| Burger |  ₹250 |
| Pizza  |  ₹300 |
| Pasta  |  ₹200 |
| Fries  |  ₹150 |
| Coke   |  ₹100 |

## Concepts Used

This project is created using basic Python concepts:

* Variables
* Assignment statements
* `input()`
* `print()`
* Arithmetic operators
* `if-else` statements
* Basic calculations

## Formula Used

### Item Cost

`Item Cost = Quantity × Price`

### Discount

If total cost is greater than ₹1000:

`Discount = Total Cost × 10%`

Otherwise:

`Discount = ₹0`

### SGST

`SGST = Total Cost × 9%`

### CGST

`CGST = Total Cost × 9%`

### Final Amount

`Final Amount = Total Cost - Discount + SGST + CGST`

## Requirements

* Python 3.x
* Any Python-compatible IDE or code editor

## How to Run

1. Install Python 3.x.
2. Open the project in a Python-compatible editor.
3. Run the Python program.
4. Enter the quantity of each item when prompted.
5. The final cafe bill will be displayed.

## Project Structure

```text
Cafe-Billing-System/
│
├── cafe_billing.py
├── README.md
└── statement.md
```

## Limitations

* No database is used.
* No file handling is used.
* No loops or functions are used.
* The menu and prices are fixed in the program.
* The program handles one order at a time.

## Conclusion

The Cafe Billing System demonstrates how basic Python programming concepts can be used to create a practical billing application. It provides a simple way to calculate item costs, discounts, taxes, and the final bill.
