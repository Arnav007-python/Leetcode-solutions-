class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Handle base cases
        # Negative numbers (e.g., -121) and numbers ending in 0 (e.g., 10) 
        # cannot be palindromes (except the number 0 itself).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        original = x
        
        # Step 2: Mathematically reverse the integer
        while x > 0:
            last_digit = x % 10  # Gets the last digit (e.g., 121 % 10 = 1)
            reversed_num = (reversed_num * 10) + last_digit  # Shifts left and adds digit
            x //= 10  # Removes the last digit using floor division (e.g., 121 // 10 = 12)
            
        # Step 3: Check if the reversed number matches the original
        return original == reversed_num
    

        return original == reversedNum;
    
