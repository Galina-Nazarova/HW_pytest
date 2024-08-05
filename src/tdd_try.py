def calc_avg(my_list):
    if len(my_list) > 0:
        return sum(my_list) / len(my_list)
    return 0

if __name__ == "__main__":
    assert calc_avg([1, 2, 3, 4]) == 2.5

    assert calc_avg([]) == 0

    assert calc_avg([]) == 0