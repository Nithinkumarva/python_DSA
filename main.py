'''print("Nithin\nNithin")
print(r"\tcurrent\new\folder")
# / is an escape character
# write a pogram to find odd and even numbers with function'''
'''def check(num):
    if num%2==0:
        print(num,"is even number")
    else:
        print(num,"is odd number")
check(10)

l= [ 1,2,3,4,5]
l.pop()
print(l)

dict={
    "name":"sriram",
    "geneder":"male",
    "age":20,
    "courses":["python","java","Data science"]
}
dict["name"]="Nithin"
dict.update({"course":  ,["python","java","Data science"]})
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())

def count(*args):
    print(type(args))
# count(1,2,3,4,5)
def dicts(**kwargs):
    print(type(kwargs))
# dicts(name="sriram",gender="male")
def default(name="sriram",gender="male"):
    print(name,gender,age,courses)
def default(geneder,age,name="Nithin"):
    print(geneder,age,name)

#oops
l=[1,2,3]
s="string"
len(l)
len(s)
# 4 pillars of oops
# 1. Inheritance:
# 2. Polymorphism:
# 3. Encapsulation:
# 4. Abstraction:
#take a string an input
# prinmt it back  by removing the fruit and last character of the input string
x = input("Enter a string: ")
print(x[1:-1])

#create an exampler while loop which will not terminate , and print n1 in each iteration
# and how will you stop the pogram manully?
while True:
    n1 = int(input("Enter a number: "))
    print(n1)'''

'''# take a number as input and find the sum of the numbers from 1 to that number by using for loop
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)

# take a number as input and find the sum of thew numbers from 1 to that number by using while loop
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)'''
# print("Vijay\nVijay\nVijay")
# print(r"\\tcurrent\\new\\folder")
# # \ is a escape character

# check if the number is even or odd using function
# def funce(a):
#     if a % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')

# a =  int(input())
# funce(a)

""" dictionary """  
# dict = {
#     "name": "Vijay",
#     "age": 20,
#     "gender": "Male",
#     "courses": ["Python", "Java", "C++"]
# }
# dict['age'] = 21
# dict.update({"name":"Vijay Rama Raju"})
# print(dict)
# print(dict.get("name"))
# print(dict.keys())
# print(dict.values())
# print(dict.items())

""" *args """
# def count(*args):
#     print(type(args))

# count(1,2,3,4,5)

# """ **kwargs """
# import pathlib
# import pathlib
# def count(**kwargs):
#     print(type(kwargs))

# count(name="Vijay", age=21, gender="Male", courses=["Python", "Java", "C++"])

# # default parameters should be last and unknown parameters should be first
# def default(a,b=10):
#     print(a,b)


# """OOPS"""

# """1. Polymorphism"""
# l = [1, 2, 3]
# s =  "Vijay"
# len(l)
# len(s)      

# Static typing will always require type declaration 
# Dynamic typing will not require type declaration


# x = "Vijay"
# print(x[-2:-5:-1])

# i= 1
# while i>0:
#     print("hi")

# print the sum of numbers from 1 to n using for loop
a  = int(input())
sum = 0
for i in range(1, a):
    sum+=i
print(sum)

#print the sum of numbers from 1 to n using while loop
sum=0
while a > 0:
    sum+=a
    a-=1
print(sum)

