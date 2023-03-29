pizza = "Please enter which pizza topping you want"
pizza += "\nWhen you finish type quit"

pizza_toppings = ''
while pizza_toppings != 'quit':
    pizza_toppings=input(pizza)
    print(f"{pizza_toppings} added.")