class chai:
    def __init__(self, sweetness , milkLevel):
        self.sweetness = sweetness
        self.milkLevel = milkLevel

    def sip(self):
        print("Sipping the chai with sweetness level of " + str(self.sweetness) + " and milk level of " + str(self.milkLevel))
    
    def addSugar(self, amount):
        print("Adding the sugar")

myChai = chai(sweetness=3, milkLevel=2)
myChai.addSugar(3)