#PythonCourse
#ByMoshHamedani
#FOR_DUMMIES
#Learnt By Cephas Cardozo

#imports
import math

#PRINT_STATEMENT
print("DOG\n")
print('\/')
print('o----')
print(' ||||\n')
print('*' * 10)

#VARIABLES

#string
name = "cephas"
#integer
price = 10
#float
rating = 4.9
#boolean
is_published = True

print(price)

#exercise_1
patient_name = "John Smith"
patient_age = 20
is_patient_new = True

#GETTING_INPUT
main = input("What's your name?\n: ")
print(f"Hey there, {main} ")

#exercise_2
person_name = input("Whats your name?/n : ")
fav_color = input("Whats your fav color?\n : ")
print(f"{person_name} likes {fav_color}")

#TYPE_CONVERSION

#int()
#float()
#bool()
birth_year = int(input('Birth Year: '))
age = 2022 - birth_year
print(age)
print(type(birth_year))

#exercise_3
weight = int(input("\nWhats your weight in pounds / lbs: "))
to_kilo = int(weight / 2.20462262)
print(to_kilo)

#STRINGS
course = "Python for 'Beginners' !"
greet = '''
Hi John, 
How r you
Today!
'''
print(course[0:3])

#FORMATED_STRINGS
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
print(msg)

#STRING_METHODS
course_new = "Python for Beginners"
print(len(course_new))
print(course_new.upper())
#find() - to find the string index value
print(course_new.find('o'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course_new)
#First letter of each word after a space Capitalized
print(course_new.title())

#ARITHEMETIC_OPERATIONS
# + - ADD
# - - SUBTRACT
# * - MULTIPLY
# / - DIVIDE BUT WITH FLOAT
# // - DIVIDE BUT VALUE OUTPUT AS AN INTEGER
# % - GIVES REMAINDER
# += - INCREMENTING
# -= - DECREMENTING

#OPERATOR_PRECEDENCE
xy = 10 + 3 * 2
xz = (2 + 3) * 10 - 3
print(xz)
#Exponentiation 2**2
#Multiplication or Division
#Addition or Subtraction

#MATHS_FUNCTIONS
xj = 2.9
#round() - to round
#abs() - always returns a positive number / value
print(round(xj))

#ceil = round
#floor = base
print(math.ceil(2.9))
print(math.floor(2.9))
