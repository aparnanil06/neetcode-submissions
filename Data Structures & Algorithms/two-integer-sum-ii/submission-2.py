class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            needed = target - numbers[i]
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                if numbers[l] == needed:
                    return [i + 1, l + 1]
                else:
                    l += 1
        return []
