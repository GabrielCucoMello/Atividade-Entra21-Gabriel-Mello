def calculate_price(value, **desc_acrescimos):
    
    tax_percentage = desc_acrescimos.get('tax_percentage')    
    if tax_percentage:
        value += value * (tax_percentage / 100)

    discount = desc_acrescimos.get('discount')
    if discount:
        value -= discount

    return value

# exemplo1:
final_price = calculate_price(100.0)
print(final_price)

# exemplo2:
final_price = calculate_price(100.0, discount=5.0)
print(final_price)

#exemplo3:
final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

#exemplo4:
final_price = calculate_price(100.0, tax_percentage=7, discount=5)
print(final_price)