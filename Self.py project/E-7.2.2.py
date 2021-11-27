print()
print()

def numbers_letters_count(my_str):
    """The function accepts as a string parameter. The function returns a list in which the first member represents the number of digits in the string, and the second member represents the number of letters in the string, including spaces, periods, punctuation, and anything other than digits.
    :param my_str: The string that the function receives from the user.
    :type my_str: "str"
    :return: The function returns a list in which the first member represents the number of digits in the string, and the second member represents the number of letters in the string, including spaces, periods, punctuation, and anything other than digits.
    :rtype: "list". 
    """
    list = [0, 0]

    for item in my_str:
        if item.isdigit() == False:
           list[1] += 1
        
        elif item.isdigit() == True:
            list[0] += 1

        else:
            continue
    
    return list

def main():
    print()
    print(numbers_letters_count("Python 3.6.3"))
    print()

if __name__ == "__main__":
    main()
