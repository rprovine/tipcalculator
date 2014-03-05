meal = float(raw_input("Please enter the cost of your meal (ie, 50.00): "))
tax = float(raw_input("Enter the tax rate as a decimal (.12 not %12): "))
tip = float(raw_input("Enter your tip rate (.20 format): "))

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip

total = meal_with_tax + tip_value

print("The base cost of the meal was %.2f." % meal)
print("The tax on the meal was %.2f percent." % tax_value)
print("The tip you must pay is %.2f in dollars." % tip_value)
print("Your grand total is %.2f in dollars." % total)