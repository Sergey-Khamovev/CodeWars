a = [1,2,6,4,14,21,112,0,3,3]
def buble_sort(list):
    count = 0
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                count += 1
    return list, count
b = buble_sort(a)
print(b)

def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    elem = input_list[0]
    left = [i for i in input_list if i < elem]
    center = [i for i in input_list if i == elem]
    right = [i for i in input_list if i > elem]
    return quick_sort(left)+center+quick_sort(right)


print(quick_sort([3,0,2,5,4]))

