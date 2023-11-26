#!/usr/bin/env python3

# import sys

def return_evens(num_list):
    return[i for i in num_list if i % 2 ==0]
        

def make_exclamation(sentence_list):
    return [i + "!" for i in sentence_list]

                    # CANVAS CODE-ALONG
#List Comprehension
"""
squared_minus_one = list()

for i in range(1, 21):
    squared_minus_one.append((i**2)-1)

print(squared_minus_one)

"""
# list comprehension applied on the above code

# squared_minus_one = [(i**2) - 1 for i in range(1, 21)]

# print(squared_minus_one)

# List comprehension helps in reducing code.
# It is executed in one line
# No need of creating a variable before hand
# List comprehensions return a list. example below
# print(type(squared_minus_one))

# syntax
# new_list = [optional_operation(item) for item in old_list if optional_condition == True]

    # Generator Expressions

# one_to_three = range(1,4)
# list comprehension comparison with generator expressions
# squared_lc = [(i**2) for i in one_to_three]
# print(squared_lc)

# generator expressions use parenthesis instead of square brackets
# squared_ge = ((i**2) for i in one_to_three)
# print(squared_ge)      #this will generate a generator object inseat of printing the values

#Key diffs btwn LC and GE
"""
List Comprehensions CREATE NEW, complete lists while generator expressions SAVE the code to
create new, complete lists.

list_comprehension = [n for n in range(100)]
generator_expression =(n for n in range(100))
"""

