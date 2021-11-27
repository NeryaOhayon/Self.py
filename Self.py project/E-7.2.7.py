
print()

# לבדוק מה אגם אומרת על זה, גם על גודל החץ כי זה משתנה רק על ידי מה שהמשתמש עצמו שם בפונקציה ולא אני שולט על זה, וגם לגבי הריטרנ

def arrow(my_char, max_length):
    for i in range(max_length * 2):
        if i <= max_length:
            print(my_char * i)

        else:
          print(my_char * (max_length * 2 - i))
       
    

arrow("*", 5)