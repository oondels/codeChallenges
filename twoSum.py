lista = [14,7,5,2]

# Primeira Solução
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(0, len(nums)):
        j=i+1
        for j in range(0, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Segunda Solução com HashMap
def twoSum_2(nums: list[int], target: int) -> list[int]:
    matches = {}
    for idx, num in enumerate(nums):
        match = target - num
        if match in matches:
            print(matches)
            return [matches.get(match), idx]
        else:
            matches[num] = idx

# Terceira Solução
def twoSum_3(nums: list[int], target: int) -> list[int]:
    nums.sort()

    for idx, num in enumerate(nums):
        right = len(nums) - 1
        if nums[idx] + nums[right] == target:
            return [idx, right]
        else:
            if nums[right] > target:
                right -= 1

print(twoSum_3(lista, 9))