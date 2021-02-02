"""
This program takes the total bill, tip percentage and number of people to split the bill as an input.
It calculates the per head amount and displays it.
"""

# Greet the user
print('Welcome to the Tip Calculator!')

# Get the total bill from user and convert it into floating point number
total_bill = float(input('What was the total bill? $'))

# Get the tip percentage from the user
tip_percent = float(input('What percentage tip would you like to give? 10, 12, or 15? '))

# Get the number of people from the user
num_of_people = int(input('How many people to split the bill? '))

# # Calculate the tip amount and add it to the total bill
# tip_amount = total_bill * tip_percent / 100
# total_bill += tip_amount

# Alternate Method
# Calculate the total bill as e.g., total_bill = total_bill * 1.12
# Here total_bill times 1 will be the total_bill and total_bill times 0.12 will be the 12 percent tip amount
# In the code below the tip percent will be as per the user input
total_bill *= (1 + tip_percent / 100)

# Calculate the per head amount
per_head = round(total_bill / num_of_people, 2)

# Display the per head amount
print(f'Each person should pay: ${per_head:.2f}')
