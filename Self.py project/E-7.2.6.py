
print()

# לבדוק לגבי התנאי של האחד שווה אחד 

while 1 == 1:

    str_list = input("Enter a list of Ingredients plaes:\n\n")
    print()
    the_enterd_num = int(input("enter a number between 1 to 9: \n\n"))

    str_as_list = str_list.split(",")  # Python code to convert string to list

    print()

    if the_enterd_num == 1:
        print(str_as_list, "\n")
    

    elif the_enterd_num == 2:
        print("the length of the list is: ", len(str_as_list), "\n")

    elif the_enterd_num == 3:
        answer = input("Is the product on the list? \n\n")
        print(answer in str_as_list, "\n")

    elif the_enterd_num == 4:
        answer = input("How many times does this product appear in the list? \n\n")
        print(str_as_list.count(answer), "\n")

    elif the_enterd_num == 5:
        answer = input("Write down the name of the product you want to delete from the list: \n\n")
        str_as_list.remove(answer)
        print(str_as_list, "\n")

    elif the_enterd_num == 6:
        answer = input("Please indicate the product you would like to add to the list. \n\n")
        str_as_list.append(answer)
        print(str_as_list, "\n")

    elif the_enterd_num == 7:
        List_of_illegal_products = []

        for item in str_as_list:
            if len(item) < 3 or item.isalpha() == False:
                List_of_illegal_products += [item]
        
            else:
                continue

        print(List_of_illegal_products, "\n")

    elif the_enterd_num == 8:
        for item in str_as_list:
            if str_as_list.count(item) > 1:
                str_as_list.remove(item)
        
            else:
                continue

        print(str_as_list, "\n")

    elif the_enterd_num == 9:
        break



	








