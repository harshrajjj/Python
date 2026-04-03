#datetime,time,calender,timedelta,,arrow,dateutil

import arrow

brewing_time = arrow.utcnow()
brewing_time = brewing_time.shift(minutes=5)
print(f"brewing time: {brewing_time}")


from collections import namedtuple

chaiProfile = namedtuple("ChaiProfile", ["name", "flavour", "strength"])
myChai = chaiProfile(name="Masala Chai", flavour="Spicy", strength=8)
print(f"Chai Profile: {myChai}")
print(f"Chai Name: {myChai.name}")
print(f"Chai Flavour: {myChai.flavour}")
print(f"Chai Strength: {myChai.strength}")
