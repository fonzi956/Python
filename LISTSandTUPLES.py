print('\n LISTS \n')
# LISTS -------------
# A list allows you to create a list of values and manipulate them
# Each value has an index with the first one starting at 0

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('The first item is', grocery_list[1] ,'\n')

# You can change the value stored in a list box
grocery_list[0] = "Green Juice"
print('print(' ',grocery_list) ',grocery_list,'\n')

# You can get a subset of the list with [min:up to but not including max]

print('print(' ',grocery_list[1:3] ',grocery_list[1:3],'\n')

# You can put any data type in a a list including a list
other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]

print('print(' ',to_do_list ',to_do_list,'\n')

# Get the second item in the second list (Boxes inside of boxes)
print('print(' ',to_do_list[1][1] ',to_do_list[1][1],'\n')

# You add values using append
grocery_list.append('onions')
print('print(' ',to_do_list append ',to_do_list,'\n')

# Insert item at given index
grocery_list.insert(1, "Pickle")

# Remove item from list
grocery_list.remove("Pickle")

# Sorts items in list
grocery_list.sort()

# Reverse sort items in list
grocery_list.reverse()

# del deletes an item at specified index
del grocery_list[4]
print('print(' ',to_do_list del ',to_do_list,'\n')

# We can combine lists with a +
to_do_list = other_events + grocery_list
print('print(' ',to_do_list combine ',to_do_list,'\n')

# Get length of list
print('Get length of list ',len(to_do_list))

# Get the max item in list
print('Get the max item in list ',max(to_do_list))

# Get the minimum item in list
print('Get the minimum item in list ',min(to_do_list))

# You can print a string multiple times with *
print('\n' * 5)

print('\n TUPLES Values in a tuple cant change like lists \n')
# TUPLES -------------
# Values in a tuple can't change like lists

pi_tuple = (3, 1, 4, 1, 5, 9)

# Convert tuple into a list
new_tuple = list(pi_tuple)

# Convert a list into a tuple
# new_list = tuple(grocery_list)

# tuples also have len(tuple), min(tuple) and max(tuple)
