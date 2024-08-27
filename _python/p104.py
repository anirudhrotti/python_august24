sorted_list = list(range(1, 1000000001))

def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1

a = 1000000000
index = linear_search(sorted_list, a)

if index != -1:
    print(f"Element {a} found at index {index}.")
else:
    print(f"Element {a} not found in the list.")
