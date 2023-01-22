print('Jesus Martinez ')  # Heading
print('Module 1 Homework')

print('Exercise 1')
data_list = [-12.5, 14.4, 8.1, 42]  # Data for the first exercise
print('Original data =', data_list)
print('Number_list(0) =')

i = 0
while i < len(data_list):  # This method uses the length of list to go through and loop all elements
    print(data_list[i])
    i = i + 1

print('Number_list(1) =')
# If I want to find th index I could use enumerate
items = (0, -12.5)
index, number = items
for index, number in enumerate(data_list):  # Each iteration will create a tuple, the tuple will be unpacked below
    print(index, number)

# Another way to loop list and make it iterable use np tp make an array
import numpy as np

number_list = np.array([data_list])
for num in number_list:
    print('Number_list(2) =', num)

Number_list_3 = number_list.tolist()  # Turning the array into a list with commas as the assignment wanted
print('Number_list =', Number_list_3, 'Finally done with exercise 1!')

data_list1 = number_list ** 2
data_list_1 = data_list1.tolist()  # Same thing as above just making a list
print('Example of looping through data (X)**2 =', data_list_1)
# example of iterable data set in action all numbers are positive as we would expect from **2

print('Exercise 2')  # Data input for ex 2
solution = [1, 2, 3, 4, 5]
print('solution =', solution)
pH = [2.5, 5.5, 10, 7.2, 9]
print('pH =', pH)

Solution_pH = list(zip(solution, pH))  # I did this so that we can see the extreme pH and corresponding solution
# print('Combined lists into tuple', Solution_pH)

print('The max and min solution (X) and pH (Y)')  # Finding the max and min using lamda to get X and Y, could use timeit
print('max pH=', max(Solution_pH, key=lambda item: item[1]))
print('min pH=', min(Solution_pH, key=lambda item: item[1]))
# Here I could have also used enumerate to be able to index the elements but lambda is a lot faster! And gives me soln #

# Finding the acidic solutions by providing a threshold. I did this so that it can return both the X and Y of the tuple
print('There are 2 solutions with an acidic pH (X,Y) <7')
threshold = 7
Acidic = [tpl for tpl in Solution_pH if tpl[1] < threshold]
print(Acidic, 'The acidic solutions are X= 1 and X= 2')

# Data analysis plots of soln acidity data
import matplotlib.pyplot as plt

# First we transfer the data
Acidity = [2.5, 5.5, 10, 7.2, 9]
bars = ('1', '2', '3', '4', '5')  # added soln numbers instead of range
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, Acidity, color='c')  # This is a visual representation of data for ex #2 in bar graph form
# Create names on the x-axis
plt.xticks(y_pos, bars, )
# Label all things
plt.xlabel("Solution", size=16)
plt.ylabel("pH ", size=16)
plt.title("pH of given Solution's", size=20)
# Plot a horizontal line to show what is acidic also add legend to show pH =7
plt.axhline(y=7, color='r', linestyle='dashed')
plt.legend(['pH = 7', ], loc='upper left')
# Show the graphic
plt.show()
# This was fun! If there is anything that you can think of to make this better I would appreciate it.
# Thank you
