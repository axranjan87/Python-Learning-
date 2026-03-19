marks = {
    "Siddhi" : 98,
    "Riddhi" : 96,
    "Shivam" : 89
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Siddhi":97 , "Ayush": 88})
print(marks)
print(marks.get("Ayush"))  