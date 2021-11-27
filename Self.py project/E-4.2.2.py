 #E-4.2.2

print("\n")

print("wellcome to my progrem\n")

word = input("Enter a word please and the software will check if the word is a palindrome:\n\n")

print("\n")

reword = word.replace(" " , "")

upper_word = reword.upper()

The_opposite_word = upper_word[::-1]

if upper_word == The_opposite_word:
	print("ok\n")
else:
	print("not\n")