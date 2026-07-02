class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(index, used, curr_i, curr_j):
            
            if index == len(word):
                return True

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for di, dj in directions:
                ni, nj = di + curr_i, dj + curr_j

                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):

                    if used[ni][nj]:
                        continue

                    if board[ni][nj] != word[index]:
                        continue

                    used[ni][nj] = True

                    if backtrack(index + 1, used, ni, nj):
                        return True
                    
                    used[ni][nj] = False
            
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:

                    used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                    used[i][j] = True

                    if backtrack(1, used, i, j):
                        return True
                        
        return False


