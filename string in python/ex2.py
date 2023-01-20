def append_middle(s1,s2):
    print("original string: ",s1,s2)

    mi = int(len(s1)/2)
    x=s1[:mi:]
    x=x+s2
    x=x+s1[mi:]
    print("after append: ",x)

append_middle("Ault","Kelly")