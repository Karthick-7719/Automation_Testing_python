def filt_numbers(numbers):
    new_list = [num for num in numbers if num > 10]
    return new_list
num_list = [5,12,8,20,3,15,7,18]
filtrd_list = filt_numbers(num_list)
print("Numbers greater than 10 is : ", filtrd_list)