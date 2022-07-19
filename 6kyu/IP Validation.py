def is_valid_IP(strng):
    arr_list = strng.split(".")
    try:
        for each in arr_list:
            if (each[0] == "0" and len(each) > 1) or not each.isdigit() or int(each) not in range(0, 256):
                return False
    except Exception:
        return False
    return False if len(arr_list) != 4 else True





