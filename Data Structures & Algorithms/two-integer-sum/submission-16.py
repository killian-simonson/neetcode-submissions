class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        for i, n in enumerate(nums):
            if n not in ind:
                ind[n] = [i]
            else:
                ind[n].append(i)
        
        print(ind)

        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in ind.keys():
                if i in ind[diff] and len(ind[diff]) == 2:
                    return ind[diff]
                elif i not in ind[diff]:
                    return [i, ind[diff][0]]
