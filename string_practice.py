word = "Programming"
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


