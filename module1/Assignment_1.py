# Assignment 1
import numpy as np

'''
Lists
'''
print('-----LISTS-----')

# Create a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nLet's look at my new list:", my_list)

# Access list items
# Let's also look at the datatype of that list item
print('\nFinal (10th) item in list:', my_list[9])
print('Datatype of 10th item in list:', type(my_list[9]))

# Change the value of a list item
print('\nOriginal value of 1st list item:', my_list[0])
my_list[0] = my_list[0]+3
print('Value of list item after adding 3:', my_list[0])

# Loop through a list
print('\nLoop through list:')
for i in my_list:
   print(i)

# Get the length of a list
print('\nLength of my list:', len(my_list))

# Add an item to the end of a list
new_number = 11
my_list.append(new_number)
print('\nLook at list with new int added:\n', my_list)

# Add an item at a specified index
my_list.insert(5, 0.032)
print('\nLook at list with new float added in 5th spot in list:\n', my_list)

# Remove an item
my_list.remove(0.032)

# Remove an item at a specified index
del my_list[10]
print('\nCheck to see that 0.032 and 11 are both removed:', my_list)

# Empty a list
my_list.clear()
print('\nCheck to see that my list is now empty:', my_list)

# Use the list() constructor to make a list
rand_array = np.random.rand(10)
rand_list = list(rand_array)
print('\nNew list of random floats:', rand_list)


'''
Dictionaries
'''
print('\n\n\n-----DICTIONARIES-----')

# Create a dictionary
truck_dict = {
    "brand": "Toyota",
    "model": "Tacoma",
    "color": "White",
    "year": 2020
}
print('\nLook at dictionary (truck_dict):', truck_dict)

# Access the items of a dictionary
print('\nLook at model of truck:', truck_dict['model'])

# Change the value of a specific item in a dictionary
truck_dict['year'] = 2021
print('\nUpdated year of truck:', truck_dict['year'])

# Print all key names in a dictionary, one by one
print('\nLook at dict key names, one by one:')
for key in truck_dict.keys():
    print('*', key)

# Print all values in a dictionary, one by one
print('\nLook at dict value names, one by one:')
for value in truck_dict.values():
    print('*', value)

# Loop through both keys and values, by using the items() function
print('\nItemize keys and values:')
for item in truck_dict.items():
    print(item)

# Check if a key exists
def check_for_key(keyname):
    if keyname in truck_dict:
        return(f'{keyname} key exists')
    else:
        return(f'{keyname} key does not exist')

print('\nCheck if color key already exists (spoiler alert: it does):')
print(check_for_key('color'))

print("\nCheck if exterior key already exists (spoiler alert: it doesn't):")
print(check_for_key('exterior'))

# Get the length of a dictionary
print('\nLength of dictionary:', len(truck_dict))

# Add an item to a dictionary
truck_dict['exterior'] = "Very muddy"
print('\nCleanliness of exterior (new key/value):', truck_dict['exterior'])

# Remove an item from a dictionary
del(truck_dict['year'])
print('\nCheck to see if year was removed:', truck_dict)

# Empty a dictionary
truck_dict.clear()
print('\nCheck to see if dictionary is now empty:', truck_dict)

# Use the dict() constructor to create a dictionary
tesla_dict = dict(brand='Tesla', model='Model 3',
    color='Midnight Silver Metallic', year=2020)
print('\nLook at new dictionary (tesla_dict):', tesla_dict)


'''
Tuples
'''
print('\n\n\n-----TUPLES-----')

# Create a tuple
tonto_trees = ('juniper', 'ponderosa', 'cottonwood', 'mesquite')
print('\nLook at tuple (tonto_trees):', tonto_trees)

# Access tuple items
print('\nLook at 2nd item in tuple:', tonto_trees[1])

# Change tuple values
trees_list = list(tonto_trees)
trees_list[0] = 'alligator juniper'
tonto_trees = tuple(trees_list)
print('\nLook at updated first tuple value', tonto_trees)

# Loop through a tuple
print('\nLook at strings in tuple:')
for i in tonto_trees:
    print('*', i)

# Check if a tuple item exists
def check_for_tuple_item(name):
    if name in tonto_trees:
        return(f'{name} exists')
    else:
        return(f'{name} does not exist')

print('\nCheck if mesquite already exists (spoiler alert: it does):')
print(check_for_tuple_item('mesquite'))

print("\nCheck if aspen already exists (spoiler alert: it doesn't):")
print(check_for_tuple_item('aspen'))

# Get the length of a tuple
print('\nLength of tuple:', len(tonto_trees))

# Delete a tuple
del tonto_trees

# Use the tuple() constructor to create a tuple
yellowstone_trees = tuple(['lodgepole pine', 'whitebark pine',
    'Engelmann spruce', 'white spruce', 'subalpine fir', 'Douglas fir',
    'Rocky Mountain juniper', 'common juniper', 'limber pine', 'quaking aspen',
    'cottonwood'])
print('\nLook at new tuple (yellowstone_trees):', yellowstone_trees)


'''
Sets
'''
print('\n\n\n-----SETS-----')

# Create a set
sanderson_sl_books = {'The Way of Kings', 'Words of Radiance', 'Oathbringer',
    'Rhythm of War'}
print('\nLook at set (sanderson_sl_books):', sanderson_sl_books)

# Loop through a set
print('\nLook at strings in set:')
for i in sanderson_sl_books:
    print('*', i)

# Check if an item exists
def check_for_set_item(name):
    if name in sanderson_sl_books:
        return(f'{name} exists')
    else:
        return(f'{name} does not exist')

print('\nCheck if Oathbringer already exists (spoiler alert: it does):')
print(check_for_set_item('Oathbringer'))

print("\nCheck if Boomshakalaka already exists (spoiler alert: it doesn't):")
print(check_for_set_item('Boomshakalaka'))

# Add an item to a set
sanderson_sl_books.add('Untitled Book 5')
print('\nCheck for new book:', sanderson_sl_books)

# Add multiple items to a set
new_books = ['Untitled Book 6', 'Untitled Book 7']
for book in new_books:
    sanderson_sl_books.add(book)
print('\nCheck for new books:', sanderson_sl_books)

# Get the length of a set
print('\nLength of set:', len(sanderson_sl_books))

# Remove an item in a set
sanderson_sl_books.discard('Untitled Book 7')
print('\nCheck if book 7 was removed:', sanderson_sl_books)

# Remove an item in a set by using the discard() method
sanderson_sl_books.remove('Untitled Book 6')
print('\nCheck if book 6 was removed:', sanderson_sl_books)

# Remove the last item in a set by using the pop() method
sanderson_sl_books.pop()
print('\nCheck if item in set was removed:', sanderson_sl_books)

# Empty a set
sanderson_sl_books.clear()
print('\nCheck if set was cleared:', sanderson_sl_books)

# Delete a set
del sanderson_sl_books

# Use the set() constructor to create a set
common_guitar_chords = ['C major', 'A major', 'G major', 'E major', 'D major']
common_chords_set = set(common_guitar_chords)
print('\nLook at new set of guitar chords:', common_chords_set)
