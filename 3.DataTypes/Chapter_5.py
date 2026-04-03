import sys
from fractions import Fraction
from decimal import Decimal

idealTemp = 95.5
currentTemp = 95.49
print(f"ideal temperature: {idealTemp}")
print(f"current temperature: {currentTemp}")
print(f"difference: {idealTemp - currentTemp}")

print(sys.float_info)