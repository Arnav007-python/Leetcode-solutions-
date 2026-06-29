from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        target_idx = 0
        
        # Iterate through the stream of integers from 1 to n
        for current_num in range(1, n + 1):
            # If we've already built the target array, stop the operations
            if target_idx == len(target):
                break
            
            # If the current number is in the target, push it and move to the next target
            if current_num == target[target_idx]:
                operations.append("Push")
                target_idx += 1
            # If the current number is not in the target, push it and immediately pop it
            else:
                operations.append("Push")
                operations.append("Pop")
                
        return operations
