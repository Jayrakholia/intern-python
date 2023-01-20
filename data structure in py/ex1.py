l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
ans= list()

odd_elements = l1[1::2]
print("element at odd-index from list1")
print(odd_elements)

even_elements = l2[0::2]
print("element at even-index from list2")
print(even_elements)

print("final list")
ans.extend(odd_elements)
ans.extend(even_elements)
print(ans)
