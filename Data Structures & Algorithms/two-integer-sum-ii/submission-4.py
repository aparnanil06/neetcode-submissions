class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            needed = target - numbers[i]
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == needed:
                    return [i + 1, mid + 1]
                elif numbers[mid] < needed:
                    l = mid + 1
                else:
                    r = mid - 1
        return []