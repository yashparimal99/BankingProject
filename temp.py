import random



def card():
    start = "2030400"
    rem = ''.join(str(random.randint(0,9)) for _ in range(9))
    return start + rem

    

cobj=card()
print("CARD", cobj)

       
