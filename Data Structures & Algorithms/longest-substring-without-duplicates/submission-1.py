class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window: adds letters incrementally, if the count for a letter becomes greater than one, increments from the left and subtract from count until count for that letter is 0
        count = {}
        l, res = 0, 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1) #calculates length from the point where the duplication stops to the current value
        return res

