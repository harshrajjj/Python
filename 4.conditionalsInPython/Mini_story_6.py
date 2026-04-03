seat_type = input("Enter your preferred seat type (sleeper, Ac, general, luxury): ").lower()

match seat_type:
    case "sleeper":
        print("You have chosen a sleeper seat.")
    case "ac":
        print("You have chosen an AC seat.")
    case "general":
        print("You have chosen a general seat.")
    case "luxury":
        print("You have chosen a luxury seat.")
    case _:
        print("Invalid seat type. Please choose from 'sleeper', 'ac', 'general', or 'luxury'.") 