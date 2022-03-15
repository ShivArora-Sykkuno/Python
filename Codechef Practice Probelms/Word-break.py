from typing import List


class Solution:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        def wordb(s, lst, memo=None):
            if memo is None:
                memo = {}
            if s in memo:
                return memo[s]
            if s == "":
                return True
            for i in lst:
                try:
                    if s.index(i) == 0:
                        remWord = s[len(i):]
                        if wordb(remWord, lst):
                            memo[remWord] = True
                            return True
                except:
                    pass
            memo[s] = False
            return False

        return wordb(s, wordDict)
