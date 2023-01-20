def palindrome(num):
    print("number ",num)
    number = num

    rev_num = 0
    while num > 0:
        dig = num % 10
        rev_num = (rev_num*10) + dig
        num = num // 10

    if number == rev_num:
        print("Yes.given number is palindrome number")
    else:
        print("No.given number is palindrome number")

palindrome(121)

palindrome(345)