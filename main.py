#print(True and False)
#print(True & True)

"""avoid and or not is
    ++ --"""
import functools
from _ast import Import

#import self as self

"""for is a loop while is not a loop"""

"""we have while in break"""

"""in for loop we know what we are looking for, in while loop we don't know what we are looking for"""

"""we can use debugger to make sure the code wont be stuck in infinite loop"""

"""use scratches file to check"""

"""Docstring should have inputs, outputs, parameters"""

"""def func-name (x: int) ->list (list is the data type)"""

"""Never change the iterable while iterating it.
Bad example of doing it below"""

"""id_list = [1,2,3,4]
id_list2 =
for id in id_list:
    print (id)
    id_list.remove(id)"""

"""class Person:
    def __init__(self, name, age, height, weight, occupation, relationship_status):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.occupation = occupation
        self.relationship_status = relationship_status


user1 = Person("john", 26, 6, 80, "student", "single")
user2 = Person("perk", 22, 5.10, 65, "student", "single")

print(user1.relationship_status)
print(user2.relationship_status)
print(user2.name)

if user2.relationship_status == "single":
    print("Are u interested in anyone?")

else:
    print("ALready commited.")"""


"""class Car:
    
    def __init__(self, BMW, Audi, Porsche, Honda, Toyota, Nissan):
        self.BMW = 2010
        self.Audi = 2011
        self.Porsche = 2009
        self.Honda = 2008
        self.Toyota = 2016
        self.Nissan = 2013

        def name(self, car_name, model, get):
            self.car_name = get.car_name
            self.model = get.model
            return1 =""
            if model < 2010:
                ph=print("It's not good.")

            else:
                ph2=print("It's good.")

        return return1

if __name__ == '__main__':
    main()"""

"""class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)

    def bark(self):
        print("security")

    def run(self):
        print("fetch")

    def pamper(self):
        print("love")

    def add_x(self, x):
        return x+1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

d1 = Dog("Tim", 7)
print(d1.name)
d2 = Dog("Scooby", 2)
print(d2.name)
d1.run()
print(d1.add_x(5))
print(type(d1))
"""

"""
class Student():

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)


student_1 = Student("Jim", 20, 92)
student_2 = Student("Bill", 20, 85)
student_3 = Student("Jack", 20, 95)

subject = Course("Science", 3)
subject.add_student(student_1)
subject.add_student(student_2)
subject.add_student(student_3)

print(subject.get_average())
"""

#There seems to be an issue, try fixing later.
"""class Votes():

    def __init__(self, no_votes, max_candidates):
        self.no_votes = no_votes
        self.max_candidates = max_candidates


    def constituancy(self, candidate, no_votes_manchester, no_votes_lowel, no_votes_salem, no_votes_nashua):
        self.candidate = candidate
        self.no_votes_manchester = no_votes_manchester
        self.no_votes_lowel = no_votes_lowel
        self.no_votes_salem = no_votes_salem
        self.no_votes_nashua = no_votes_nashua
        self.areas = (self.no_votes_manchester, self.no_votes_lowel, self.no_votes_salem, self.no_votes_nashua)
        self.value = (self.no_votes_manchester + self.no_votes_lowel + self.no_votes_salem + self.no_votes_nashua)
        return self.value
            #value += self.no_votes


    def add_candidates(self, candidates):
        self.candidates = candidates
        self.candidates = []
        if len(self.candidates) < self.max_candidates:
            self.candidates.append(self.candidate)
            return True
        return False


election = Votes(1000000, 2)
candidate1 = election.constituancy("Jack", 45000, 40000, 30000, 20000)
candidate2 = election.constituancy("Bob", 20000, 30000, 40000, 20000)
election.add_candidates(candidate1)
election.add_candidates(candidate2)

print(Votes.e)"""



"""issue with this code too
class Students:
    def __init__(self, name, age, major, max_students):
        self.name = name
        self.age = age
        self.major = major
        self.max_students = max_students
        self.students = []


    def add_studentz(self, add_students):
        self.add_students = add_students
        if len(add_students) < self.max_students:
            self.students.append(add_students)
            return True
        return False

total_students = Students
student1 = ("jack", 20, "science")
student2 = ("jill", 19, "commerce")
print(total_students.add_studentz(2))"""

"""
Inheritance pattern
"""
"""class Pet:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def show(self):
        print(f'My name is {self.name}, and I am {self.age} years old.')

class Cat(Pet):
    def speak(self):
        print("Mewo")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Cat("Jenner", 3)
print (p)
d = Dog("Scooby", 5)
print(d)"""

#class
"""class SoftwareEngineer:

    alias = "Keyboard magician"

    def __init__(self, name, age, position, salary, years):
        #instance attributes
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.years = years


    def experience(self, years):
        self.years = years


#instance
se1 = SoftwareEngineer("Jack", 25, "senior developer", 12000)
print(se1.name , se1.age)
se2 = SoftwareEngineer("Lisa", 35, "CTO", 25000)
print(se2.name, se2.salary)
print(SoftwareEngineer.alias)"""


"""
class Course:

    def __init__(self, stu_name, maths, science, full):
        self.stu_name = stu_name
        self.maths = maths
        self.science = science
        self.full = full



    def avg(self):
        return self.maths+self.science/self.full


s1 = Course("jack", 20, 30, 100)
print(s1.avg())"""

"""
class School:
    def __init__(self, name, age, clas):
        self.name = name
        self.age = age
        self.clas = clas
        self.list = []


    def max_students(self, mx_students):
        self.mx_students = mx_students



    def add_students(self, student):
        self.student = student
        if len(self.list)<self.mx_students:
            self.list.append(self.student)
            return True
        return False
"""
"""
radius = int(input("Enter the radius:"))
area = (radius * radius) * 3.1415
print("The area of a circle with radius", radius, "is:", area)
"""

"""
grocery_item = ""
while grocery_item != "done":
    grocery_item = input("Please write down an item to add to your grocery list. When you are done writing the list simply type: done")
    print(grocery_item)
"""
"""
grocery_item = ""
grocery_list = []
while grocery_item != "done":
    grocery_item = input("Please write down an item to add to your grocery list. When you are done writing the list then simply type: done")
    if grocery_item == 'done':
        continue
    else:
        print("adding the item to the list")
        grocery_list.append(grocery_item)
print("Here is our grocery list:")
print(grocery_list)
"""
"""
print(9 // 3)
print(26 // 5.0)
print(7%3)
print(11//3)
"""
"""hobbies = ([
            ['gardening', 'activity', 10],
            ['soccer', 'games', 1]
            ])
print(hobbies[1][0])"""
"""
list2 = {}
list = {"sdjflksj": 10, "dsjflkajds": 32, "sdjlfjaslf": 45}
if list.keys() == int:
    list2.append(list.keys())
    return (list2())
else:
    print("nill")
print(list2)
"""
"""class hobbies:
   def __init__(self, hobby_list, hobby_activity):
      self.hobby_list = hobby_list
      self.hobby_activity = hobby_activity

   def add_score:
      for self.hobby_activity in
      for self.hobby_activity in self.hobby_list:
         print(list(self.hobby_activity.values()))

list1 = ("sdljsljfl", 2823)

"""
"""print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello", 45)"""

"""print(str(17))
print(str(123.45))
print(type(str(123.45)))"""

"""message = "What's up, Doc?"
n = 17
pi = 3.14159

print(message)
print(n)
print(pi)"""

"""message = "What's up, Doc?"
n = 17
pi = 3.14159

print(type(message))
print(type(n))
print(type(pi))"""

"""y = 3.14
x = len("hello")
print(x)
print(y)

print(2 * len("hello") + len("goodbye"))
"""
"""
x = 2
y = 1
print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))"""
"""
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
print (2**2)"""

"""print(16 - 2 * 5 // 3 + 1)"""

"""current_time = input("what is the current time (in hours)?")
wait_time = input("How many hours do you want to wait")

print(current_time)
print(wait_time)"""

"""subtotal = input("Enter total before tax:")
tax = .08 * subtotal
print("tax on", subtotal, "is:", tax)"""

"""i = 10
z = 12

while z<i:
    print("hi")
    z+=z"""

"""current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)"""

"""current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait"

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)
"""
"""
a = input('wpisz godzine')
x = input('wpisz liczbe godzin')
int(x)
int(a)
h = x // 24
s = x % 24
print (h, s)
a = a + s
print ('godzina teraz', a)"""

"""str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)"""

"""import random
prob = random.random()

diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)"""

"""class Point:
    Point class for representing and manipulating x,y coordinates. 

    def __init__(self):

        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print("Nothing seems to have happened with the points")
"""


"""class Point:
    Point class for representing and manipulating x,y coordinates. 

    def __init__(self):
        self.x = 0
        self.y = 0


p = Point()  # Instantiate an object of type Point
q = Point()  # and make a second point

print(p)
print(q)

print(p is q)"""

"""
class NumberSet:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

p = NumberSet(10,2)
print(p.getX()+p.getY())
"""
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)"""
"""
print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))"""
"""
accum = 0
for w in range(11):
    accum = accum + w
print(accum)

# or, if you use two inputs for the range function

sec_accum = 0
for w in range(1,11):
    sec_accum = sec_accum + w
print(sec_accum)"""
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for w in nums:
    count = count + 1
print(count)"""

"""
t = (5,6)
print(type(t))

l = [2,3]
print(type(l))

x = (5)
print(type(x))"""

"""
school = "Luther College"
m = school[2]
print(m)

lastchar = school[-1]
print(lastchar)"""
"""
numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])"""

"""
prices = (1.99, 2.00, 5.50, 20.95, 100.98)
print(prices[0])
print(prices[-1])
print(prices[3-5])"""
"""
s = "python rocks"
print(s[3])"""
"""
lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
output = lst[34]
print(output)"""
"""
new_lst = ["NFLX", "AMZN", "GOOGL", "DIS", "XOM"]
part_of_new_lst = new_lst[0]
print(part_of_new_lst)"""
"""
lst = [0]
n_lst = lst[0]

print(lst)
print(n_lst)
"""
"""
fruit = "Banana"
print(len(fruit))
"""
"""
fruit = "Banana"
sz = len(fruit)
print(sz)"""
"""
fruit = "grape"
midchar = fruit[len(fruit)//2]
print(midchar)

fruits = 'orange'
midchar2 = fruits[len(fruits)//2]
print(midchar2)
"""
"""
alist = ["hello", 2.0, 5]
print(len(alist))
print(len(alist[0]))
"""
"""
singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])"""

"""fruit = "banana"
print(fruit[:3])
print(fruit[3:])
print(fruit[1:])


a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])"""
"""
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)"""

"""
medals = {"gold" : 33, "silver" : 17 , "bronze" : 12}
print(medals)"""

"""
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places ["Brazil"] = 2016
print(places)
"""
"""
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers['Phelps'] = swimmers['Phelps'] + 5
print(swimmers)
"""
"""
inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for avalue in inventory.values():
    print("Got key", avalue, "which maps to ", inventory[avalue])

ks = list(inventory.values)
print(ks)
print(ks[0])"""

"""s = (10,2,3,4,5,6,7)
x = []
for i in s:
    if i<10:
        x.append(i)
print(x)"""

"""class Animal:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def limbs(self):
        return self.x + self.y

spider = Animal(4,4)
dog = Animal(2,2)
spider_limbs = spider.limbs()
print(spider_limbs)"""

"""import math

class Point:
    def __init__ (self, intX, intY):
        self.x = intX
        self.y = intY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrgin(self):
        return((self.x**2) + (self.y**2)) ** 0.5

def distance(point1, point2):
    xdiff = point2.getX()-point1.getX()
    ydiff = point2.getY()-point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4,3)
q = Point(0,0)
print(distance(p,q))"""

"""swimmers = {"Mike": 4, "Jack": 8, "Jonas": 16, "Phelps": 15}
swimmers["Phelps"] = swimmers["Phelps"] + 5
print(swimmers)
"""

"""students_grades = {"Mike": 82, "Taylor": 78, "Ross": 90}
students_grades["Taylor"] = students_grades["Taylor"] + 10
print(students_grades)
"""
"""
inventory = {'apples': 430, 'bananas': 800, 'mangoes': 400}
for akey in inventory.keys():
    print("Got key", akey, "which maps to ", inventory[akey])

ks = list(inventory.keys())
print(ks)
print(ks[0])"""
"""
inventory = {"mike": 79, "jake": 82, "jonathan": 79}
for key in inventory.keys():
    print(key)"""
"""
inventory = {"jack": 50, "mike": 82, "Robin": 63}
list(inventory.values())

for key in inventory.values():
    print(f'Got keys {inventory.values()}')"""

"""inventory = {"robin": 50, "mike": 80, "kevin": 83}
list(inventory.items())

for k, v in inventory.items():
    print(f'Got Key {k}, and it maps to {v}')
"""
"""
inventory = {"robin": 50, "mike": 80, "kevin": 83}
list(inventory.items())

for k, v in inventory.items():
    print(f'Got key {k} and the value {v}')
"""

"""inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries",0))
"""
"""
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
list(inventory.items())
print(inventory.items())
print(inventory)"""
"""
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])"""
"""
f = ('oufioajslfjsiufudsifjsiofusiofjshfiukkjrhiusyisfuiusdufisuf'
         'sdfjdsfiusdfosifjsdfkfksjhfkjdsfh'
         'sdflkjdfksjiuynxcvxnbcvnbzkhyiujlnr,mbuxiyvxiucvoijv'
         'dkhsiuvjljn')
#now txt is one long string containing all characters
t_count = 0 #initialize the accumulator variable
for c in f:
    if c == 's':
        t_count = t_count + 1 #increment the counter
print("t: " + str(t_count) + " occurences")"""

"""
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
s_count = 0 # initialize the s counter accumulator as well
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the t counter
    elif c == 's':
        s_count = s_count + 1
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")"""
"""
string1 = "Hello, my name is Mike."
name_count = 0
for xyz in string1:
    if xyz == 'e':
        name_count += 1
print (name_count)"""

"""
students = {'jack': 18, 'jill': 17, 'mike':20}
for k, v in students.items():
    print("Key " + str(k) + " Value " + str(v))"""
"""
f = ('ljsdlfuosfslkjflsn,wenrkjewhyiuvjdkjxncvvkhdsiueworu')
#now txt is one long string containing all the characters
letter_count ={}
for c in f:
    if c not in letter_count:
        letter_count[c] = 0
    else:
        letter_count[c] = letter_count[c] + 1

print("t " + str(letter_count['t']) + 'occurences')"""

# ENUMERATE

"""players = ["curry", "jonas", "jack", "chris", "lebron"]
for x, element in enumerate(players):
    print(x, element)
"""
"""
g = 'hey'
f = list(enumerate(g))
print(f)"""
"""
name = "Mike"
for k, v in enumerate(name):
    print(k, v)
"""

"""print({i:v for i,v in enumerate ("hey")})"""

"""print({str(v) for index, value in enumerate([8686, 3438, 34, 433434])})"""
"""
seasons = ['spring', 'summer', 'fall', 'winter']
for season in range(len(seasons)):
    print(season, seasons[season])"""
"""
f = open('scarlet.txt', 'r')
txt_lines = f.readlines()
# now txt_lines is a list, where each item is one
# line of text from the story
print(len(txt_lines))"""
"""
sentence = ("Hello, my name is Jackdsfdjljsdlfjoieor is my")
word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)


sentence = ("Hello, my name is Jackdsfdjljsdlfjoieor is my")
word_count = {}

for word in sentence:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)"""
"""
sentence = ("helleoo")
letter_count = {}

for letter in sentence:
    if letter not in sentence:
        letter_count[letter] = 0

    else:
        letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)

letter_values = letter_count

total = 0
for letter in letter_count:
    if letter in letter_values:
        total = total + letter_values[letter] * letter_count[letter]

print(total)"""
"""
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4,
          "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0

for i in travel:
    total = total + travel[i]

print(total)"""
"""
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4,
            "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3,
            "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4,
            "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4,
            "ANTHRO 101": 4}
total_credits = 0
for credit in schedule:
    total_credits = total_credits + schedule[credit]

print(total_credits)"""


"""test_math_func"""
"""def add(x, y=2):
    return x+y

def product(x, y=2):
    return x*y
"""
"""
class Food():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getprice(self):
        return self.price

    def __str__(self):
        return self.name + ":" + str(self.getprice())

def buildmenu(names, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], costs[i]))
    return menu

names = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Apple', 'Donut', 'Cake']
costs = [250, 150, 180, 70, 65, 55, 120, 350]

Foods = buildmenu(names, costs)
n=1
for el in Foods:
 print(n, '.', el)
 n = n+1
 """

#To check whether given key exists
"""dict = {1: 10, 2: 14, 3: 58, 4: 89}
def is_key_present(x):
    if x in dict:
        print("x is present")
    else:
        print("x is not present")

is_key_present(9)
is_key_present(2)
"""

#To add key
"""dict = {4: 10, 5: 454}
print(dict)
dict.update({6:99})
print(dict)"""

#concatenate dictionaries
"""dict1 = {1:10, 2:20, 3:30}
dict2 = {4:40, 5:50, 6:60}
dict3= {}
for d in (dict1, dict2): dict3.update(d)
print(dict3)"""

"""#concatenate dictionaries
year_2019 = {"Mike":490, "Jack":489}
year_2020 = {"John":493, "Rob":489}
toppers = {}
for students in (year_2019, year_2020): toppers.update(students)
print(toppers)"""

