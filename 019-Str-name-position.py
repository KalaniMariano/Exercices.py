n = str(input("Type a full name: "))
s = n.split() #separating the name in a list and saving in variable "s"
print (s)
print (f"The first name is: {s[0]}")
print (f"And the last name is: {s[len(s)-1]}")