class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        indices = [0] * (max(nums) + 1)
        neg_indices = [0] * (-1 * (min(nums) - 1))
        print(neg_indices)

        for n in nums:
            if n >= 0:
                if indices[n] > 0:
                    return True
                indices[n] += 1
            else:
                if neg_indices[-1 * n] > 0:
                    return True
                neg_indices[-1 * n] += 1
        
        return False