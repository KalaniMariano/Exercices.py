phrase = str(input("Type a sentence: "))

length_phrase = len(phrase)

inverted_phrase = phrase[length_phrase::-1]

if inverted_phrase == phrase:
    print ("Your sentence is a palindrome :)\n")
else:
    print ("Your sentence is NOT a palindrome :(\n")
print (inverted_phrase)