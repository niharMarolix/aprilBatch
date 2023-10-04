'''
Write a program that prompts the user to enter a number. 
If the number is positive, the program should print the square 
root of the number. If the number is negative, 
the program should print an error message and 
ask the user to try again. If the number is zero, 
the program should print a message saying that the 
square root of zero is zero.
'''
num = int(input("enter a number: "))

if num>0:
    num = num**0.5
    print(num)
elif num<0:
    print("try again")
else:
    print("square root of zero is zero")
