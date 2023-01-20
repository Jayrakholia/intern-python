def middle(str1):
    print("original string: ",str1)

    mi=int(len(str1)/2)

    ans= str1[mi-1:mi+2]
    print("middle three char: ",ans)

middle("jhonDippeta")
middle("jaSonAy")