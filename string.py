# Create a Python script that utilizes at least 5 different string methods (e.g., upper(), lower(), split(), replace(), find()) to perform the following tasks:
# Read a given string from user input
# Convert the string to uppercase and lowercase
# Split the string into substrings based on a specified delimiter
# Replace a specific substring with another
# Find the index of a specified character or substring within the string

string=input("enter a string: ")
s=string.upper()                     #upper method is used to covert the lowercase to uppercase
print(s)

string=input("enter a string: ") 
s=string.lower()                      #lower method is used to covert the uppercase to lowercase
print(s)


string=input("enter a string: ")
s=string.split()                     #it sepearte the word
print(s)


string=input("enter a string: ")     #it replace the wrod to another word
s=string.replace("python","java")
print(s)

string=input("enter a string: ")
s=string.find("python")               #find the index of the word
print(s)



