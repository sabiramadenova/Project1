def recursive_search(item, lst, index=0):

    if index >= len(lst):
        return -1

    if lst[index] == item:
        return index

    return recursive_search(item, lst, index + 1)


my_list = [2, 5, 7, 8, 3]
item_to_find = 8
result_index = recursive_search(item_to_find, my_list)
if result_index != -1:
    print("item " + str(item_to_find) + " result: " + str(result_index))
else:
    print("not")
