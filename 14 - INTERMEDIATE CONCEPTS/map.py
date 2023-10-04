def square( element):
    return element**2

arr1 = [1,2,3,4,5]
sqr = map(square,arr1)
sqrdList = []
for i in sqr:
    sqrdList.append(i)
print(sqrdList)