#String concatenation
str1='hello'
str2="world"
print(str1+" "+str2)


#String replication
str1="\nHappy "
print(str1*5)


#Length of a string
str1="\nHELLOsenku"
print(len(str1))


#Converting to upper and lower case
str1="\nben tennyson"
str2=str1.upper()
print(str2)
print(str2.lower())


#Reversing a string
str1="\nMathew McCounghey"
print(str1[::-1])


#String split
str1="\nI hate Coding"
words=str1.split()
print(words)


#Pallindrome check
a=input("\nEnter string: ").lower()
if a==a[::-1]:
    print("Pallindrome")
else:
    print("Not Pallindrome")


#Join list of strings
a=["\nI","like","mango"]
res="".join(a)
print(res)


#Find a substring
str1=input("\nEnter string(find): ")
a=input("String you want to find: ")
index=str1.find(a)
print(index)


#Replace a string
str1=input("\nEnter string(replace): ")
str2=input("String you want to replace:")
str3=input("New string:")
rep=str1.replace(str2,str3)
print(rep)


#check if string contains substring
str1=input("Enter the string(check in): ")
str2=input("enter the string to want to check: ")
print(str2 in str1)


#count occurence of ch
str=input("Enter string(count): ")
str1=input("Enter character to want to count: ")
res=str.count(str1)
print(res)


# Check if string starts with a substring
str=input("Enter string(start): ")
str1=input("Enter substring to check: ")
res=str.startswith(str1)
print(res)


# Check if string ends with the substring
str=input("Enter string(end): ")
str1=input("Enter substring to check: ")
res=str.endswith(str1)
print(res)


# Remove leading whitespaces
str=input("Enter string: ")
res=str.lstrip()
print(res)


# Remove trailing whitespaces
str=input("Enter string: ")
res=str.rstrip()
print(res)


# Remove both leading and trailing whitespaces
str=input("Enter string: ")
res=str.strip()
print(res)


# Capitalize first letter
str=input("Enter string: ")
res=str.capitalize()
print(res)


# Swapcase of string
str=input("Enter string: ")
res=str.swapcase()
print(res)


# Check if all characters are alphabets
str=input("Enter string: ")
res=str.isalpha()
print(res)


# Check if all characters are digits
str=input("Enter string: ")
res=str.isdigit()
print(res)


# Check if string is alphanumeric
str=input("Enter string: ")
res=str.isalnum()
print(res)


# Check if a string is in lowercase
str=input("Enter string: ")
res=str.islower()
print(res)


# Check if a string is in uppercase
str=input("Enter string: ")
res=str.isupper()
print(res)


# Check if a string is in title case
str=input("Enter string: ")
res=str.istitle()
print(res)


# Convert to title case
str=input("Enter string: ")
res=str.title()
print(res)


# Find minimum character in string
str=input("Enter string: ")
res=min(str)
print(res)


# Find maximum character in string
str=input("Enter string: ")
res=max(str)
print(res)


# Convert string to list of characters
str=input("Enter string: ")
res=[]
for c in str:
    res.append(c)
print(res)


# Remove specific characters from string
str=input("Enter string: ")
chars=input("Enter characters to remove: ")
res=""
for c in str:
    if c not in chars:
        res+=c
print(res)


# Count occurrences of substring
str=input("Enter string(count): ")
sub=input("Enter substring to count: ")
res=str.count(sub)
print(res)


# Check if string contains only white spaces
str=input("Enter string: ")
res=str.isspace()
print(res)


# Extract substring using slice
str=input("Enter string: ")
start=int(input("Enter start index: "))
end=int(input("Enter end index: "))
res=str[start:end]
print(res)


# Center align a string
str=input("Enter string: ")
width=int(input("Enter width for center align: "))
res=str.center(width)
print(res)


# Left align a string
str=input("Enter string: ")
width=int(input("Enter width for left align: "))
res=str.ljust(width)
print(res)


# Right align a string
str=input("Enter string: ")
width=int(input("Enter width for right align: "))
res=str.rjust(width)
print(res)


# Convert string to ASCII values
str=input("Enter string: ")
res=[]
for c in str:
    res.append(ord(c))
print(res)


# Format a string using format()
str=input("Enter string: ")
res="Formatted string: {}".format(str)
print(res)


# Format strings with f-strings
str=input("Enter string: ")
res=f"Formatted string: {str}"
print(res)


# Count vowels in a string
str=input("Enter string: ")
vowels="aeiouAEIOU"
res=0
for c in str:
    if c in vowels:
        res=res+1
print(res)


# Find words with specific length
str=input("Enter string: ")
length=int(input("Enter word length to find: "))
words=str.split()
res=[]
for w in words:
    if len(w)==length:
        res.append(w)
print(res)


# Remove digits from string
str=input("Enter string: ")
res=""
for c in str:
    if not c.isdigit():
        res+=c
print(res)


# Remove punctuation from string
import string
str=input("Enter string: ")
res=""
for c in str:
    if c not in string.punctuation:
        res+=c
print(res)


# Sort characters in a string
str=input("Enter string: ")
chars=[]
for c in str:
    chars.append(c)
chars.sort()
res=""
for c in chars:
    res+=c
print(res)


# Find longest word in a string
str=input("Enter string: ")
words=str.split()
res=""
max_len=0
for w in words:
    if len(w)>max_len:
        max_len=len(w)
        res=w
print(res)


# Reverse words in a string
str=input("Enter string: ")
words=str.split()
res=""
for i in range(len(words)-1,-1,-1):
    res+=words[i]
    if i!=0:
        res+=" "
print(res)
