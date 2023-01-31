last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#list called subjects filled with the classes I'm taking
subjects = ["physics", "calculus","poetry", "history"]

#list called grades filled with my scores
grades = [98, 97, 85, 88]

#two-dimensional list that combined subjects and grades. Assigned the value into a variable called gradebook
gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], [subjects[2], grades[2]], [subjects[3], grades[3]]]

#used the .append() method to add a list with the ff.values and associated grade values to our two-dimensional list
gradebook.append(['computer science', 100]) 
gradebook.append(['visual arts', 93])

#Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class. I accessed the index of the grade for my visual arts class and modified it to be 5 points greater.
gradebook[-1][-1] = 98


#switched from a numerical grade value to a Pass/Fail option for your poetry class.Used the .remove() method to delete it.
gradebook[2].remove(85)

#used the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.
gradebook[2].append("Pass")
print(gradebook)

#Created a new variable full_gradebook that combined both last_semester_gradebook and gradebook using + to have one complete grade book.Printed full_gradebook to see our completed list.
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
