#File Handling
file1=open("file1.txt", "w")
file1.write("Hello There!")
file1.close()

file1 = open("file1.txt", "r")
print("Contents of the file: ")
print(file1.read())
file1.close()

file1=open("file1.txt", "r")
file2=open("file2.txt", "w")
file2.write(file1.read())
file1.close()
file2.close()
print("File copied successfully")