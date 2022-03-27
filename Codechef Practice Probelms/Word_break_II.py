from collections import defaultdict as dd


def wordBreak(s, wordDict):
    dp = [True] + [False] * len(s)
    d = dd(lambda: [])
    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                if j == 0:
                    d[i].append(s[j:i])
                else:
                    for k in d[j]:
                        d[i].append(k + " " + s[j:i])
    if dp[len(s)]:
        return d[len(s)]
    return []
