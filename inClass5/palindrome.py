def palin ():
    msg = "Please enter a string: "
    str1 = input(msg)
    str2 = str1[::-1]

    if not str1.isalpha():
        return -1

    if str1 == str2:
        # print("String is a palindrome")
        return True
    else:
        # print("String is NOT a palindrome")
        return False