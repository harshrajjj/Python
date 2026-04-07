def process_order(item , quantity):
    try:
        price ={"masala":20}[item]
        total = price * quantity
        print(f"The total price for {quantity} {item} is {total} rupees.")
    except KeyError:
        print("Sorry, we don't have that item on the menu.")
    except TypeError:
        print("Quantity must be a number.")


process_order("ginger", 2)
process_order("masala", "two")