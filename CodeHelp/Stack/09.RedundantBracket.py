'''
https://www.codingninjas.com/codestudio/problems/redundant-brackets_975473?leftPanelTab=1
'''
'''
    Time Complexity: O(|S|)
    Space Complexity: O(|S|)

    Where '|S|' is the length of the given string.
'''

from collections import deque

def findRedundantBrackets(s):
    
    # For keeping track of opening and closing brackets.
    brackets = deque()
    
    n = len(s)
    
    # Iterate through the string.
    for i in range(n):
        
        # Push the current character to the stack if it is an operator or an opening bracket.
        if s[i] == '(' or s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
            
            brackets.append(s[i])
            
        # If the current character is a closing bracket.
        elif s[i] == ')':
            # For checking if the current bracket is redundant or not.
            isRedundant = True
            
            # Keep popping from the stack till we reach an opening bracket.
            while brackets[-1] != '(':
                
                # If we find a operator then the current bracket is not redundant.
                if brackets[-1] == '+' or brackets[-1] == '-' or brackets[-1] == '*' or brackets[-1] == '/':
                    
                    isRedundant = False
                    
                brackets.pop()
            
            brackets.pop();
            # Return true if we did not find any operator before finding the opening bracket.
            if isRedundant == True:
                
                return True
                
    # If no bracket is redundant then return false.
    return False