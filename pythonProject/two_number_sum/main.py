"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum.

  If any two numbers in the input array sum up to the target sum, the function
  should return them in an array, in any order.

  If no two numbers sum up to the target sum, the function should return
  an empty array.

  Example usage:
  array = [3, 5, -4, 8, 11, 1, -1, 6]
  targetSum = 10
  result = twoNumberSum(array, targetSum)
  print(result)  # output: [11, -1]
"""


def two_number_sum(array, target_sum_input):
    # create an empty dictionary to store the complement of each number in the array
    nums = {}

    # loop through each number in the array
    for num in array:
        # calculate the complement of the current number
        potential_match = target_sum_input - num
        # check if the complement is already in the dictionary
        if potential_match in nums:
            # if it is, return the two numbers in an array
            return [potential_match, num]
        # if it's not, add the current number to the dictionary
        nums[num] = True

    return []


if __name__ == '__main__':
    temp_array_input = []
    array = []
    user_input = input("Enter the array: ")
    array_input = user_input.split(",")

    for i in array_input:
        i = int(i)
        array.append(i)

    user_target_sum_input = input("Enter the target sum: ")
    target_sum_input = int(user_target_sum_input)
    num = two_number_sum(array, target_sum_input)
    print(num)
