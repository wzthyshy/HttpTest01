'''
1.对比前一个与后一个数对比，如果前一个数大于后一个数，就交换，否则不变
'''
list1 = [45, 32, 8, 26, 12, 21]

# 普通对比,一个一个对比，比较麻烦
# if list1[0]>list1[1]:
#     temp=list1[0]
#     list1[0]=list1[1]
#     list1[1]=temp

for i in (range(len(list1) - 1)):
    for j in (range(len(list1) - 1)):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list1)
