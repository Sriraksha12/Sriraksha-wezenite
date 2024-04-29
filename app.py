print("Hello world")
print('o--')
print('!!!!')
print('*' * 10)

price = 10
rating = 4.9
name1 = 'Mosh'
is_pblished = True
print(price)

full_name = 'John smith'
age = 20
is_new = True
#receiving inputs
name = input('What is your name?')
favorite_color = input('What is your favorite color?')
print(name + 'likes' + favorite_color)

#type coversion
birth_year = input('Birth year:')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input('Weight(lbs):')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

#strings and string methods
course = 'python for beginners'
print(course)
print(course[0])
print(course[0:3])
name2 = 'Jennifer'
print(name[1:-1])

first = 'John'
last = 'smith'
message = first + '[' + last + '] is a coder'
print(message)


print(len(course))
print(course.upper())
print(course.lower())
print(course.find('p'))
print(course.replace('beginners' , 'absolute beginners'))
print('python' in course)

#Airthmetic operation
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
x = 10
x = x + 3
print(x)
y = (2+3) * 10 - 3
print(y)

#math function
a = 2.9
print(round(a))
print(abs(-2.9))

import math

print(math.ceil(2.9))
print(math.floor(2.9))

#if statement
is_hot = True
is_cold = False
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")
else:
    print("It is a lovely day")
print("Enjoy your day")


price = 1000000
has_god_credit1 = True
if has_god_credit1:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

#logical operator
has_high_income = True
has_good_credit = False
has_criminal_record = False
if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

#comparison operator
temperature = 35
if temperature > 30:
    print("It is hot day")
else:
    print("It is not a hot day")


nam = "J"
if len(nam) < 3:
    print("Name must be at least 3 characters.")
elif len(nam) > 50:
    print("Name must be maximum of 50 characters.")
else:
    print("Name looks good!")

#weight converter programe
weight = int(input('Weight:'))
unit = input('(L)bs or (k)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

#while
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

#building a guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("Sorry you failed")

#car game
cmd=""
started=False
stopped=False
while(True):
    cmd= input("> ").lower()
    if cmd=='help':
        print("""
start-to start the car 
stop-to stop the car
quit-to exit
          """)
    elif cmd=='start':
        if started:
            print("car already started")
        else:
            started=True
            print('car started...Ready To Go!!')
    elif cmd=='stop':
        if stopped:
            print("car already stopped")
        else:
            stopped=True
            print('car Stopped!!')
    elif cmd=='quit':
        break
    else:
        print('sorry!I Dont Understand that')

#for loop
for item in 'python':
    print(item)
print('fruits')
for items in ['apple','mango','grapes']:
    print(items)
print('numbers from 0 to 9')
for item in range(10):
    print(item)
print("skip 2's from 5 to 20")
for item in range(5,20,2):
    print(item)
print("CALCULATING TOTAL COST:")
prices=[10,20,30]
total=0
for price in prices:
    total+=price
print(f"TOTAL PRICE= {total}")

#nested loops 
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
print("print f shape")
numbers=[5,2,5,2,2]
for num in numbers:
    output=''
    for i in range(num):
        output+='x'
        
    print(output)

#list
names=['annie','jose','luv','ajay','john']
print(names)
print(names[0])
print(names[-1])
print(names[0])
print(names[2:])
print(names[2:4])
print(names[:])
names[1]='joe'
print(names)
print("FIND LARGEST NUMBER IN A LIST")
numbers=[8,4,2,19,4,0]
grt=numbers[0]
for num in numbers:
    if grt<num:
        grt=num
print(f"GREATEST NUMBER IN THE LIST IS {grt}")

#2d lists
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[2][1])
for row in matrix:
    for item in row:
        print(item)
#list methods
numbers=[5,8,7,6,10]
print("add element at end")
numbers.append(20)
print(numbers)
print("add element at any position")
numbers.insert(36,4)
print(numbers)
print("remove element at end")
numbers.remove(6)
print(numbers)

print("remove element at end")
numbers.pop()
print(numbers)
print("to know index")
print(numbers.index(20))
print("check existence of an element in the list")
print(10 in numbers)
print("sort in ascending")
numbers.sort()
print(numbers)
print("delete all elements")
numbers.clear()
print(numbers)
print("remove duplicate elements in list")
nums=[2,2,4,6,6,1,3]
unique=[]
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)

#tuples
numbers=(5,1,2,3,2)
print(numbers[0])
print(numbers.count(2))
print(numbers.index(2))

#unpacking
coordinates=(1,2,3)
x,y,z=coordinates
print(x)
print(y)
print(z)

#dictionaries
customer={
    "name": "john smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate"))
customer["name"]="jack"
print(customer["name"])
print("PRINT PHONE NUMBER IN WORDS")
Nnum={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":'seven',
    "8":"eight",
    "9":"nine"
}
ph=input('phone: ')
output=""
for p in ph:
    output+=(Nnum.get(p,"!"))+ " "
print(output)

#emoji converter
message=input(">")
words=message.split(' ')
emojis={
    ":)" : "😊",
    ":(" : "😢",
    }
output=""
for word in words:
    output+= emojis.get(word,word)+ " "
print(output)


#functions, parameters, key word argument
def greet_user(firstname, lastname):
    print(f'Hi {firstname} {lastname}!')
    print('welcome aboard')
print("Start")
greet_user(firstname = "John", lastname= "Smith")
greet_user("Mary" , "Smith")
print("Finish")

#return statement
def square(number):
    return number * number
result = square(3)
print(result)
print(square(3))

#recreating the reusable function
def emoji_converter(message1):
    words=message1.split(' ')
    emojis={
        ":)" : "😊",
        ":(" : "😢",
    }
    output=""
    for word in words:
        output+= emojis.get(word,word)+ " "
    return output

message1=input(">")
print(emoji_converter(message1))

#exceptions
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')

#comments
#classes and constrructor
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw() 
point2 =Point()
point2.x = 1
print(point2.x)
#constructor
point = Point(10, 20)
point.x = 11
print(point.x)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()
bob = Person("Bob Smith")
bob.talk()

#inheritance
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.be_annoying()

#modules
import converters
from converters import kg_to_lbs
kg_to_lbs(100)
print(converters.kg_to_lbs(70))

#finding the max
from utils import find_max
numbers = [10,3,6,2]
max = find_max(numbers)
print(max)

#generating random value
import random
for j in range(3):
    print(random.random())
    print(random.randint(10,20))

members =  ['John', 'Mary', 'Bob' , 'Mosh']
leader = random.choice(members)
print(leader)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
dice = Dice()
print(dice.roll())

#files and directories
from pathlib import Path
path = Path()
for file in path.glob('*.py'):
    print(file)

