# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light" which gives the color of a traffic light.
# If the color is "red", the function should return "stop". If the color is "green", the function
# should return "go". If the color is "yellow" the function should return "wait". If the color
# is anything else, the function should raise an exception with the following message:
# "Undefined instruction for color: <light>" where <light> is the value of the parameter light.

def car_at_light(light):
    try:
        if light=="red":
            print("red")
            return ("stop")
        elif light=="green":
            print("green")
            return ("go")
        elif light=="yellow":
            print("yellow")
            return ("wait")
        else:
            raise Exception('"Undefined instruction for color: <light>" where <light> is the value of the parameter light.')
    except Exception as exception:
        print(exception)
        return

#car_at_light("orange")
#car_at_light("red")


#__________________________________________________________________________________________________________#

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type,
# it returns None.
# If there is any other reason why it fails show the problem
#

##
def safe_subtract(a,b):
    try:
        print("First value is {}".format(a))
        print("Second value is {}".format(b))
        print("Result is :",b-a)
        return(b-a)
    except TypeError:
        print("Encountered TypeError. Function will return None")
        return (None)
    except Exception:
        print("Exception")
        return (None)


#safe_subtract(2,"a")

##



#__________________________________________________________________________________________________________#

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl


def retrieve_age_eafp(details):
    try:
        print(2022 - details['birth'])
        return 2022 - details['birth']
    except KeyError :
        print("Birth detail not available")
        return


def retrieve_age_lbyl(details):
    if 'birth' in details.keys():
        print(2022 - details['birth'])
        return 2022 - details['birth']
    else:
        print("Birth detail not available")
        return


details_1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
details_2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
#retrieve_age_eafp(details_1)
#retrieve_age_eafp(details_2)
#retrieve_age_lbyl(details_1)
#retrieve_age_lbyl(details_2)


#__________________________________________________________________________________________________________#

# 4)
# Imagine you have a file named data.csv.
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact
# that it might not exist.
#

import csv
import pandas
import os

def read_data(filename):
    filepath = ""

    # finding the file location and reading
    for root, dirs, files in os.walk(r'C:'):
        for name in files:
            if name == filename:
                filepath = (os.path.abspath(os.path.join(root, name)))
                print("File found at File path:",filepath)
    try:
        f = open(str(filepath), "r")
        print(f.read())
        # to read the csv as a dataframe we can do the below:
        # dataframe = pd.read_csv(filepath)
    except FileNotFoundError:
        print('File Not Found')


#filename_present= 'sample_diabetes_mellitus_data.csv'
# function call with above filename will print the contents of the file
#read_data(filename_present)

#filename_not_present = 'this_file_is_not_in_system.csv'
# function call with the above filename will throw File Not Found exception, which is handled in the except block
#read_data(filename_not_present)


#__________________________________________________________________________________________________________#

# 5) Squash some bugs!
# Find the possible logical errors (bugs)
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    # total_double_sum += elem     [commented out the logically incorrect code]
    # to get the sum of double the values in the list we should add 'double' instead of 'elem'
    # corrected code below:
    total_double_sum += double

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    # strings = string+"_"+string       [commented out the logically incorrect code]
    # to get a concatenation of the strings in the list we could use .join method as well,
    # however a small modification as below also works
    # corrected code below:
    strings = string + "_"

### (c) Careful!
j=10
while j > 0:
   # j += 1             [commented out the logically incorrect code]
   # incrementing value of j by 1 in each iteration results in infinite loop,
   # rather we should be decrementing the value by 1, so that after 10 iterations
   # the condition j > 0 become false and the loop terminates
   # corrected code below:
   j -= 1

### (d)


# productory = 0                [commented out the logically incorrect code]
# if we initiate productory with value 0 then in all product we get result zero
# corrected code below:
productory = 1

for elem in [1, 5, 25]:
    productory *= elem




################################################
##### Try to use map and reduce in the next 3 exercises

# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
#

from functools import reduce

def count_simba(list_of_strings):
    count_per_string = list(map(lambda x: x.count("Simba"), list_of_strings))
    count = reduce(lambda a, b: a+b, count_per_string)
    print(count)

text = ["Simba and Nala are lions.", "I laugh in the face of danger.",
        "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

#count_simba(text)


#__________________________________________________________________________________________________________#

# 7)
# Create a function called "get_day_month_year" that takes
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its
# day, month, and year.
#

import pandas as pd
import datetime
def get_day_month_year(list_of_datetimes):
    list_of_dates = list(map(lambda x: x.date, list_of_datetimes))
    list_of_months = list(map(lambda x: x.month, list_of_datetimes))
    list_of_years = list(map(lambda x: x.year, list_of_datetimes))

    # Calling DataFrame constructor after zipping
    # the lists, with columns specified
    df = pd.DataFrame(list(zip(list_of_dates, list_of_months, list_of_years)),
                      columns=['day', 'month', 'year'])
    print(df)
    return df

# creating a datetime list to make fucntion call
# base = datetime.datetime.today()
# date_list = [base - datetime.timedelta(days=x) for x in range(10)]
# function call
# get_day_month_year(date_list)


#__________________________________________________________________________________________________________#


# 8)
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#


import itertools
from geopy.distance import geodesic
def compute_distance(list_of_coordinates):

    # given input has a list of tuples of tuples , we convert it to list of list of tuples
    # because reduce can unpack a list of tuples but not tuple of tuples
    print("Original Input --> List of tuples of tuples :",list_of_coordinates)
    #list_of_coordinates_modified = list(map(lambda x: list(x), list_of_coordinates))
    #print("Modified List --> List of list of tuples :",list_of_coordinates_modified)
    list_of_distances = list(map(lambda x: (geodesic(x[0], x[1]).km), list_of_coordinates))
    print(list_of_distances)
    return list_of_distances


#compute_distance([((41.23,23.5), (41.5, 23.4)),((52.38, 20.1),(52.3, 17.8))])



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

def sum_general_int_list(l):
    total = 0
    for j in range(len(l)):
        if type(l[j]) == list:
            total += sum_general_int_list(l[j])
        else:
            total += l[j]

    return total

#print(sum_general_int_list([[2], 3, [[1,2],5]]))



