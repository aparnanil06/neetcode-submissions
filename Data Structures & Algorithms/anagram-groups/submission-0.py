class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i in strs:
            sortedI = ''.join(sorted(i))
            seen[sortedI].append(i)
        return list(seen.values())
        
         