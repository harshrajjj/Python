is_boiling = True
stri_count = 5
totalActions  = stri_count + is_boiling #upcasting
print(f"total actions: {totalActions}")

milkPresent = 0  #no milk
print(f"is there milk? {bool(milkPresent)}")

water_hot = True
tea_added = True
tea_ready = water_hot and tea_added
print(f"is the tea ready? {tea_ready}")