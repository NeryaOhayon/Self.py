

# E-5.3.5 - distance function . 
# abs() = Calculating the absolute value

print()

#def distance(num1, num2, num3):
   #if (ABS = abs(num1 - num2) == 1 or abs(num1 - num3) == 1) and ()
    
#def distance(num1, num2, num3):
    #ABS = abs(num2 - num1) >= 2  and abs(num2 - num3) >= 2 or abs(num3 - num1) >= 2 and abs(num3 - num2) >= 2
    #print(ABS)


    # Need now just combine the first condition with the second condition and then I solved the exercise.
    # I will probably need to change the form of writing I did so that I can adapt to writing terms and that you will connect to the next terms.
    # Then check if "Abs" should be deleted.
    

def distance(num1, num2, num3):
    if (abs(num1 - num2) == 1 or abs(num1 - num3) == 1) and (abs(num2 - num1) >= 2  and abs(num2 - num3) >= 2 or abs(num3 - num1) >= 2 and abs(num3 - num2) >= 2):
        print("True")
    else:
        print("False")

distance(1, 2, 10)

print()

distance(4, 5, 3)

print()