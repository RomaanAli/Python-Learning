import re
text="I bought 12 apples, 5 bananas, and 20 oranges."

print("\n-----",text)
match = re.search(r"\d+",text)
print("match by SEARCH:",match.group())

match=re.findall(r"\d+",text)
print("match all integers Findall: ",match)

match=re.findall(r"\w+",text)
print("match all words findall: ",match)

match=re.search(r"\s",text)
print("match all white-spaces by Search: ",match.group())

match=re.findall(r"\s+",text)
print("match all white-spaces by findall: ",match)

match=re.findall(r"[aeiou]",text)
print("match all Vowels are: ",match)
text1="123 45 678 246 79 100"
print("-----text: ",text1)
match=re.findall(r"\d{3}",text1)
print("match exact 3 digits: ",match)




