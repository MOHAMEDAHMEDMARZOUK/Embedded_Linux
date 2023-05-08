# create a tuple of items and their prices
grocery_items = (
    ('apple',  2.50),
    ('banana', 1.50),
    ('orange', 3.00),
    ('bread',  2.00),
    ('eggs',   2.50),
    ('milk',   3.50),
)

# define a function to display the menu
def display_menu():
    print('Welcome to our grocery shop!\n')
    print('Here is the list of items we offer and their prices:')
    for item in grocery_items:
        print(f'{item[0]} - ${item[1]:.2f}')
    print('')

# define a function to calculate the total price of the items in the cart
def calculate_total(cart):
    total = 0
    for item in cart:
        for grocery_item in grocery_items:
            if item[0] == grocery_item[0]:
                total += grocery_item[1] * item[1]
                break
    return total

# main program
cart = []
display_menu()

while True:
    choice = input('Enter the name of the item you want to buy (or "done" to finish): ').lower()
    if choice == 'done':
        break
    else:
        quantity = int(input('Enter the quantity: '))
        cart.append((choice, quantity))

total = calculate_total(cart)
print(f'Thank you for shopping with us!\nYour total is: ${total:.2f}')
