class Solution:
    def findMin(self, nums: List[int]) -> int:
        s=0
        e=len(nums)-1
        while(s<e):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return min(nums[0],nums[1])
            mid = s+(e-s)//2
            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid
        
        return nums[s]
