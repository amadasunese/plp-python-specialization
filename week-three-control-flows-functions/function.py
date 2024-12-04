# calculate_discount function
def calculate_discount(price, discount_percentage):
    # Check if discount is 20% or higher
    if discount_percentage >= 20:
        # Apply the discount
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return original price
        return price

# Prompt the user for the orignal price and discount percentage
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage:"))

# Calculate the final price with discount
final_price = calculate_discount(original_price, discount_percentage)

# Display the final price
print(f"The final price after discount is: {final_price:.2f}")