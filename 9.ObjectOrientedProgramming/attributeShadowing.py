class chai:
    temp = "hot"
    strength = "strong"


cutting_chai = chai()
print(cutting_chai.temp)

cutting_chai.temp = "cold"
print(cutting_chai.temp)
print(chai.temp)

del cutting_chai.temp
print(cutting_chai.temp)
print(chai.temp)