'''
https://leetcode.com/problems/sentence-screen-fitting/submissions/
https://www.youtube.com/watch?v=e987rKv1d7E
'''
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s=' '.join(sentence) +' '
        n=len(s)
        total_len=0
        for _ in range(rows):
            total_len += cols
            
            if s[total_len % n] == ' ':
                total_len += 1
            else:
                while(s[(total_len-1)%n] != ' ' and total_len > 0):
                    total_len -= 1
        return total_len//n
        