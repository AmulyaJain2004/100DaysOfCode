def two_sum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

nums_input = input("Enter the numbers separated by spaces = ")
nums = list(map(int, nums_input.split()))

target = int(input("Enter the target value: "))
result = two_sum(nums, target)
print(result)
