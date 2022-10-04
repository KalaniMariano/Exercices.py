''' Develop a program that reads the first term and ratio of an arithmetic progression.
At the end, show the first 10 terms of this progression'''

term = int(input("Fist term: "))
ratio = int(input("Ratio: "))
n = term + (10 - 1) * ratio
for i in range (term,n,ratio):
        print ("{} ".format(i), end=' > ')
print ("FINISHED")