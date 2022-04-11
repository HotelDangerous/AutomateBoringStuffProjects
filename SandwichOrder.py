# This project asks the user to build a sandwich then charges them based on what they made.
import pyinputplus as pyip

sandwich = []  # Empty list which will contain everything about the sandwich

# Using the pyinpuplus module for input validation while asking user to build a sandwich.
choice = pyip.inputMenu(prompt='Choose your bread:\n',
                        choices=['Wheat', 'White', 'Sourdough'], numbered=True)
sandwich.append(choice)  # Appending the users choice to our sandwich list.

choice = pyip.inputMenu(prompt='Choose your protein:\n',
                        choices=['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
sandwich.append(choice)

cheese_or_not = pyip.inputYesNo(prompt='Would you like cheese on your sandwich? ')
if cheese_or_not == 'yes':
    choice = pyip.inputMenu(prompt='Choose your cheese:\n', choices=['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
    sandwich.append(choice)

if pyip.inputYesNo(prompt='Would you like mayo? ') == 'yes':
    sandwich.append('Mayo')
if pyip.inputYesNo(prompt='Would you like Mustard? ') == 'yes':
    sandwich.append('Mustard')
if pyip.inputYesNo(prompt='Would you like Lettuce? ') == 'yes':
    sandwich.append('Lettuce')
if pyip.inputYesNo(prompt='Would you like Tomato? ') == 'yes':
    sandwich.append('Tomato')

multiplicity = pyip.inputInt(prompt='How many of these sandwiches would you like? ', min=1)

# Dictionary matching sandwich items to their respective prices.
my_dictionary = {'Wheat': 1.50, 'White': 1.00, 'Sourdough': 1.50, 'Chicken': 2.50, 'Turkey': 3.00, 'Ham': 2.75,
                 'Tofu': 3.75, 'Cheddar': 0.75, 'Swiss': 1.00, 'Mozzarella': 1.50, 'Mayo': 0.00, 'Mustard': 0.00,
                 'Lettuce': 0.10, 'Tomato': 0.10}

total = 0.00
for i in range(len(sandwich)):  # Getting the price of sandwich as sum of dictionary values.
    total = total + my_dictionary.get(sandwich[i])

total = multiplicity*total
format_total = "{:.2f}".format(total)  # Formatting total to be two decimal places.
sandwich_string = ', '.join([str(item) for item in sandwich])  # Making our sandwich list a string.
print(f'Order: {multiplicity} {sandwich_string} sandwich. \nTotal: {format_total}')
