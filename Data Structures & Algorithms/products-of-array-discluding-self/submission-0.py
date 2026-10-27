class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        op = [1]*n
        # print(op)
        pre = 1
        for i in range(n):
            op[i] = pre
            pre *= nums[i]
            # print(op)
        suff = 1

        for i in range(n - 1, -1, -1):
            op[i] *= suff
            suff *= nums[i]
            # print(op)

        return op


    # Pattern to remember => prefix pass → store left product → suffix pass → multiply right product.