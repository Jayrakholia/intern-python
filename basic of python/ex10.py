def merge_list(list1,list2):
    final_list=[]

    for num in list1:
        if num%2 != 0:
            final_list.append(num)

    for num in list2:
        if num%2 == 0:
            final_list.append(num)
    return final_list

list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]

print("final list:",merge_list(list1,list2))