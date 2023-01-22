# py.JM.Module1
Small code that looks at different data sets and uses various means of interpretation to manipulate and catagorize. Run code for full demonstration. 
This is a short code made to display several functions of python. It includes two exercises that consist of data sets that are manipulated in different ways.  

In exercise 1 we change a data_list into a iterable list that can be looped with different functions element by element. This is done in three ways using while statements, using enumerate to list not only and iterable list but also the index of the elements. And finally, using numpy to form an array that will then be turned into a list using .tolist function. 

Exercise 2 will is a data set that consists of experimental pH data that will be evaluated and analyzed for certain criteria. The data was first zipped together to be able to find the index of (Y) pH. This was then processed through lambda to find the max and min pH as well as the index (X) of the corresponding max and min pH. A threshold was then applied to the data to find the acidic solutions both X and Y elements.  

The data from exercise 2 was then used to form a bar graph using the matplotlib library. Dimensions of the plot were dictated by the length of bars instead of a range. This makes for a more aesthetically pleasing plot. The graph is accented with a red line that is suppose to indicate the critical pH level that was found in part(b) of the exercise.  
