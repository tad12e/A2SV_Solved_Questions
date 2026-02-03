class Solution:
    def isPalindrome(self, x: int) -> bool:

    
        # A negative number is not a palindrome
        if x < 0:
            return False
        
        # Initialize a variable to store the reversed number
        reversed_num = 0
        original_num = x
        
        while x != 0:
            # Get the last digit and add it to the reversed number
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            # Remove the last digit from x
            x //= 10
        
        # Check if the original number and the reversed number are the same
        return original_num == reversed_num
