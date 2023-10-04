# numbers = [2, 3, 4, 5]
# product = 1
# for i in range(len(numbers)):
#     product = product*numbers[i]
# print(product)
from functools import reduce

def product(x,y):
    return x*y

numbers = [2, 3, 4, 5]
resProduct = reduce(product, numbers)
print(resProduct)
