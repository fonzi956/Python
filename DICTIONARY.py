print('\n DICTIONARY or MAP \n')
# DICTIONARY or MAP -------------
# Made up of values with a unique key for each value
# Similar to lists, but you can't join dicts with a +

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}

print('print(' ',super_villains[\'Captain Cold\'] ',super_villains['Captain Cold'] , '\n')

# Delete an entry
del super_villains['Fiddler']
print('print(' ',super_villains del ',super_villains)

# Replace a value
super_villains['Pied Piper'] = 'Hartley Rathaway'

# Print the number of items in the dictionary
print('print(' ',len(super_villains) ',len(super_villains))

# Get the value for the passed key
print('print(' ',super_villains.get("Pied Piper") ',super_villains.get("Pied Piper"))

# Get a list of dictionary keys
print('print(' ',super_villains.keys() ',super_villains.keys())

# Get a list of dictionary values
print('print(' ',super_villains.values() ',super_villains.values())
