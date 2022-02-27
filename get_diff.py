list1 = ['121-001', '122-002']

list2 = ['121-001', '122-002', '122-003', '122-004']

list_difference = [item for item in list1 if item not in list2]

print(list_difference)