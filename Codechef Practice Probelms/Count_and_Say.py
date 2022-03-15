class Solution:
    def countAndSay(self, n):
        prev = "1"
        for i in range(n-1):
            current = '.'
            count = 0
            new = ""
            for c in prev:
                if c != current:
                    if current != '.':
                        new += str(count)+current
                    current = c
                    count=1
                else:
                    count+=1
            new +=str(count)+current
            prev = new
        return prev