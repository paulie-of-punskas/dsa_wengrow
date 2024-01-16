# === implement bubble sort
# === examples:
# 2135
# 1235

# ===
# 42713
# - first run:
# 24713
# 24173
# 24137 (7 becomes a bubble)
# - second run:
# 24137
# 21437
# 21347 (4 become a bubble)
# - third run:
# 21347
# 12347 (3 becomes a bubble)
# - fourth run:
# 12347

def bubble_sort(input_array:list):
    """
    implementation of bubble sort, on a list
    """
    print("")
    sorted_array = input_array
    print(f">> number of iterations: ", str(len(sorted_array) - 1))
    print(f">> input array: {sorted_array}")

    # loop through input list
    for q in range(len(sorted_array) - 1):
        # loop through all elements
        for j in range(len(sorted_array) - 1):
            print(f">> iteration: {j} checking: {sorted_array[j]}, {sorted_array[j + 1]}")
            if sorted_array[j] > sorted_array[j + 1]:
                temp = sorted_array[j] 
                sorted_array[j] = sorted_array[j + 1]
                sorted_array[j + 1] = temp
                print(f">>>> reordered to {sorted_array}")
    return sorted_array

print(bubble_sort([2, 1, 3, 5]))
print(bubble_sort([4, 2, 10, 7, 1, 3]))

