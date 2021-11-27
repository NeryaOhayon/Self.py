print()

def shift_left(my_list):
    """The function receives a list of length 3 and returns a new list moved one step to the left.
    :param my_list: The list that the user enters into the function.
    :variable first_character: Represents the first organ in the list received from the user.
    :variable second_character: Represents the second organ in the list received from the user.
    :variable third_character: Represents the third organ in the list received from the user.
    :variable the_new_list: Represents the new list.
    :type my_list: list . 
    :type first_character: Can be any type.
    :type second_character: Can be any type.
    :type third_character: Can be any type.
    :type the_new_list: Can be any type.
    :return: Returns a new list - arranged in the order explained at the beginning of the documentation.
    :rtype: list. 
    """
    first_character = my_list[0]
    second_character = my_list[1]
    third_character = my_list[2]
    the_new_list = [second_character, third_character , first_character]
    print(the_new_list)
   # return the_new_list

def main():
    shift_left([0, 1, 2])
    shift_left(['monkey', 2.0, 1])
if __name__ == "__main__":
    main() 

print()
help(shift_left)
print()