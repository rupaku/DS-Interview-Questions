# https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict


class Solution:
    def findDuplicate(self, paths):
        content_file_hash = defaultdict(list)
        #paths= root/a 1.txt(abcd) 2.txt(efgh)
        for path in paths:
            path_list = path.split() #[root/a, 1.txt(abcd), 2.txt(efgh)]
            directory = path_list[0] + '/' # root/a/
            for file_str in path_list[1:]:
                name_content = file_str.split('(') #[1.txt, abcd)]
                name = name_content[0] #1.txt
                content = name_content[1].strip(')') #abcd
                content_file_hash[content].append(directory + name) #{abcd: root/a/1.txt}

        """
        Use content_file_hash to create the result that is
        returned from this program.
        """
        print(content_file_hash)
        # {'abcd': ['root/a/1.txt', 'root/c/3.txt'], 'efgh': ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']}
        result = []
        for content in content_file_hash:
            if len(content_file_hash[content]) > 1:
                result.append(content_file_hash[content])
        return result