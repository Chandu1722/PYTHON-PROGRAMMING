def duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

nums = [1, 2, 3, 4, 2]
print(duplicates(nums))  # Output: True
