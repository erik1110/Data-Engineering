def make_icecream(*toppings):
    print("The topping of the ice cream :")
    for topping in toppings:
        print("---",topping)

def make_drink(size,drink):
    print("Your drink :")
    print("---",size.title())
    print("---",drink.title())