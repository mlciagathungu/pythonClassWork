"""'you're building an e-commerce order processing
system,and you need to calculate discounts, taxes and final prices
for multiple products.instead of writing the same logic
repeatedly,you'll create reusable logic
"""
import tax

price = float(input("Enter the price of the product::"))
discount = float(input("Enter the discount percentage of the  product::"))


def apply_discount(price, discount):
    discount_price = (price * discount / 100)
    return price - discount_price





def apply_tax(price ):
    tax = 5
    tax_price = (price * tax/100)
    return tax_price
def get_final_price(price, discount,tax ):
    discountedPrice = apply_discount(price, discount)
    tax = apply_tax(price)
    final_price = (discountedPrice - tax)
    return (f"The item discount price is {discountedPrice} "
            f"it has a tax of" f"{tax} so the final price is "f"{final_price}")
print(get_final_price(price, discount, tax))










amount = int(input("Enter the amount ::"))
balance = 0
withdrawal_amount = int(input("Enter the withdrawal amount ::"))

def deposit(amount,balance):
    result = balance + amount
    return result
def withdraw(withdrawal_amount):
    current_balance = deposit(amount, balance)
    if current_balance < withdrawal_amount:
        return ("Insufficient "
                "funds")
    else:
        available_balance = current_balance - withdrawal_amount
    return (f"withdrawal success {withdrawal_amount} the balance was at" 
            f"{current_balance} and now the new balance is {available_balance}")
print(withdraw(withdrawal_amount))