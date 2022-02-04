#1. Update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
# Change the value 20 in z to 30
z[0]['y'] = 30

# - -- - -- - -- -- -  -- - - -- - - -- - -- - -- - - -- - -- - - -- - -- - -- - - -- -- - 
#2. Iterate through a list of dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for dict in students:
        print(f"first_name - {dict['first_name']}, last_name - {dict['last_name']}")

iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name -

# - -- - -- - -- -- -  -- - - -- - - -- - -- - -- - - -- - -- - - -- - -- - -- - - -- -- - 
#3. Get values from a list of dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        print(dict[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# - -- - -- - -- -- -  -- - - -- - - -- - -- - -- - - -- - -- - - -- - -- - -- - - -- -- - 
#4. iterate through a dictionary with list values
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
def printInfo(some_dict):
    for key in some_dict:
        print(f"{key} size: {len(some_dict[key])}")
        for val in some_dict[key]:
            print(val)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

