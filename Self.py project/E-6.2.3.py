print()

def format_list(my_list):
    """The function takes the organs in the even places, and the last organ in the list, and edits them nicely.
    :param my_list: Receives the list from the user.
    :variable the_first_part_of_the_list: Cut from the original list the organs in the even places.
    :variable the_second_part_of_the_list: Cuts from the original list the last organ in the list.
    :variable new_list: Adds a comma and space to the new list, by the method join. 
    :type my_list: list. 
    :return: The function returns a string that contains the list members in the even positions, separated by a comma and a space, as well as the last member with the caption and in front of it.
    :rtype: list. 
    """
    the_first_part_of_the_list = my_list[::2]
    the_second_part_of_the_list = my_list[-1]
    new_list = ", ".join(the_first_part_of_the_list)
    print(new_list + ", and",the_second_part_of_the_list)


def main():
    format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"])
    format_list(["nerya", "tamar", "avia", "yoyo", "joli"," jacob", "jodit", "theila"])

if __name__ == "__main__":
    main()    

print()

help(format_list)
