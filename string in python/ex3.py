def mixstr(s1,s2):
    first_char=s1[0]+s2[0]

    middle_char=s1[int(len(s1)/2):int(len(s1)/2)+1]+s2[int(len(s2)/2):int(len(s2)/2)+1]

    last_char=s1[len(s1)-1]+s2[len(s2)-1]

    ans= first_char+middle_char+last_char
    print("mix string: ",ans)

s1 = "America"
s2 = "Japan"
mixstr(s1, s2)