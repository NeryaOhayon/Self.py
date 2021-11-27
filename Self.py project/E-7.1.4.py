
def squared_numbers(start, stop):
    """  The function gets two integers, start and stop. The function returns a list containing all the number squares between start and stop (inclusive).
    :param start: The number from which to start calculating the squares of numbers.
    :param stop: The number to which the number squares are calculated.
    :type start: "int". 
    :type stop: "int". 
    :return: The function returns a list containing all the number squares between start and stop (inclusive).
    :rtype: "list". 
    """
    list = []
    while start <= stop:
        the_pow = pow(start, 2)
        list = list + [the_pow]
        start += 1
    return list
    
def main():
    print()
    print(squared_numbers(4, 8))
    print()
    print(squared_numbers(-3, 3))
    print()
    

if __name__ == "__main__":
    main()    

print()

help(squared_numbers)

print()
