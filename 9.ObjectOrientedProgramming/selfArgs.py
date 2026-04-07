class cahiCup:
    size =150

    def describe(self):
        print(f"This is a {self.size} ml cup.")

my_cup = cahiCup()
my_cup.describe()

print(cahiCup.describe(my_cup))