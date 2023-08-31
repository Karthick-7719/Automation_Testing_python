def Max_Element(lists):
    max = lists[0]
    for element in lists:
        if element > max:
            max = element
        return max
lists = [70,19,53,60,66]
print("Largest element of the list is : ", Max_Element(lists))