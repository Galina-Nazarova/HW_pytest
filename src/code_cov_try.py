

def finder(my_list, my_type):
    counter = 0
    if isinstance(my_list, list):
        for item in my_list:
            if isinstance(item, my_type):
                counter += 1
        return counter