def checkEven(number):
    return number % 2==0

arr1 = [1,2,3,4,5,6,7,8,9,10]
even = filter(checkEven, arr1)

evenArray = []

for i in even:
    evenArray.append(i)

print(evenArray)

