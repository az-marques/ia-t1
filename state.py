class State:
    
    board_h = 5 #height of the board
    board_w = 5 #width of the board

    def __init__(self, matrix):
        self.board = matrix

    def print_board(self):
        for i in range(self.board_h):
            print('|', end=' ')
            for j in range(self.board_w):
                print(self.board[i][j], end=" ")
            print('|')

    #returns length of longest horizontal line of specified character
    def longest_h_line(self, player_char):
        longest_line_lenght = 0
       
        for i in range(self.board_h):
            line_length = 0
            
            for j in range(self.board_w):
                #if it's that player's piece, line gets bigger
                if self.board[i][j] == player_char:
                    line_length = line_length + 1
                    if line_length > longest_line_lenght:
                        longest_line_lenght = line_length
                #otherwise the line is broken, reset the count
                else:
                    line_length = 0
        
        return longest_line_lenght
    
    #returns length of longest vertical line of specified character
    def longest_v_line(self, player_char):
        longest_line_lenght = 0
       
        for j in range(self.board_w):
            line_length = 0
            
            for i in range(self.board_h):
                #if it's that player's piece, line gets bigger
                if self.board[i][j] == player_char:
                    line_length = line_length + 1
                    if line_length > longest_line_lenght:
                        longest_line_lenght = line_length
                #otherwise the line is broken, reset the count
                else:
                    line_length = 0
        
        return longest_line_lenght
    
    #returns length of longest upwards diagonal (/) line of specified character
    def longest_d_up_line(self, player_char):
        longest_line_lenght = 0

        #diagonals starting from the leftmost collumn
        for row in range(self.board_h):
            i = row
            j = 0
            line_length = 0

            while (i >= 0 and j < self.board_w):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                    if line_length > longest_line_lenght:
                        longest_line_lenght = line_length
                else: #otherwise the line is broken, reset the count
                    line_length = 0
                i = i-1
                j = j+1

        #diagonals starting from the bottom row
        for col in range(1,self.board_w):
            i = self.board_h-1
            j = col
            line_length = 0

            while (i >= 0 and j < self.board_w):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                    if line_length > longest_line_lenght:
                        longest_line_lenght = line_length
                else: #otherwise the line is broken, reset the count
                    line_length = 0                
                i = i-1
                j = j+1
        
        return longest_line_lenght
        

    #returns length of longest downwards diagonal (\) line of specified character
    def longest_d_down_line(self, player_char):
        longest_line_lenght = 0

        #diagonals starting from the rightmost collumn
        for row in range(self.board_h):
            i = row
            j = self.board_w-1
            line_length = 0

            while (i >= 0 and j >= 0):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                    if line_length > longest_line_lenght:
                        longest_line_lenght = line_length
                else: #otherwise the line is broken, reset the count
                    line_length = 0
                i = i-1
                j = j-1

        #diagonals starting from the bottom row
        for col in reversed(range(self.board_w-1)):
            i = self.board_h-1
            j = col
            line_length=0

            while (i >= 0 and j >=0):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                    if line_length > longest_line_lenght:
                        longest_line_lenght = line_length
                else: #otherwise the line is broken, reset the count
                    line_length = 0
                i = i-1
                j = j-1

        return longest_line_lenght
    
    #returns number of pieces of a specified character
    def piece_count(self, player_char):
        count = 0
        for i in range(self.board_h):
            for j in range(self.board_w):
                if self.board[i][j] == player_char:
                    count = count + 1

        return count

                    
            









