'''n=5
for i in range(n):
    print("*",end=" ")'''    

'''n = 5
for i in range(n):
    print("* " * n)'''


'''n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''


'''#right angle triangle
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''

'''#inverted right angle triangle
n=5
for i in range (n):
    for j in range(n-i):
        print(" * ",end=" ")
    print()'''



'''#Right-Aligned Triangle  
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''        


'''#Inverted Right-Aligned Triangle  
n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()'''


'''#symmetric full pryramid
n=5
for i in range(n):
    for j in range(n+i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()'''

'''#diamond pattern
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n-2, -1, -1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()'''

'''#inverted symatric full pryramid
n = 5
for i in range(n-1, -1, -1):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()'''

'''# Armstrong number
n=int(input("Enter the number:"))
total=0
temp=n
while temp>0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")'''


'''# Hollow square pattern
size = 5
for row in range(size):
    for column in range(size):
        if row == 0 or row == size - 1 or column == 0 or column == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''



'''# Pascal's triangle pattern
rows = 5
for row in range(1, rows + 1):
    number = 1
    for space in range(rows - row):
        print(" ", end=" ")
    for column in range(1, row + 1):
        print(number, end="   ")
        number = number * (row - column) // column
    print()  ''' 

