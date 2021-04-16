def password(x):
    import random
    i = x
    while i > 0:
        print (chr(random.randint(0,127)))
        i -= 1

password(10)