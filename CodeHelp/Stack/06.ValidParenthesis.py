'''
https://www.codingninjas.com/codestudio/problems/valid-parenthesis_795104?leftPanelTab=1
'''
'''
   	Time Complexity : O(N)
	Space Complexity : O(N)

	Where N is the length of the string.
'''

def isValidParenthesis(expression):
    s = []

    # Traversing the Expression.
    for i in range(len(expression)):
        if (expression[i] == '(' or expression[i] == '[' or expression[i] == '{'):
            # Push the element in the stack.
            s.append(expression[i])
            continue

        '''
            If current current character is not opening
            bracket, then it must be closing. So stack
            cannot be empty at this point.
        '''

        if len(s) == 0:
            return False

        # Store the top element.
        x = s.pop()

        # Check for opening braces in stack of corresponding closing braces.
        if expression[i] == ')':
            if (x == '{' or x == '['):
                return False

        elif expression[i] == '}':
            if (x == '(' or x == '['):
                return False

        elif expression[i] == ']':
            if (x == '(' or x == '{'):
                return False

    # Check Empty Stack.
    return len(s) == 0


# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")
