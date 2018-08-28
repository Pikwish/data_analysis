#-*- coding:utf8 -*-
#!/usr/bin/env python3


#第1题
list1 = ['a','b','c','d','e','f','g']
list2 = [1,2,3,4,5,6,7]
list3 = ['h','i','j','k','l','m','n']

new_list = list1 + list2 +list3

max_index = len(new_list)

for i in range(max_index):
    print(i,'->',new_list[i])



#第2题
list4 = ['SONY','Microsoft','Nintendo']
list5 = ['PS4','Xbox one','Switch']
my_dict = {}

for x in range(len(list5)):
    my_dict[list4[x]] = list5[x]

print(my_dict)


#第3题
list6 = [[1,2,3],[4,5,6],[7,8,9]]
for i in list6:
    result = ''
    max_index = len(i)
    for x in range(len(i)):
        if x < (max_index-1):
            result += '{},'.format(i[x])
        else:
            result += '{}\n'.format(i[x])

print(result)