def palin ():
    msg = "Please enter a string: "
    str1 = input(msg)

    # str3 = "apples are fun to eat"
    # str1 = str(str3)

    # str1 = ""
    # str3 = "redivider"
    # str1 = str(str3)

    str2 = str1[::-1]

    if str1 == "":
        return ""

    if not str2.isalpha():
        return -1

    if str1 == str2:
        # print("String is a palindrome")
        return True
    else:
        # print("String is NOT a palindrome")
        return False