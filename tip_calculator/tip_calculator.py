import sys

meal = float(sys.argv[1])
tip = float(sys.argv[2])
tax = float(sys.argv[3])

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip

total = meal_with_tax + tip_value

print("The base cost of the meal was ${0:.2f}." .format(meal)
print("The tax on the meal was ${0:.2f}." .format(tax_value)
print("The tip you must pay is {0}%.  You should leave ${1:.2f} for a tip." .format(tip_value)
print("Your grand total is ${0:.2f}." .fortmat(total)