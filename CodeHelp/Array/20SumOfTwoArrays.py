'''
https://www.codingninjas.com/codestudio/problems/sum-of-two-arrays_893186?leftPanelTab=2
'''
'''
		Time Complexity: O(max(N, M)))
		Space Complexity: O(1)
 
		Where N is the size of the first array and M is the size of the second array.
'''

def findArraySum(a, n, b, m):
    ans = list()
    carry = 0
    sum = 0
    i = n - 1
    j = m - 1
 
    while i >= 0 or j >= 0:
        sum = 0
        # If we have some elements left in the first array, then add it to the sum.
        if i >= 0:
            sum += a[i]
            i -= 1

        # If we have some elements left in the second array, then add it to the sum.
        if j >= 0:
            sum += b[j]
            j -= 1

        sum += carry
        lastDigit = sum % 10
        carry = sum // 10
        ans.append(lastDigit)

    # If still some carry is left, then push it to the answer.
    if carry:
        ans.append(carry)

    ans = reversed(ans)
    return ans


