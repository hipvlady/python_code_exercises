"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1,3,4]  form a subsequence of the array
  [1, 2, 3, 4] , and so do the numbers [2, 4]. Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence =  = [1, 6, -1, 10]

    Output True
"""


def is_subsequence(array, subsequence):
    array_idx = 0
    subsequence_idx = 0

    while array_idx < len(array) and subsequence_idx < len(subsequence):
        if array[array_idx] == subsequence[subsequence_idx]:
            subsequence_idx += 1
        array_idx += 1

    return subsequence_idx == len(subsequence)


def main():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    subsequence = [1, 6, -1, 10]

    result = is_subsequence(array, subsequence)
    print(result)


if __name__ == "__main__":
    main()