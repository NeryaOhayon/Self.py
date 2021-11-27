
print()

#this is the exercise with the three pigs.

num = int(input("enter a three digit number:\t\n"))

print()

x = num // 100 # pig number 1
y = num % 100
z = y // 10 # pig number 2
t = y % 10 # pig number 3

print("The total number of bricks collected by the piglets is",x + z + t,"bricks\n")

b = x + z + t
n = b // 3
d = b % 3

print("every pig will get",n,"bricks after equal division\n")

print("The rest of the division is",d,"bricks\n")

print(d == 0,"\n")