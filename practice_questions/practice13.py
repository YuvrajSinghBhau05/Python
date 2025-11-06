'''WAP to accept characters from user and print characters in capital or small letter'''
chr=input("Enter a character")
if chr==chr.lower():
    print(chr.upper())
else:
    print(chr.lower())
