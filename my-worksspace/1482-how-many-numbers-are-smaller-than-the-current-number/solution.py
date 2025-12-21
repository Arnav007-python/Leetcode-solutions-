class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. Create a sorted version of the array
        sorted_nums = sorted(nums)
        
        # 2. Map each number to its first index in the sorted array
        smaller_count_map = {}
        for i, num in enumerate(sorted_nums):
            # Only record the first time we see the number
            if num not in smaller_count_map:
                smaller_count_map[num] = i
        
        # 3. Use the map to build the result array
        return [smaller_count_map[num] for num in nums]
        
