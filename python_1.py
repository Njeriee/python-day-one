# initialising a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# accessing values in a dictionary.
print(dict['Name'])

# updating dictionary
# updating an entry
dict['Age'] = 10
print(dict['Age'])

# adding a new entry
dict['School'] = 'New light kindergarten'
print(dict)

# deleting 
# deleting an enty ; will remove entry with name as key together with its value
del dict['Name']
print(dict)

# deliting all the entries ; will return an empty dictionary
dict.clear()
print(dict)

# deleting an entire dictionary
del dict

# lists
# creating a list
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

# accessing values 
# a single value
print(list1[0])

# accessing multiple values
print(list1[1:3])

# updating list ; will remove the inital value and replace it with the new one
list1[2] = 'new stuff'
print(list1)

# adding an item
# list1.append(1, 'biology')

# deleting an item at a specific index
del list1[2]
print(list1)

# checking the length
print(len(list1))

# concatation
print(list1 + list2)

# repetition
print(list1*2)

# checking whether an item is in list or not
print(2000 in list1)
print('physics' in list1)

# iteration
for i in list1:
    print(i)

# tuples
# initialising tuples
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

# accessing items in a tuple
# accessing multiple items i.e slicing
print(tup1[0:2])

# accsessing a single item
print(tup1[3])

# tuples are immutable hence there is no allowance for update or deletion of tuple elements one can delete an entire tuple though
del tup1
# this will raise an error
# print(tup1) 

# getting lenth
print(len(tup2))

# concatation
print(tup2 + tup3)

# repetititon 
print(tup2*2)

# iteration
for item in tup2:
    print(item)


# sets
# creating/initialising a set
# using set() function
set1 = set(['Mon','Tue','Wed','Thur'])
print(set1)

# using curly braces
set2 = {'Jan','Feb','May','June'}
print(set2)



