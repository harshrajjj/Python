# file  = open("orders.txt", "w")
# try:
#     order =["masala dosa", "plain dosa", "onion dosa", "paper dosa"]
#     for item in order:
#         file.write(item + "\n")
# except Exception as e:
#     print(e)
# finally:
#     file.close()

with open("orders.txt", "w") as file:#file.__enter__() and file.__exit__()
    order =["masala dosa", "plain dosa", "onion dosa", "paper dosa"]
    for item in order:
        file.write(item + "\n")