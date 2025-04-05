from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}

        for i in range(0,len(nums)):
            remaining = target - nums[i];
            if(remaining in dict):
                index = dict.get(remaining)
                return [index,i]
            else:
                dict[nums[i]]=i

        return [-1,-1]            

sol = Solution()
print(sol.twoSum([2,7,11,15],9))

