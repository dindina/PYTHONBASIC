import heapq
from typing import List
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        charmap = Counter(nums)
        heap = []
        for num in charmap.keys():
            heapq.heappush(heap, (charmap[num],num))
            if (len(heap) > k):
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result    


    def bottomKFrequentElement(self,nums,k):
        charmap = Counter(nums)
        myheap = []
        for num in charmap.keys():
            heapq.heappush(myheap, (-nums[num],num))
            if(len(myheap) > k):
                heapq.heappop(myheap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(myheap)[1])
        return result                    
            



obj = Solution()
list11 = [1,2,2,3,3,3]
print(obj.topKFrequent(list11,2))
print(obj.bottomKFrequentElement(list11,2))

        
