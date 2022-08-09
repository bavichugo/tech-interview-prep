class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            hSet = set()
            vSet = set()
            for j in range(9):
                # Horizontal
                if board[i][j] in hSet:
                    return False
                if board[i][j] != ".":
                    hSet.add(board[i][j])
                
                # Vertical
                if board[j][i] in vSet:
                    return False
                if board[j][i] != ".":
                    vSet.add(board[j][i])
        
        # 0: [0, 0] 1: [3, 0] 2: [6, 0] 3: [0, 3]
        for i in range(9):
            hAdd = (i % 3) * 3
            vAdd = (i // 3) * 3
            bSet = set()
            test = []
            for v in range(vAdd, vAdd + 3):
                for h in range(hAdd, hAdd + 3):
                    if board[v][h] != ".":
                        if board[v][h] in bSet:
                            return False
                        bSet.add(board[v][h])
        return True