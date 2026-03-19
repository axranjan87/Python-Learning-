name = "ayush"
print(len(name))   #@length function

print(name.endswith("ush"))   #@
print(name.startswith("Ayu")) #@\
print(name.capitalize())






""" >>> NOTES
1. lower()
String ko lowercase me convert karta hai.

text = "HELLO"
print(text.lower())

Output:
hello

2. upper()
String ko uppercase me convert karta hai.

text = "hello"
print(text.upper())

Output:
HELLO

3. strip()
String ke start aur end ke extra spaces remove karta hai.

text = "  python  "
print(text.strip())

Output:
python

4. replace()
String ke andar kisi word ko replace karta hai.

text = "I like Java"
print(text.replace("Java", "Python"))

Output:

I like Python

5. split()
String ko list me divide karta hai.

text = "apple,banana,mango"
print(text.split(","))

Output:
['apple', 'banana', 'mango']

6. join()
List ko string me convert karta hai.

words = ["I", "love", "Python"]
print(" ".join(words))

Output:
I love Python

7. find()
String me character ya word ki position batata hai.

text = "Hello Python"
print(text.find("Python"))

Output:
6

8.count()
String me koi character kitni baar aaya hai.

text = "banana"
print(text.count("a"))

Output:
3

9. startswith()
Check karta hai ki string kisi word se start ho rahi hai ya nahi.

text = "Python is easy"
print(text.startswith("Python"))

Output:
True

10. endswith()
Check karta hai ki string kisi word se end ho rahi hai ya nahi.

text = "file.txt"
print(text.endswith(".txt"))

Output:
True"""