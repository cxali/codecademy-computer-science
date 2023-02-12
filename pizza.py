#To keep track of the kinds of pizzas you sell, create a list called toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#To keep track of how much each kind of pizza slice costs, create a list called prices
prices = [2, 6, 1, 3, 2, 7, 2]

#Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.
num_two_dollar_slices = prices.count(2)
print("Count the number of occurrences of 2 in the prices list: " + str(num_two_dollar_slices))

#Find the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas = len(toppings)
print("\nWe sell " + str(num_pizzas) + " different kinds of pizza!")

#Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices. Print it out.
pizza_and_prices = [[prices[0], toppings[0]], [prices[1], toppings[1]], [prices[2], toppings[2]], [prices[3], toppings[3]], [prices[4], toppings[4]], [prices[5], toppings[5]], [prices[6], toppings[6]]]
print("\nPizza and prices:" + str(pizza_and_prices))

#Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
pizza_and_prices.sort()
print("\nSorted: " + str(pizza_and_prices))

#Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_and_prices[0]
print("\nCheapest pizza: " + str(cheapest_pizza))

#Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[-1]
print("\nPriciest pizza: " + str(priciest_pizza))

#It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.pop()
print("\nMinus the priciest pizza: " 
+ str(pizza_and_prices))

#Since the new pizza has a price of 2.5, it should come after [2, "pepperoni"] but before [3, "sausage"].
pizza_and_prices.insert(1, [2.5, "peppers"])
print("\nAdd the new pizza: " + str(pizza_and_prices))

#Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizza_and_prices[:3]

#Print the three_cheapest list.
print("\nThree cheapest pizza: " + str(three_cheapest))
