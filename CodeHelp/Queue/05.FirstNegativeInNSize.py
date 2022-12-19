'''
https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
Sliding window
'''

def printFirstNegativeInteger( A, N, K):
    # code here
    i=0
    j=0
    l=[]
    ans=[]
    while(j<N):
        if(A[j]<0):
            l.append(A[j])
        if(j-i+1)<K:
            j+=1
        elif(j-i+1)==K:
            #print(l)
            if(len(l)==0):
                ans.append(0)
            else:
                #rint(ans)
                ans.append(l[0])
                #if l[0]
                if l[0]==A[i]:
                    l.remove(l[0])
            j+=1
            i+=1
    return ans