def Check_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

users_input = input("Enter the numbers separated by space : ")
nums = list(map(int, users_input.split()))
result = Check_duplicates(nums)

print(result)
