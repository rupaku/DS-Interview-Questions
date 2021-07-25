'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3056/
'''
class Solution:
    def word_to_tuple(self,word):
        stack=[]
        prev=""
        count = 0
        for ch in word:
            if prev != ch:
                count = 1
                stack.append((ch, count))
            else:
                char, cnt = stack.pop()
                stack.append((char, cnt+1))
            count += 1                
            prev = ch
        return stack

    def expressiveWords(self, S: str, words: List[str]) -> int:
        # S="heeellooo"
        # words =["hello", "hi", "helo"]
        source = self.word_to_tuple(S)
        # print(source)
        # source -- [('h', 1), ('e', 3), ('l', 2), ('o', 3)]
        queries = []
        for word in words:
            ww=self.word_to_tuple(word)
            # print(ww)
            '''[('h', 1), ('e', 1), ('l', 2), ('o', 1)]
                [('h', 1), ('i', 1)]
                [('h', 1), ('e', 1), ('l', 1), ('o', 1)]'''
            if len(ww)==len(source):
                queries.append(ww)
        # print(queries)
        # [[('h', 1), ('e', 1), ('l', 2), ('o', 1)], [('h', 1), ('e', 1), ('l', 1), ('o', 1)]]
        res=[True]*len(queries)

        for i in range(len(source)):
            char_s, count_s = source[i]
            for j, quer in enumerate(queries):
                char_q, count_q = quer[i]
                if char_s != char_q or count_s < count_q or count_s==2 and count_q==1:
                    res[j]=False
        return sum(res)



        