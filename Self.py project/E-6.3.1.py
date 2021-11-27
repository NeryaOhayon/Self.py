
def are_lists_equal(list1, list2):
    """The function receives two lists containing values from the int and float types only, and checks whether all the values contained in the content are the same.
    :param list1: Receives the first list from the user.
    :param list2: Receives the second list from the user.
    :variable list1_sorted: sorted list1. 
    :variable list2_sorted: sorted list2.
    :variable True_or_False: Compares the lists and checks whether true or false. 
    :type list1: list. 
    :type list2: list. 
    :type list1_sorted: list. 
    :type list2_sorted: list. 
    :type True_or_False: bool. 
    :return: The function returns true if the two lists contain exactly the same members (even if in a different order), otherwise, the function returns a lie.
    :rtype: bool. 
    """
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    True_or_False = list1_sorted == list2_sorted
    print(True_or_False)

def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]

    print()
    are_lists_equal(list1, list2)
    print()
    are_lists_equal(list1, list3)
    print()

if __name__ == "__main__":
    main()

print()
help(are_lists_equal)
print()
