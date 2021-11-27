print()

#גם בקוד של אגם יש טעות, אין התייחסות לזה שהאותיות ברצף 
#לתקן שיהיה קשור לרצף של האותיות
#def sequence_del(my_str):
 #   lst = list(my_str)
  #  str = ""

   # for chr in lst:
        
    #    while lst.count(chr) > 1:
     #       lst.remove(chr)

    #for i in lst:
     #   str += i
    
    #return str 


#def main():
 #   print()
  #  print(sequence_del("pppyyyyyythhhhhooonnnnn"))
   # print()
    #print(sequence_del("Heeyyy   yyouuuu!!!"))
#if __name__ == "__main__":
 #   main()
    


#next_chr = lst.index(chr) + 1
#chr == lst[next_chr]:

#lst.count(chr) > 1















# לבדוק מה צריך להוסיף

#def sequence_del(my_str):
 #   my_str_list = list(my_str)
   
  #  for i in my_str_list:
   #     if my_str_list.count(i) > 1:
    #       my_str_list.remove(i)

     #   else:
      #      continue
           

    #return my_str_list


#print(sequence_del("pppyyyyyythhhhhooonnnnn"))
#print()





#def sequence_del(my_str):
 #   my_str_list = list(my_str)
  #  new_list = []
   # for i in my_str_list:
    #    if my_str_list.count(i) == 1:
     #       new_list += [i]
            

      #  elif (my_str_list.count(i) > 1) and (i in new_list == False):
       #     new_list += [i]
            

    #return new_list




# לבדוק איך לעקוף את זה שזה מחוץ לטווח

def sequence(my_str):
    my_str_list = list(my_str)
    
    
    for i in my_str_list:
        next_i = my_str_list.index(i) + 1

        while i == my_str_list[next_i]:
            my_str_list.remove(i)
            #my_str.translate({ord(i): None})

    return my_str_list

print(sequence("pppyyyyyythhhhhooonnnnn"))
print()