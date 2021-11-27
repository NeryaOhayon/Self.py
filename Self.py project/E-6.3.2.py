
def longest(my_list):
    """The function receives a list consisting of strings and returns the longest string.
    :param my_list: Receives a list from the user.
    :variable the_sorted_list: Sort the list from the entry with the smallest number of characters to the entry with the largest number of characters.
    :variable the_longest_str: Displays the value with the largest number of characters in the list.
    :type my_list: "list". 
    :type the_sorted_list: "list". 
    :type the_longest_str: "str".
    :return: The function returns the string with the largest number of characters in the list.
    :rtype: "str". 
    """
    the_sorted_list = sorted(my_list, key=len)
    the_longest_str = the_sorted_list[-1]
    print(the_longest_str)

def main():
     list1 = ["111", "234", "2000", "goru", "birthday", "09"]
     longest(list1)

if __name__ == "__main__":
    main()

    print()
    help(longest)
    print()