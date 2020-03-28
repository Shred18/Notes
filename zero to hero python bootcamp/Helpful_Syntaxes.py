#This is the sytax for asking for an input, and if the input
#is incorrect, you will return a statement saying so (using try/except)

def ask_for_int():

    while True:
        try:
            #this is trying the input
            result = int(input("Please provide a number:  "))
        except:
            #if the input is incorrect, it defaults to the
            #except portion
            print("Whoops! That is not a number")
            continue
        else:
            #if the input is correct, it moves to the else portion
            print("Yes, thank you")
            break
        
