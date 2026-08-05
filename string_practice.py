"""word = "Programming"
print(word[0])
print(word[-1])
print(word[3:])
print(word[:3])
c=0
const=0
vowels={'a'}
constant={'a'}
constant.clear()
word=input("Enter a string:")
vowels.clear()
for ch in word:
    print(ch)
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        c+=1
        vowels.add(ch)
    else:
        const+=1
        constant.add(ch)

print("Number of vowels in the string is:",c)
print("The vowels in the string are:",vowels)
print("The constant are:",constant)
print("the number of constant are:",const)

for index, ch in enumerate(word):
    print(f"{index}: {ch}")


x =input("Enter a string:")
print("-----With Slicing----- ")
if x==x[::-1]:
    print("Is palindrome")
else:
    print("IS not a palindrome")
print("-----With reverse method----- ")
rev="".join(reversed(x))
if x==rev:
    print("Is palindrome")
else:
    print("Is Not palindrome")


txt=input("Enter a string:")
cont={}
for i in txt:
    if i in cont:
        cont[i]+=1
    else:
        cont[i]=1
print(cont)


#Find all duplicate characters.
s = input("Enter the string:")
c=[]
for ch in s:
    if ch in c:
        continue
    else:
        c.append(ch)
print("first non-Repeating characters:",c[0])


s = input("Enter the string:")
c = list(dict.fromkeys(s))
print(c)
print("Non-Repeating characters:", c[0])

print("----- check Anagram ------")
s1=input("Enter first string:")
s2=input("Enter second string:")
s1="".join(sorted(s1.lower()))
s2="".join(sorted(s2.lower()))
if len(s1)==len(s2) and s1==s2:
    print("Is Anagram")
else:
    print("Is not Anagram")

s= input("Enter a string:")
s=s.split()
long=len(s[0])
sml=len(s[0])
word=""
sword=""
for i in s:
    if long <= len(i):
        long=len(i)
        word=i
    if sml >= len(i):
        sml=len(i)
        sword=i
print(f"the longest word is *{word}* and the length is: {long}")
print(f"the shortest word is *{sword}* and the length is: {sml}")
print("The number of words in the sentence are:",len(s))


s1 = input("Enter a string:")
n=" ".join(s1.split())
print(n)
# Output: "Hello world! This is a test."

s =input("Enter a string:")
s=s.title()
print(s)

s="hello word"
ch_dict={}
for ch in s:
    freq=s.count(ch)
    ch_dict[ch]=freq
print(ch_dict)
lst= list(ch_dict.keys())
print(lst[0])

"""
s = "hello word"

ch_dict = {}
for ch in s:
    ch_dict[ch] = ch_dict.get(ch, 0) + 1

print(ch_dict)
lst = list(ch_dict.keys())
print(lst[0])