class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res=[]
        for i in range(9):
            for j in range(9):
                elem=board[i][j]
                if elem !=".":
                    res+=[
                        ("row",i,elem)
                    ,("col",j,elem)
                    ,(i//3,j//3,elem)
                    ]
        return len(res)==len(set(res))
        