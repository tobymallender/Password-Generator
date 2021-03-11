
result = ""
message = ""
choice = ""
option = 0

import string
from random import *
characters = string.ascii_letters+string.digits
characters2 = "1234567890"
symbol = "!*#_-"

def print_menu():
    print(" ____ ____ ____ ____ ____ ____ ____ ____")
    print("||P |||a |||s |||s |||w |||o |||r |||d ||")
    print("||__|||__|||__|||__|||__|||__|||__|||__||     ")
    print("|____|____|____|____|____|____|____|____|____")
    print("||G |||e |||n |||e |||r |||a |||t |||o |||r ||")
    print("||__|||__|||__|||__|||__|||__|||__|||__|||__||")
    print("|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|")
    print("    ")
    
      

          
print("  1  -  random 3 digits + input + random 3 digits")
print("  2  -  random 3 digits + level 1 encrypted input + random 4 digits")
print("  3  -  random 4 digits + level 2 encrypted input + random 5 digits")
print("  4  -  QUIT PROGRAM")

loop=True




while loop:
    print_menu()
    option=input("Select an option for the program: ")
    

    if option =="1":
        name = input ("choose a word for your secure password: ")
        password = "".join(choice(characters) for x in range(randint(3,3)))
        password2 = "".join(choice(characters2) for x in range(randint(3,3)))
        restart = input("your secure password is: "+(password+(name)+password2)
                        +" - press enter to continue")
        password3 = "".join(choice(characters2) for x in range(randint(3,3)))
        password4 = "".join(choice(characters) for x in range(randint(3,3)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print (password3+(name)+password4)
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password5 = "".join(choice(characters) for x in range(randint(3,3)))
        password6 = "".join(choice(characters) for x in range(randint(3,3)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print (password5+(name)+password6)
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password7 = "".join(choice(characters) for x in range(randint(3,3)))
        password8 = "".join(choice(characters) for x in range(randint(3,3)))

        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password7+(name)+password8) + " - SYSTEM TERMINATED - END")
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password49 = "".join(choice(characters) for x in range(randint(3,3)))
        password50 = "".join(choice(characters) for x in range(randint(3,3)))

        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password49+(name)+password50) + " - SYSTEM TERMINATED - END")
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password51 = "".join(choice(characters) for x in range(randint(3,3)))
        password52 = "".join(choice(characters) for x in range(randint(3,3)))

        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password51+(name)+password52) + " - SYSTEM TERMINATED - END")
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password53 = "".join(choice(characters) for x in range(randint(3,3)))
        password54 = "".join(choice(characters) for x in range(randint(3,3)))

        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password53+(name)+password54) + " - SYSTEM TERMINATED - END")
        else:
            print("SYSTEM TERMINATED - END")
            exit()
    
    elif option=="2":
        name = input ("choose a word for your secure password: ")
        password9 = "".join(choice(characters) for x in range(randint(3,3)))
        password10 = "".join(choice(characters2) for x in range(randint(4,4)))
        restart = input("your secure password is: "+(password9+(name[0:2].upper()+name[2:999].lower())+password10)+" - press enter to continue")
        password11 = "".join(choice(characters2) for x in range(randint(3,3)))
        password12 = "".join(choice(characters) for x in range(randint(4,4)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print (password11+(name[0:2].upper()+name[2:999].lower())+password12)
        else:
            print("SYSTEM TERMINATED - END")
            exit()


        password13 = "".join(choice(characters) for x in range(randint(3,3)))
        password14 = "".join(choice(characters) for x in range(randint(4,4)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print (password13+(name[0:2].upper()+name[2:999].lower())+password14)
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password15 = "".join(choice(characters) for x in range(randint(3,3)))
        password16= "".join(choice(characters) for x in range(randint(4,4)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password15+(name[0:2].upper()+name[2:999].lower())+password16) + " - SYSTEM TERMINATED - END")
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password40 = "".join(choice(characters) for x in range(randint(4,4)))
        password41 = "".join(choice(characters) for x in range(randint(5,5)))
        password42 = "".join(choice(symbol) for x in range(1,1))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password40+(name[0:2].upper()+name[2:999].lower())+password41+password42))
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password43 = "".join(choice(characters) for x in range(randint(4,4)))
        password44 = "".join(choice(characters) for x in range(randint(5,5)))
        password45 = "".join(choice(symbol) for x in range(1,1))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password43+(name[0:2].upper()+name[2:999].lower())+password44+password45))
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password46 = "".join(choice(characters) for x in range(randint(4,4)))
        password47 = "".join(choice(characters) for x in range(randint(5,5)))
        password48 = "".join(choice(symbol) for x in range(1,1))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password46+(name[0:2].upper()+name[2:999].lower())+password47+password48))
        else:
            print("SYSTEM TERMINATED - END")
            exit()




    elif option=="3":
        name = input ("choose a word for your secure password: ")
        password17 = "".join(choice(characters) for x in range(randint(4,4)))
        password18 = "".join(choice(characters2) for x in range(randint(5,5)))
        password25="".join(choice(symbol) for x in range(randint(1,1)))
        password26 = "".join(choice(symbol) for x in range(1,1))
        restart = input("your secure password is: "+(password17+(name[0:2].upper()+name[2:4].lower()+name[4:5].upper()+name[5:999].lower())+password25+password26+password18)
                        + " - press enter to continue")
        password19 = "".join(choice(characters2) for x in range(randint(4,4)))
        password20 = "".join(choice(characters) for x in range(randint(5,5)))
        password27 = "".join(choice(symbol) for x in range(randint(1,1)))
        

        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password19+(name[0:2].upper()+name[2:999].lower())+password20+password27))
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password21 = "".join(choice(characters) for x in range(randint(4,4)))
        password22 = "".join(choice(characters) for x in range(randint(5,5)))
        password29 = "".join(choice(symbol) for x in range(randint(1,1)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print (
                (password21+(name[0:2].upper()+name[2:999].lower())+password29+password22))
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password31 = "".join(choice(characters) for x in range(randint(4,4)))
        password32 = "".join(choice(characters) for x in range(randint(5,5)))
        password33 = "".join(choice(symbol) for x in range(randint(1,1)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print (
                (password31+(name[0:2].upper()+name[2:999].lower())+password32+password33))
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password34 = "".join(choice(characters) for x in range(randint(4,4)))
        password35 = "".join(choice(characters) for x in range(randint(5,5)))
        password36 = "".join(choice(symbol) for x in range(randint(1,1)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print (
                (password36+(name[0:2].upper()+name[2:999].lower())+password35+password34))
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password37 = "".join(choice(characters) for x in range(randint(4,4)))
        password38 = "".join(choice(characters) for x in range(randint(5,5)))
        password39 = "".join(choice(symbol) for x in range(randint(1,1)))
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print (
                (password37+(name[0:2].upper()+name[2:999].lower())+password38+password39))
        else:
            print("SYSTEM TERMINATED - END")
            exit()

        password23 = "".join(choice(characters) for x in range(randint(4,4)))
        password24 = "".join(choice(characters) for x in range(randint(5,5)))
        password30 = "".join(choice(symbol) for x in range(randint(1,1)))
        
        more = input ("would you like another secure password? ")
        if more == 'yes' or more == 'y' or more == 'Yes' or more == 'Y':
            print ((password23+(name[0:2].upper()+name[2:999].lower())+password24+password30))
            print ("SYSTEM TERMINATED - END")
        else:
            print("SYSTEM TERMINATED - END")
            exit()


    exit()
    
    
       
                   
        #Randomise order of encryption (Symbols)




            
