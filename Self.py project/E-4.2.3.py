
print()
print("Welcome to my degree conversion calculator !!\n")

Type = input("Select the type of degrees you want to convert:\n\n For degrees Celsius press: \'C\' \n For degrees Fahrenheit press: \'F\' \n\n print here:\t")

Type = Type.lower()

print()

deg = float(input("Now type the number of degrees you want to convert:\t"))

print()

if Type == "c":
    print(deg, "Celsius in Fahrenheit is", (9 * deg + 32 * 5 ) / 5, "defrees\n")
  

elif Type == "f":
    print(deg, "Fahrenheit in Celsius is", (5 * deg - 160) / 9, "defrees\n")

else:
    print("The software does not support this type of degrees\n")

print("Thank you for using my Conversion Calculator !!\n")    
