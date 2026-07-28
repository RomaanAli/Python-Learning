numbers = {10, 20, 20, 30, 30}
print(numbers)

numbers.add(50)
numbers.add(100)
print(numbers)
x=numbers.pop()
print(numbers)
print(x)

numbers.update([60,70,80,90])
print(numbers)
numbers.remove(10)
print(numbers)
print("The length of the set is:",len(numbers))
numbers.discard(90)
print(numbers)
print("The length of the set is:",len(numbers))

