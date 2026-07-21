'''#errors
value error - data type mismatch
type error - operation are incompatible with data type
Idex error - index is out of range'''

'''#x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
try:
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("done")'''


'''for i in range (5):
    if i == 4:
        break
    print(i)
else:
    print("done")
'''

'''try:
    a=int(input("Enter a number: "))
    print(a) 
except ValueError as e:
    print(e)
else:
    print("done")
'''
#to thow an error
a=int(input("Enter a number: "))
if a<0:
    raise ValueError("number of negative")
else:
    print(a)
