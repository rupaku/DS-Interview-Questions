'''
https://leetcode.com/problems/word-ladder/submissions/
https://www.youtube.com/watch?v=ZVJ3asMoZ18
'''
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        print(all_combo_dict)
        # {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], 'ho*': ['hot'], 'd*t': ['dot'], 'do*': ['dot', 'dog'], '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'], 'l*t': ['lot'], 'lo*': ['lot', 'log'], 'l*g': ['log'], 'c*g': ['cog'], 'co*': ['cog']}

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                print(current_word)
                ''' hit
                    hit
                    hit
                    hot
                    hot
                    hot
                    dot
                    dot
                    dot
                    lot
                    lot
                    lot
                    dog ''' 
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                print(intermediate_word)

                ''' *it
                    h*t
                    hi*
                    *ot
                    h*t
                    ho*
                    *ot
                    d*t
                    do*
                    *ot
                    l*t
                    lo*
                    *og   '''
                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))