'''with open("file1.txt", "w") as file:
    file.write("Hello, World!")
with open("file1.txt", "r") as file:
    print(file.read())
with open("file1.txt", "a") as file:
    file.write("python programming") '''

'''#task1
#keep asking valid intiger number
#if not valid intiger number then print error 
while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        print("You entered:", num)
        break
    else:
        print("Please enter a valid number.")
#task2
#handle index error while accessing list elements if it is out of range of handle it
l = [1,2,3,4,5,6,7,8,9,10]
try:
    index = int(input("Enter the index: "))
    print("Element:", l[index])
except IndexError:
    print("Error! Index is out of range.")'''




