class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        unseen = {}
        for i , num in enumerate(nums):
            comp = target-num
            if comp in unseen:
                return [unseen[comp],i]
            unseen[num] = i
        
        return []
        
