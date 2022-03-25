class Solution:
    
    def __init__(self):
        self.n = None
        self.solution = None

    def traversal(self, qnum, Qcord, columns, sums, diag):
        if qnum == self.n:
            sol = []
            for i in range(self.n):
                place = "." * Qcord[i][1] + "Q" + "." * (self.n - Qcord[i][1] - 1)
                sol.append(place)
            self.solution.append(sol)
            return
        for col in range(self.n):
            newcord = (qnum, col)
            if qnum < col:
                startcell = (0, col - qnum)
            else:
                startcell = (qnum - col, 0)
            if (col not in columns) and (sum(newcord) not in sums) and (startcell not in diag):
                colmns, s, d, Qc = columns.copy(), sums.copy(), diag.copy(), Qcord.copy()
                colmns.append(col)
                s.append(sum(newcord))
                d.append(startcell)
                Qc.append(newcord)
                self.traversal(qnum + 1, Qc, colmns, s, d)

    def solveNQueens(self, n: int):
        self.solution = []
        if n in [2, 3]:
            return self.solution
        self.n = n
        self.traversal(0, [], [], [], [])
        return self.solution
