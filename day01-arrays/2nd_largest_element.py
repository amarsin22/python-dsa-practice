arr = [3,6,4,6,8,2,4,8,10,2]
largest = max(arr)
filtered_arr = [x for x in arr if x!= largest]
second_largest = max(filtered_arr)
print(second_largest)