class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        array = [0]*256
        for ch in s:
            array[ord(ch)] += 1

        for ch  in t:
            array[ord(ch)] -= 1
        for i in range(0,len(array)):
            if array[i] != 0:
                return False
        return True
    
solution = Solution()
print(solution.isAnagram("anagram","nagaram"))
