####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Fancy Cakes"
signature_flavors = "cinnamen , rose hip , orange"
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for listing_menue in menu:
        print (listing_menue , menu[listing_menue])


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (SAR %s each):" % original_price)
    for original_flavors_ in original_flavors:
        print (original_flavors_)
    # your code goes here!


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (SAR %s each):" % signature_price)
    # your code goes here!
    for signature_flavors_ in signature_flavors:
        print(signature_flavors_)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu or order in original_flavors or order in signature_flavors:
     return True
    else:
     return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    user_order = input("what would you like to order? ")
    while user_order != "exit":
        if is_valid_order(user_order):
            order_list.append(user_order)
        else:
            print("No such a value!")
        user_order = input("what else would you like? ")

    return order_list


def accept_credit_card(total):
   if total > 5 :
    return True
   else:
    return False

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for prices in order_list:
        if prices in menu:
            total += menu[prices]
        elif prices in original_flavors:
            total += original_price
        elif prices in signature_flavors:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        print("- %s " % order)

    print()
    price = get_total_price(order_list)
    print("That'll be SAR %s" % price)
    if accept_credit_card(price):
        print("This order is eligible for credit card payment.")

    print("Thank you for shopping at %s" % cupcake_shop_name)
