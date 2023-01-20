str1='james'
print("original string: ",str1)

ans= str1[0]
l=len(str1)
mi=int(l/2)
ans=ans+str1[mi]
ans=ans+str1[l-1]
print("new string: ",ans)
