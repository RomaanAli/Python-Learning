from collections import Counter
from collections import namedtuple
from collections import deque

def highest_frequency(s1):
    c = Counter(s1)
    max_char = c[0]
    for char,val in c.items():
        if val>c[max_char]:
            max_char=char
    return max_char

def check_anagram(s1,s2):
    return Counter(s1)==Counter(s2)

def extra_character(s1,s2):
    if len(Counter(s1))>len(Counter(s2)):
        return Counter(s1)-Counter(s2)
    else:
        return Counter(s2)-Counter(s1)

def odd_frequency(s):
    odd={}
    ctr=Counter(s)
    for i,val in ctr.items():
        if val%2 != 0:
            odd.update({i:val})
    return odd


s="aabbcdde"
non_rep=[]
ctr=Counter(s)
print(ctr)
for i in ctr:
    if ctr[i]==1:
        non_rep.append(i)
print(non_rep)
print(non_rep[0])

s="abcdefcad"
ctr=Counter(s)
for i in ctr:
    if ctr[i]>1:
        non_rep.append(i)

print(non_rep)

#highest frequency of the element in string
sr="Mississippi"
print(highest_frequency(sr))

#checking anagram
s1="Mississippi"
s2="Mississippi"
print("Checking anagram s1 : ",s1,"and s2 is: ",s2," ==result ",check_anagram(s1,s2))

#checking extra elements
s1="clothes"
s2="cloth"
print("checking extra characters-- s1:",s1,"and s2 is: ",s2,"and the ==result: ",extra_character(s1,s2))

#odd frequency elements
print("odd frequency of s1:",odd_frequency(s1))
print("odd frequency of s2:",odd_frequency(s2))

print("---------------NamedTuple-----------------------")

ct=Counter("hello world to python programming")
li=''.join((ct.elements()))
print(li)
print("the most common characters with frequency are:",ct.most_common())
print("The total of count of all values:  ",ct.total())

Student=namedtuple("Student",["name","age","department"])
student= Student("Romaan","23","Software Engineering")
print(student.name,student.age,student.department)
name,age,department=student
print("\nUnpacked the namedtuple:",name,age,department)
for i in student:
    print(i)
print("\nall fields of student object:",student._fields)
print("\nshowing as dict: ",student._asdict())

print("---------------Deque-----------------------")

numbers=deque([1,2,3,4,5,6,7,8,9,10])
print(numbers)
#for i in numbers:
#    print(i)
numbers.appendleft(0)
numbers.appendleft(100)
numbers.append(200)
print(numbers)
print("---removing item----")
print("using the pop last element:",numbers.pop())
print("using the popleft() first value:",numbers.popleft())
print("using the popleft() first value--again:",numbers.popleft())

numbers.rotate(3)
print(numbers)
