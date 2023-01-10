# define a weight variable and set it equal to any number
weight = 41.5

# Ground Shipping: a small flat charge plus a rate based on the weight of your package.

if weight <= 2:
  cost_ground_shipping = weight * 1.50 + 20.00
elif weight <= 6:
  cost_ground_shipping = weight * 3.00 + 20.00
elif weight <= 10:
  cost_ground_shipping = weight * 4.00 + 20.00
else:
  cost_ground_shipping = weight * 4.75 + 20.00
print("Ground Shipping $", cost_ground_shipping)

# Ground Shipping Premium: higher flat charge, but you aren’t charged for weight.

# Create a variable for the cost of premium ground shipping.
cost_ground_shipping_premium = 125.00
print("Ground Shipping Premium $", cost_ground_shipping_premium)

# Drone Shipping: has no flat charge, but the rate based on weight is triple the rate of ground shipping.
if weight <= 2:
  cost_drone_shipping = weight * 4.50
elif weight <= 6:
  cost_drone_shipping = weight * 9.00
elif weight <= 10:
  cost_drone_shipping = weight * 12.00
else:
  cost_drone_shipping = weight * 14.25
print("Drone Shipping $", cost_drone_shipping)
