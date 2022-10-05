phrase = str(input("Type a sentence: "))

length_phrase = len(phrase)

inverted_phrase = phrase[length_phrase::-1]
list_phrase = phrase.split()
join_list_phrase = ''.join(list_phrase)
list_inverted_phrase = inverted_phrase.split()
join_list_inverted_phrase = ''.join(list_inverted_phrase)

if join_list_inverted_phrase == join_list_phrase:
    print ("Your sentence is a palindrome :)")
else:
    print ("Your sentence is NOT a palindrome :(")
