
##  This is what I initially thought to do, but it's a mistake!
#def filter_teens(a=13, b=13, c=13):
 #   if (13 <= a <= 14 or 17 <= a <= 19) or (13 <= b <= 14 or 17 <= b <= 19) or (13 <= c <= 14 or 17 <= c <= 19):
       
            
def filter_teens(a=13, b=13, c=13):
    sum = fix_age(a) + fix_age(b) + fix_age(c)
    return sum



def fix_age(age=0):
    if 13 <= age <= 14 or 17 <= age <= 19:
        age = 0
        return age
    else:
        return age

    

# Running examples:

filter_teens()

filter_teens(1, 2, 3)

filter_teens(2, 13, 1)

filter_teens(2, 1, 15)
