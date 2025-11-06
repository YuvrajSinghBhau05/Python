#program to implement condtional statements
print("Break Example")
for i in range(1,10):
    if i==4:
        break
    print(i)
print("\n Continue Example")
for i in range(1,10):
    if i==5:
        continue
    print(i)
print("\n Pass Example")
for i in range(1,10):
    if i==3:
        pass
    print(i)