'''
https://leetcode.com/problems/text-justification/
https://www.youtube.com/watch?v=r-F1sCTmZxA
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        num of lettes + spaces +new word > maxwidth
        1 word -> pad to right
        n word -> uniformly distribute spaces
        words-> padded to the right
        '''
        if not words:
            return
        res=[]
        curr=[]
        num_of_letters=0
        for w in words:
            if num_of_letters + len(curr) +len(w) > maxWidth:
                if len(curr) == 1:
                    res.append(curr[0]+' '*(maxWidth - num_of_letters))
                else:
                    num_of_spaces= maxWidth - num_of_letters
                    space_between_words,extra=divmod(num_of_spaces,len(curr)-1)

                    for i in range(extra):
                        curr[i] += ' '
                    res.append((' '*space_between_words).join(curr))
                curr=[]
                num_of_letters=0
                
            curr.append(w)
            num_of_letters += len(w)
        res.append(' '.join(curr)+' '*(maxWidth - num_of_letters- len(curr)+ 1))
        return res
                

