arr = [3, 6, 1, 5, 2, 4]

for j in range(len(arr)):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i = i - 1
    arr[i + 1] = key

print(arr)
