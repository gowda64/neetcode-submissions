class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup_s=defaultdict(int)
        lookup_t=defaultdict(int)
        for char in s:
            lookup_s[char]+=1
        for char in t:
            lookup_t[char]+=1
        if lookup_s==lookup_t:
            return True
        else:
            return False