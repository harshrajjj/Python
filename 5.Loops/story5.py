names = ["harsh", "sai", "sumanth" ]
bills = [100, 150, 200]

for name, bill in zip(names, bills):#zip is used to iterate over two or more lists simultaneously
    print(f"preparing chai for {name} with bill amount {bill}")