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
print("----------------------")
#other operatores
a={1,2,3,4,5,}
b={6,7,8,2,3,4}
#intersection
print("The intersection of sets:",a&b)
print("The union of sets:",a|b)
print("The difference of sets a to b:",a-b)
print("The difference of sets b to a:",b-a)
print("The difference of sets a to a:",a-a)
print("Find 6 in b:",6 in b)
print("Find 6 not in b:",6 not in b)
a={1,2,3,4}
b={1,2,3,4}
print(a.isdisjoint(b))
print(a.issuperset(b))
print(b.issubset(a))

fs=frozenset({1,2,3,4})
print(fs)