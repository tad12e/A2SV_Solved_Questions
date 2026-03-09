class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rotations = [True] * 4
        for i in range(len(target)):
            for j in range(len(target[i])):
                if mat[i][j] != target[i][j]:
                    rotations[0] = False
                if mat[-j-1][i] != target[i][j]:
                    rotations[1] = False
                if mat[j][-i-1] != target[i][j]:
                    rotations[2] = False
                if mat[-i-1][-j-1] != target[i][j]:
                    rotations[3] = False
                if True not in rotations:
                    return False
        return True
        
     

        