def sum_numbers(num):
    if num == 1:
        return 1

    result = sum_numbers(num - 1)
    return result + num


print(sum_numbers(666))
