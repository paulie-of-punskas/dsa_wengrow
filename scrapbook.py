# input_array = [2, 1, 3, 5]
# for element in range(len(input_array) - 1):
#     print(f"{input_array[element]}, {input_array[element+1]}")

# j = 0
# n = len(input_array) - 1
# while j < n:
#     print(f">> j: {j}, {input_array[j]}, {input_array[j+1]}")
#     j += 1

sorted_array = [4, 2, 7, 1, 3]
# loop through whole array once
for q in range(len(sorted_array) - 1):
    for j in range(len(sorted_array) - 1):
        print(f">> iteration: {j} checking: {sorted_array[j]}, {sorted_array[j + 1]}")
        if sorted_array[j] > sorted_array[j + 1]:
            temp = sorted_array[j] 
            sorted_array[j] = sorted_array[j + 1]
            sorted_array[j + 1] = temp
            print(f">>>> reordered to {sorted_array}")