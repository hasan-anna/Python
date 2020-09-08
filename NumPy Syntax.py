#Project: Betty's Bakery 
import numpy as np 

#Create a Numpy array 
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

#Load the csv file into a variable called recipes 
recipes = np.genfromtxt('recipes.csv', delimiter = ',')
print(recipes)
#Select and save all the ingredients of the 3rd column 
eggs = recipes[:,2]

#Which recipes require 1 egg 
one_egg = recipes[eggs == 1] 
print(recipes)

#Select all the ingredients of the 3rd row 
cookies = recipes[2, :]
# double the ingredients of cupcakes 
double_batch = cupcakes * 2  
# Add cookies and double_batch togetehr in a new variable called grocery_list
grocery_list = cookies + double_batch
print(grocery_list)
