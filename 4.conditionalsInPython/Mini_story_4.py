device_status = input("Is the device on or off? ").lower()

temperature = int(input("Enter the current temperature in degrees Celsius: "))

if device_status == "on":
    if temperature < 20:
        print("The device is on and the temperature is low. It's a good time to turn it on.")
    elif 20 <= temperature <= 30:
        print("The device is on and the temperature is moderate. It's a comfortable environment.")
    else:
        print("The device is on and the temperature is high. Be cautious of overheating.")
else:
    print("The device is off. Please turn it on to check the temperature.")