# names = ('John', 'Paul', 'George', 'Ringo')

# print(names[-1])
# print(len(names))
# print(names.index('George'))
# print('Ringo' in names)
# print(sorted(names))
# newTuple = names + ('Mick', 'Keith')
# print(newTuple)

# =================== Library  ==========================

# dog = {'name': 'Roger', 'age': 5, 'weight': '20 lbs'}

# print(dog['name'])
# print(dog['age'])

# dog['name'] = 'Rocky'
# print(dog)
# print(dog.get('name'))
# print('color' in dog)

# print(dog.keys())
# print(dog.values())
# print(dog.items())

# dog['favorite food'] = 'chicken'
# print(dog)

# del dog['age']
# print(dog)

# ======================= SETS ======================
# sets cannot have duplicates

# set1 = {'Sydney', 'Melbourne', 'Brisbane', 'Perth'}
# set2 = {'Paris', 'London', 'New York', 'Sydney'}

# intersect = set1 & set2  # & is the intersection operator
# print(intersect)  # {'Sydney'}

# mod = set1 | set2  # | is the union operator
# # {'Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Paris', 'London', 'New York'}
# print(mod)

# dif = set1 - set2  # - is the difference operator
# print(dif)  # {'Brisbane', 'Perth'}


# =================== FUNCTIONS ======================

def hello():
    print('Hello World!')
