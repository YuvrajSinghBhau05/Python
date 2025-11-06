#count Vowels, consonants, digitd, and length of the string
s=input("Enter a string:")
vow=0
con=0
dig=0
for ch in s:
    if ch.isdigit():
        dig+=1
    elif ch.lower() in "aeiou":
        vow+=1
    elif ch.isalpha():
        con+=1
print("Vowels:", vow)
print("Consonants:", con)
print("Digits:", dig)
print("Length:", len(s))