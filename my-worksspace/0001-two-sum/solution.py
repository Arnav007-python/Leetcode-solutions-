class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store the number and its corresponding index
        num_to_index = {}
        
        for i, num in enumerate(nums):
            # Calculate what number we need to reach the target
            complement = target - num
            
            # If the complement is already in our map, we found the pair!
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Otherwise, store the current number and its index in the map
            num_to_index[num] = i
            
        return [] # Return empty list if no solution is found (though constraints guarantee one)
