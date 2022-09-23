'''
https://www.codingninjas.com/codestudio/problems/aggressive-cows_1082559?leftPanelTab=1
'''

def is_possible(stalls, k,mid):
    cow_cnt=0
    last_pos=stalls[0]
    for i in range(len(stalls)):
        if (last_pos+stalls[i] >= mid):
            cow_cnt =cow_cnt+1
            if cow_cnt == k:
                return True
            last_pos = stalls[i]
    return False

def aggressiveCows(stalls, k):
    # Write your code here
    # Return the minimum number of pages
    s=0
    maxi=0
    for i in range(len(stalls)):
        maxi=max(maxi,stalls[i])
    e=maxi
    ans=-1
    while s <= e:
        mid= (s+e)//2
        if is_possible(stalls, k,mid):
            ans=mid
            s=mid+1
        else:
             e=mid-1 
    return ans
