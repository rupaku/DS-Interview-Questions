'''
https://www.codingninjas.com/codestudio/problems/count-ways-to-reach-nth-stairs_798650
'''
"""
    Time Complexity: O( 2 ^ N )
    Space complexity: O( N )

    Where 'N' is the stair to reach, given in the input.
"""


"""
    Time Complexity: O( 2 ^ N )
    Space complexity: O( N )

    Where 'N' is the stair to reach, given in the input.
"""
def countDistinctWays(nStairs: int) -> int:

    if nStairs < 0:
        return 0
    if nStairs == 0:
        return 1
    ans =countDistinctWays(nStairs-1)+countDistinctWays(nStairs-2)
    return ans


