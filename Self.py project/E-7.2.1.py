print()

print("welcome to my function !!")

print()

def is_greater(my_list, n):
    """ The function receives two parameters: list and number - "n", and then the function returns a new list in which all the numbers greater than "n" from the received list. 
    :param my_list: Represents the list received from the user.
    :param n: The number being checked which of the numbers in the received list is larger than it. 
    :type my_list: "list". 
    :type n: "int" or "float". 
    :return: The function returns a new list containing all the organs larger than the number n.
    :rtype: "list". 
    """
    new_list = []
    for item in my_list:
        if item > n:
            new_list = new_list + [item]
            
        else:
            continue

    return new_list


def main():
    print(is_greater([1, 30, 90, 25, 60, 27, 28], 28))
    print()

if __name__ == "__main__":
    main()


