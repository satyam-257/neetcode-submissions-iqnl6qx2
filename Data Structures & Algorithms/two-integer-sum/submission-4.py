class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = []
        for i in range(len(nums)):
            indexed_nums.append([nums[i], i])
            
        
        indexed_nums.sort()
        
        
        i, j = 0, len(nums) - 1
        
        while i < j:
            current_sum = indexed_nums[i][0] + indexed_nums[j][0]
            
            if current_sum == target:
                
                return sorted([indexed_nums[i][1], indexed_nums[j][1]])
            elif current_sum < target:
                i += 1
            else:
                j -= 1