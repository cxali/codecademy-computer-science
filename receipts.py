"""
In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

Create a variable called lovely_loveseat_description and assign to it the following string
"""

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high X 40 inches wide x 30 inches deep. Red or white."

#Create a variable lovely_loveseat_price and set it equal to 254.00
lovely_loveseat_price = 254.00

#Create a variable called stylish_settee_description and assign to it the following string
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#Create a variable stylish_settee_price and assign it the value of 180.50
stylish_settee_price = 180.50

#Create a new variable called luxurious_lamp_description and assign it the following
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

#Create a variable called luxurious_lamp_price and set it equal to 52.15.
luxurious_lamp_price = 52.15

#Define the variable sales_tax and set it equal to .088. That’s 8.8%.
sales_tax = .088

#define a variable called customer_one_total. Let’s set that variable equal to 0 for now.
customer_one_total = 0

#Create a variable called customer_one_itemization and set that equal to the empty string ""
customer_one_itemization = ""

#Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total
customer_one_total += lovely_loveseat_price

#Add the description of the Lovely Loveseat to customer_one_itemization.
customer_one_itemization += lovely_loveseat_description

#Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.
customer_one_total += luxurious_lamp_price

#add the description of the Luxurious Lamp to our itemization
customer_one_itemization += luxurious_lamp_description

#Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax
customer_one_tax = customer_one_total * sales_tax

#Add the sales tax to the customer’s total cost
customer_one_total += customer_one_tax

#printing out the heading for the customer's itemization
print("Customer One Items:")

#printing out the customer's itemization
print(customer_one_itemization)

#printing out the heading for the customer's total cost
print("Customer One Total:")

#printing out the customer's total
print(customer_one_total)
