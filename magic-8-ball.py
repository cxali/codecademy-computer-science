import random

# declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball
name = "Ali"

# declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball
question = "Will I be successful someday?"

# store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
answer = ""

# create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call
random_number = random.randint(1,12)

# Next, add a print() statement that outputs the value of random_number
print(random_number)

# we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "As I see it, yes"
elif random_number == 11:
  answer = "Cannot predict now"
elif random_number == 12:
  answer = "Don’t count on it"
else:
  answer = "Error"

# If the name string is empty, the output of the program looks like the following
if name == "":
  print("Question: " + question)
  # second print() statement that will output the Magic 8-Ball’s answer
  print("Magic 8-Ball's answer: " + answer)
# If the question is an empty string, print out a message to the user
elif question == "":
  print("Please input your question")
else:
  # output the asker’s name and their question
  print(name + " asks: " + question)
  # second print() statement that will output the Magic 8-Ball’s answer
  print("Magic 8-Ball's answer: " + answer)
