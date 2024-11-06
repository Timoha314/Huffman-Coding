def huffman(arr):
    n = len(arr)
    arr_pointer = 0
    sums_pointer = 0
    sums = []
    total_cost = 0
    for i in range(n - 1):
        if arr_pointer < n and (sums_pointer >= len(sums) or arr[arr_pointer] <= sums[sums_pointer]):
            min1 = arr[arr_pointer]
            arr_pointer += 1
        else:
            min1 = sums[sums_pointer]
            sums_pointer += 1

        if arr_pointer < n and (sums_pointer >= len(sums) or arr[arr_pointer] <= sums[sums_pointer]):
            min2 = arr[arr_pointer]
            arr_pointer += 1
        else:
            min2 = sums[sums_pointer]
            sums_pointer += 1

        combined = min1 + min2
        total_cost += combined
        sums.append(combined)

    return total_cost


with open('input.txt', 'r') as file:
   n = int(file.readline())
   arr = list(map(int, file.readline().split()))
with open('output.txt', 'w') as output_file:
    output_file.write(str(huffman(arr)))
