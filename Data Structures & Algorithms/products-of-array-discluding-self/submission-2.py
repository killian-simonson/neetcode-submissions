class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suff = [1] * len(nums)
        for num in nums:
            pre.append(num * (pre[-1] if pre else 1))
        
        current_suff = 1
        for i in range(len(nums) - 1, -1, -1):
            current_suff *= nums[i]
            suff[i] = current_suff

        return [(pre[x - 1] if x > 0 else 1) * (suff[x + 1] if x < len(nums) - 1 else 1) for x in range(len(nums))]