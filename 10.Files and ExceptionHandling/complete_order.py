class InvalidChaiError(Exception):
    pass    

def bill(flavour,cups):
    menu ={"masala":20, "plain":10, "onion":15, "paper":25}
    try:
        if flavour not in menu:
            raise InvalidChaiError("Sorry, we don't have that flavor of chai.")
        else:
            total = menu[flavour] * cups
            print(f"The total price for {cups} {flavour} chai is {total} rupees.")
    except Exception as e:
        print(e)

bill("ginger", 2)
bill("masala", 2)
bill("plain", 2)
bill("onion", 2)
bill("paper", 2)