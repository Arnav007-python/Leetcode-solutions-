from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        answer = []
        
        # Calculate the length of the first half of the palindrome
        half_length = (intLength + 1) // 2
        
        # The smallest number of length `half_length`
        start = 10**(half_length - 1)
        
        # The total number of valid palindromes of length `intLength`
        max_palindromes = 9 * start
        
        for q in queries:
            if q > max_palindromes:
                answer.append(-1)
            else:
                # Calculate the first half for the q-th palindrome
                half_str = str(start + q - 1)
                
                # Construct the full palindrome string
                if intLength % 2 == 1:
                    # Odd length: reverse all but the last character of the half
                    palindrome_str = half_str + half_str[-2::-1]
                else:
                    # Even length: reverse the entire half
                    palindrome_str = half_str + half_str[::-1]
                
                answer.append(int(palindrome_str))
                
        return answer
