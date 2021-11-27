# E-5.3.4

print("hello, today I am creating a function")

def last_early(my_str):
    my_str = my_str.lower()
    The_last_character = my_str[-1:]
    true_or_false = my_str.count(The_last_character) > 1
    return true_or_false
   
    #print(my_str.count(The_last_character) > 1) instand of "return"


