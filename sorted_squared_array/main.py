def sortedSquaredArray(array):
    squared_array = [num * num for num in array]
    squared_array.sort()
    return squared_array


def main():
    array = [1, 2, 3, 5, 6, 8, 9]
    result = sortedSquaredArray(array)
    print(result)


if __name__ == "__main__":
    main()
