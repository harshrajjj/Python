class cahi:
    origin = "india"


print(cahi.origin)

cahi.isHot = True
print(cahi.isHot)


#creating an object of the class cahi 

masala = cahi()
print(masala.origin)
print(masala.isHot)
masala.isHot = False
print(masala.isHot)
print(cahi.isHot)
masala.flavour = "spicy"
print(masala.flavour)
# print(cahi.flavour)