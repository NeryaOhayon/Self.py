
def extend_list_x(list_x, list_y):
    """ The function adds the list - list_y to the beginning of the second list - list_x.
  :param list_x: Gets the list from the user that will eventually contain at the beginning, the second list list_y.
  :param list_y: Gets a list from the user, which will eventually be added to the beginning of the list - list_x.
  :type list_x: list. 
  :type list_y: list.
  :return: The function returns the list - list_x, which initially contains the second list - list_y.
  :rtype: list.
    """
    list_x[:0] = list_y
    print(list_x)

def main():
    x = [4, 5, 6]
    y = [1, 2, 3]
    extend_list_x(x, y)  

if __name__ == "__main__":
    main() 

print()

help(extend_list_x)