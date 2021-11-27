print()

print("hellow, welcome to my progrem !!\n")


word = input("Enter some string pleas:\n\n")


the_letter_should_be_replaeced = word[0:1] 
#print(the_letter_should_be_replaeced)
y = the_letter_should_be_replaeced
#print(y)

the_rest_of_the_sentence = word[1:]
#print(the_rest_of_the_sentence)
x = the_rest_of_the_sentence
#print(x)

after_replacing = x.replace(y, "e")
#print(after_replacing)

print()

new = y + after_replacing
print("your new word is:" ,new, "\n")

print("thank you for using my progrem !!\n")