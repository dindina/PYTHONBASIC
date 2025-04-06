from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bb = Counter(nums)
        for num in list(bb.values()):
            if num > 1:
                return True
        return False 