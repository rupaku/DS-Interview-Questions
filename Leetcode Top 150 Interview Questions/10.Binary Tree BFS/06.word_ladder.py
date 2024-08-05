# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
            
        word_len = len(beginWord)
        
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
                
        queue = deque([(beginWord, 1)])
        visited = {beginWord: 1}
        
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(word_len):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                        
                all_combo_dict[intermediate_word] = []
                
        return 0