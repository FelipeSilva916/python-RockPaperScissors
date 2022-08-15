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

# def hello(name, age):
#     print(f"Hello {name}, you are {age} years old.")


# hello('Felipe', 35)

# val = {'name': 'Felipe', 'age': 35}


# def change(value):  # value is a dictionary
#     value['age'] = value['age'] + 1  # value increases by 1


# change(val)  # val is a dictionary
# print(val)


# =================== VARIABLE SCOPE ======================
# def test():
#     age = 35
#     print(age)


# test()

# ===================== NESTED FUNCTIONS ======================

# def talk(phrase):  # phrase is a string
#     def say(word):  # word is a string
#         print(word)  # prints the word

#     words = phrase.split(' ')  # splits the phrase into words
#     for word in words:  # for each word in the phrase
#         say(word)  # calls the say function


# talk('I am going to buy a new car')

# ====================== OBJECTS ======================

# age = 35

# print(age.real)
# print(age.imag)
# print(age.conjugate())  # returns the complex conjugate
# print(age.bit_length())  # returns the number of bits in the number

# items = [1, 2, 3, 4, 5]
# items.append(6)  # adds 6 to the end of the list
# print(items)  # [1, 2, 3, 4, 5, 6]
# print(id(items))  # prints the memory address of the list


# ====================== LOOPS ======================

# condition = True
# while condition == True:
#     print('Hello')
#     condition = False

# count = 0
# while count < 10:
#     print('The count is:', count)
#     count += 1

# print('Goodbye')

# items = [1, 2, 3, 4, 5]

# for item in items: # for each item in the list
#     print(item) # prints each item

# enumerate returns the index and the item
# for index, item in enumerate(items):
#     print('Index: ', index, 'Item:', item)  # prints the index and the item

# for item in items:
#     if item == 3:
#         break
#     print(item)

# ====================== CLASSES ======================

# class Animal:
#     def walk(self):
#         print('Animal is walking')


# class Dog(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print('Woof!')


# roger = Dog('Roger', 5)  # creates a new Dog object
# # print(type(roger))  # prints the type of the object
# print(roger.name)  # prints the name of the dog
# print(roger.age)  # prints the age of the dog
# roger.bark()  # prints the bark of the dog
# roger.walk()  # prints the walk of the dog


# ====================== Accepting Arguments ======================
import argparse  # imports the argparse module
import sys  # imports the sys module

# name = sys.argv[1]  # sys.argv is a list of arguments passed to the script
# print('Hello', name)  # prints the name passed to the script


parser = argparse.ArgumentParser(
    description='This program prints the name of dogs'
)  # creates a new ArgumentParser object

parser.add_argument('-c', '--color', metavar='color', required=True,
                    help='The color of the dog')  # adds a new argument

args = parser.parse_args()  # parses the arguments passed to the script


print(args.color)  # prints the color passed to the script
