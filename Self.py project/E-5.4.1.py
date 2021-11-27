print()

def func(num1, num2):
    """Calculates the division between num1 and num2.
    :param num1: The divider.
    :param num2: Divided.
    :type num1: int.
    :type num2: int.
    :return: The result of dividing num1 in num2.
    rtype: float.
   """
    #division = num1 / num2
    #return division
    print("the result is:", num1 / num2)


def main():
    # Call the function func
    func(35, 5)
    func(255, 55)
if __name__ == "__main__":
    main() 

print()  

help(func)

print()