from collections import Counter
from operator import truediv

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
print(check_anagram(s1,s2))

s1="mississippiioo"
s2="mississippi"
print(extra_character(s1,s2))


