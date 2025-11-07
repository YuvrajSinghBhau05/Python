#Program to update existing key values in a dictionary
student = {
    "name": "Akira Kenshin",
    "age": 18,
    "course": "Neuroscience with Physics",
    "grade": "F"
}
print("Original dictionary:")
print(student)
student["age"] = 21
student["grade"] = "A+"
student.update({"course": "Data Science", "grade": "A++"})
print("\nDictionary after updating values:")
print(student)

