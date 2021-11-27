
print()

def seven_boom(end_number):

    list = []
    
    for item in range(end_number + 1):
        
        if (("7" in str(item)) or (item % 7 == 0)):
            list += ["BOOM"]

        else:
            list += [item]
    
    return list


def main():
    print()
    print(seven_boom(17))
    print()
    print(seven_boom(21))
    print()

if __name__ == "__main__":
    main()

