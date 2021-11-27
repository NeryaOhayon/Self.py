print()

print("welcome to my progrem !!\n")

word = input("Please type any sentence to continue:\n\n")

print()

len = len(word)

h_str = len // 2

f_slice = word[:h_str]

s_slice = word[h_str:]

up = s_slice.upper()

print(f_slice + up, "\n")

print("thank you for using my progrem, i'll see yo later !\n")