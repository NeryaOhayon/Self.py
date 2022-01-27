print()


def sequence_del(my_str):
    """The function takes a string and deletes the letters that appear in sequence. That is, the function returns a string in which only one character appears from each sequence of identical characters in the input string.
    :param my_str: Receives from the user a string to decrypt.
    :variable bar: The final string is stored in it.
    :type my_str: "str". 
    :type bar: "str". 
    :return: The function returns a string without repeating the same signal several times in succession.
    :rtype: "str". 
    """

    bar = ''
    for chr in my_str:
        if bar == '' or chr != bar[len(bar)-1]:
            bar += chr
    return bar



def main():
    print()
    print(sequence_del("Heeyyy   yyouuuu!!!"))
    print()
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print()
    print(sequence_del("SSSSsssshhhh"))
    print()

if __name__ == "__main__":
    main()
    
help(sequence_del)

