   # 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#
def car_at_light(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'wait'
    elif light == 'green':
        return 'go'
    else:
        raise Exception(f'Undefined instruction for color {light}')

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def safe_subtract(x,y):
    try:
        return x - y
    except TypeError:
        return None
    else:
        return "Could not be subtracted due to type"


# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

def retrieve_age_eafp(x: dict):
    try:
        return 2022 - x['birth']
    except KeyError:
        return 'error'


def retrieve_age_lbyl(x: dict):
    if 'birth' in x.keys():
        return 2022 - x['birth']
    else:
        print(f'failed for dict {x}')
        pass


# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

import csv


def read_data(filepath):
    try:
        with open(filepath, 'r') as data:
            for line in csv.reader(data):
                return line
    except FileNotFoundError:
        return 'File Not Found'

#______________________________________________________________________

#import csv
#import pandas
#import os

#def read_data(filename):
#    filepath = ""

    # finding the file location and reading
#   for root, dirs, files in os.walk(r'C:'):
#        for name in files:
#            if name == filename:
#                filepath = (os.path.abspath(os.path.join(root, name)))
#                print("File found at File path:",filepath)
#    try:
#        f = open(str(filepath), "r")
#        print(f.read())
#        # to read the csv as a dataframe we can do the below:
#        # dataframe = pd.read_csv(filepath)
#    except FileNotFoundError:
#        print('File Not Found')
#


#filename_present= 'sample_diabetes_mellitus_data.csv'
# function call with above filename will print the contents of the file
#read_data(filename_present)

#filename_not_present = 'this_file_is_not_in_system.csv'
# function call with the above filename will throw File Not Found exception, which is handled in the except block
#read_data(filename_not_present)

#_____________________________________________________




# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2

    total_double_sum += elem
# total_double_sum is only counted with the values of elem. The easiest way to get the double value of all elements in a list combined would be just to sum the list without iteration, like so:

input_list = [10, 5, 2]
total_double_sum = sum(input_list) * 2
# If for some reason you want to iterate, you could use the code below

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string
# Looks like you're trying to combine elements in a list into one string.
# #What this code actually does is iterates over a list, and returns the last string as
#"Groot_Groot" because you iterate without saving each iteration anywhere.
# Because strings is defined as one object, not an iterable, you can't iterate over it.
# Instead join like below
str_concat = '_'.join(strings)

### (c) Careful!
j=10
while j > 0:
   j += 1
# This is just going to keep adding from 10 until infinity, because the while condition
# is set to j>0, and j will always be >0 while you keep adding one to 10. I don't know what this
# iteration is trying to achieve, but if you're trying to count from 1 to 10, just change it like below
j=0
while j < 10:
   j += 1

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem
#Anything * 0 is 0. Start from 1 instead.
productory = 1
for elem in [1, 5, 25]:
    productory *= elem

##### Try to use map and reduce in the next 3 exercises
################################################
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
strings = ["Simba and Nala are lions.", "I laugh in the face of danger.",
  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

count = 0
for i in strings:
    if 'Simba' in i:
        count += 1

count2 = len(list(filter(lambda x: 'Simba' in x, strings)))
#count2 is less readable, so if efficiency isn't a problem the for loop is better.

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#


