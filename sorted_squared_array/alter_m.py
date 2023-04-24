def sortedSquaredArray(array):
    squared_array = [0] * len(array)
    squared_array[0] = min(array)**2
    squared_array[-1] = max(array)**2
    for indx, i in enumerate(array):
        if i**2 > min(squared_array) & i**2 < max(squared_array):
            squared_array[indx] = i**2
    squared_array.sort()
    return squared_array

array = [1, 2, 3, 5, 6, 8, 9]
result = sortedSquaredArray(array)
print(result)



