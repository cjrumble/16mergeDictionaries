# MERGE DICTIONARIES LESSON
# Merge Dictionaries in Python

# Before we jump on thesolutions, let’s define our problem statement first.
# Problem statement
# We have two dictionaries representing twoBUs(business units) of an IT company.
# Both include their employee names as keys along with the work ex as values.You can see the structure below.
# Business Unit = {Employee Name: Work Experience, ...}
# Here are two dictionaries with some sample data that we need to merge.
# unitFirst = {'Joshua': 10, 'Ryan': 5, 'Sally': 20, 'Martha': 17, 'Aryan': 15}
# unitSecond = {'Versha': 11, 'Tomi': 7, 'Kelly': 12, 'Martha': 24, 'Barter': 9}
# Set some goals for merging dictionaries, actually the business units.
# If employee names are duplicate, then unit2values should override the unit1.
# Both units must have valid keys. Both units must have valid integer values.
# Creating a new dictionary should not lead to any changes in the original two.
# Any modification in the new dictionary should not impact the data of the unit1 and unit2.
# Methods for merging dictionaries and choose which fits best in your case.

# By updating dictionaries cumulatively
# The most obvious way to combine the given dictionaries is to call the update() method for each unit.
# Since we’ve to keep the unit2 values in case of duplicates, so we should update it last.
# Please note that we can merge even more than two dicts using this approach.
"""
Desc:
  Python program to combine two dictionaries using update()
"""
# Define two existing business units as Python dictionaries
unitFirst = {'Joshua': 10, 'Ryan': 5, 'Sally': 20, 'Martha': 17, 'Aryan': 15}
unitSecond = {'Versha': 11, 'Tomi': 7, 'Kelly': 12, 'Martha': 24, 'Barter': 9}
# Initialize the dictionary for the new business unit
unitThird = {}
# Update the unitFirst and then unitSecond
unitThird.update(unitFirst)
unitThird.update(unitSecond)
# Print new business unit
# Also, check if unitSecond values overrided the unitFirst values or not
print("Unit Third: ", unitThird)
print("Unit First: ", unitFirst)
print("Unit Second: ", unitSecond)
# Result:
# Unit
# Third: {'Kelly': 12, 'Ryan': 5, 'Joshua': 10, 'Barter': 9, 'Tomi': 7, 'Aryan': 15, 'Sally': 20, 'Martha': 24,
#         'Versha': 11}
# Unit
# First: {'Sally': 20, 'Ryan': 5, 'Joshua': 10, 'Aryan': 15, 'Martha': 17}
# Unit
# Second: {'Tomi': 7, 'Kelly': 12, 'Barter': 9, 'Versha': 11, 'Martha': 24}
# New unit retained employee named Martha with value( 24) from the second unit.
# However, the new dictionary has combined all other elements from the two input dicts.
# we first created a new dict to keep the merged output of the other two dictionaries.
# It’ll make sure that changing the new one won’t affect the values of the original containers.

# Merge dictionaries using unpacking operator
# In Python 3.5 or above, we can combine even more than two dictionaries with a single expression.
# Merging two dictionaries using unpacking operator
#dictMerged = {**dictFirst, **dictSecond}
# Alternatively, we can call this approach using the ** kwargs in Python.
# It helps us pass variable size key - value pairs to a method.It also treats a dictionary as a sequence of key - value pairs.
# When used as ** kwargs, it decomposes the dictionary into a series of key - value elements.
sample_dict = {'emp1': 22, 'emp2': 12, 'emp3': 9, 'emp4': 14}
# The ** kwargs expression would treat the sample_dict as:
#** sample_dict = > 'emp1': 22, 'emp2': 12, 'emp3': 9, 'emp4': 14
# So, let’s apply ** kwargs or unpacking operator to combine the dictionaries. We’ll operate on the two given business
# units in our problem statement.
"""
Desc:
  Python program to merge two dictionaries using **kwargs
"""
# Define two existing business units as Python dictionaries
unitFirst = {'Joshua': 10, 'Ryan': 5, 'Sally': 20, 'Martha': 17, 'Aryan': 15}
unitSecond = {'Versha': 11, 'Tomi': 7, 'Kelly': 12, 'Martha': 24, 'Barter': 9}
# Merge dictionaries using **kwargs
unitThird = {**unitFirst, **unitSecond}
# Print new business unit
# Also, check if unitSecond values override the unitFirst values or not
print("Unit Third: ", unitThird)
print("Unit First: ", unitFirst)
print("Unit Second: ", unitSecond)
# Output:
# Unit
# Third: {'Sally': 20, 'Ryan': 5, 'Versha': 11, 'Tomi': 7, 'Martha': 24, 'Joshua': 10, 'Aryan': 15, 'Kelly': 12,
#         'Barter': 9}
# Unit
# First: {'Aryan': 15, 'Martha': 17, 'Joshua': 10, 'Sally': 20, 'Ryan': 5}
# Unit
# Second: {'Barter': 9, 'Martha': 24, 'Kelly': 12, 'Versha': 11, 'Tomi': 7}

# Combine two or more dictionaries
# Using the ** kwargs method to merge the dictionaries was a very straightforward method.

# How it groups three given dictionaries.
"""
Desc:
Python program to merge three dictionaries using **kwargs
"""
# Define two existing business units as Python dictionaries
unitFirst = {'Joshua': 10, 'Ryan': 5, 'Sally': 20, 'Martha': 17, 'Aryan': 15}
unitSecond = {'Versha': 11, 'Tomi': 7, 'Kelly': 12, 'Martha': 24, 'Barter': 9}
unitThird = {'James': 3, 'Tamur': 5, 'Lewis': 18, 'Daniel': 23}
# Merge three dictionaries using **kwargs
unitFinal = {**unitFirst, **unitSecond, **unitThird}
# Print new business unit
# Also, check if unitSecond values override the unitFirst values or not
print("Unit Final: ", unitFinal)
print("Unit First: ", unitFirst)
print("Unit Second: ", unitSecond)
print("Unit Third: ", unitThird)
# Output:
# Unit
# Final: {'Tomi': 7, 'Ryan': 5, 'Tamur': 5, 'Versha': 11, 'James': 3, 'Sally': 20, 'Martha': 24, 'Aryan': 15,
#         'Daniel': 23, 'Barter': 9, 'Lewis': 18, 'Kelly': 12, 'Joshua': 10}
# Unit
# First: {'Joshua': 10, 'Ryan': 5, 'Martha': 17, 'Sally': 20, 'Aryan': 15}
# Unit
# Second: {'Tomi': 7, 'Barter': 9, 'Martha': 24, 'Versha': 11, 'Kelly': 12}
# Unit
# Third: {'Daniel': 23, 'Tamur': 5, 'James': 3, 'Lewis': 18}

# Merge dictionaries with some custom action
# Consolidating the dataof two or more dictionaries, it is also possible totake some custom action.
# For example, if a person exists in two units with different work-ex values, then you may like to add up his experience while merging.
# How to add values for the same keys while combining three dictionaries.Here is a simple example for your help:
"""
Desc:
  Python program to merge dictionaries and add values of same keys
"""
# Define two existing business units as Python dictionaries
unitFirst = {'Joshua': 10, 'Daniel': 5, 'Sally': 20, 'Martha': 17, 'Aryan': 15}
unitSecond = {'Versha': 11, 'Daniel': 7, 'Kelly': 12, 'Martha': 24, 'Barter': 9}

def custom_merge(unit1, unit2):
    # Merge dictionaries and add values of same keys
    out = {**unit1, **unit2}
    for key, value in out.items():
        if key in unit1 and key in unit2:
            out[key] = [value, unit1[key]]
    return out

# Merge dictionaries while adding values of same keys
unitFinal = custom_merge(unitFirst, unitSecond)
# Print new business unit
# Also, check if unitSecond values override the unitFirst values or not
print("Unit Final: ", unitFinal)
print("Unit First: ", unitFirst)
print("Unit Second: ", unitSecond)
# This is a custom function that addsvalues of the same keys in a list.
# You can cross - check the same by executing the code:
# Unit
# Final: {'Sally': 20, 'Joshua': 10, 'Barter': 9, 'Versha': 11, 'Kelly': 12, 'Daniel': [7, 5], 'Martha': [24, 17],
#         'Aryan': 15}
# Unit
# First: {'Sally': 20, 'Joshua': 10, 'Daniel': 5, 'Martha': 17, 'Aryan': 15}
# Unit
# Second: {'Barter': 9, 'Kelly': 12, 'Daniel': 7, 'Martha': 24, 'Versha': 11}

# There are two common key entries in unit1 and unit2 dictionaries, namely Daniel and Martha.
# In the output, you can see that the program added their values in a list.