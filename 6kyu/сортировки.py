

def buble_sort(input_list):
    for j in range(len(input_list) - 1):
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
    return input_list


def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    elem = input_list[0]
    left = [i for i in input_list if i < elem]
    center = [i for i in input_list if i == elem]
    right = [i for i in input_list if i > elem]
    return quick_sort(left)+center+quick_sort(right)




