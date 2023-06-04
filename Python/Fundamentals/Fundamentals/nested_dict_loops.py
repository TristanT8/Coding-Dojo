'''
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
x[1][0] = 15
print(x[1])

students [0]['last_name'] = 'Bryant'
print(students)

sports_directory ['soccer'][0] = "Andres"
print(sports_directory)

z [0]['y'] = 30
print(z)
'''

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
"""
for f, l in zip(students[::2], students[1::2]):
    print(f, l)

for person in students:
    print(person.get('first_name')),
for person in students:
    print(person.get('last_name'))
"""

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def dojo_info(dict):
    for value in dict.items():
        for x in range(0, len(value)):
            print(value[x])
            
dojo_info(dojo)
