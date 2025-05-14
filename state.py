class State:
    
    __board_h = 5 #height of the board
    __board_w = 5 #width of the board
    __empty = ' ' #character that represents __empty space
    p1_char = 'X' #character that represents a piece by player 1
    p2_char = 'O' #character that represents a piece by player 1

    def __init__(self, matrix, to_move: bool):
        self.board = matrix
        self.to_move = to_move # True = p1 move, False = p2 move

    def print_board(self):
        for i in range(self.__board_h):
            print('|', end=' ')
            for j in range(self.__board_w):
                print(self.board[i][j], end=" ")
            print('|')

    #returns length of longest horizontal line of specified character
    def longest_h_line(self, player_char):
        longest_line_lenght = 0
       
        for i in range(self.__board_h):
            line_length = 0
            
            for j in range(self.__board_w):
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
       
        for j in range(self.__board_w):
            line_length = 0
            
            for i in range(self.__board_h):
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
        for row in range(self.__board_h):
            i = row
            j = 0
            line_length = 0

            while (i >= 0 and j < self.__board_w):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                    if line_length > longest_line_lenght:
                        longest_line_lenght = line_length
                else: #otherwise the line is broken, reset the count
                    line_length = 0
                i = i-1
                j = j+1

        #diagonals starting from the bottom row
        for col in range(1,self.__board_w):
            i = self.__board_h-1
            j = col
            line_length = 0

            while (i >= 0 and j < self.__board_w):
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
        for row in range(self.__board_h):
            i = row
            j = self.__board_w-1
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
        for col in reversed(range(self.__board_w-1)):
            i = self.__board_h-1
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
    
    #returns the number of pieces of a specified character that aren't along an edge of the board
    def center_pieces(self, player_char):
        count = 0
        for i in range(1,self.__board_h-1):
            for j in range(1,self.__board_w-1):
                if self.board[i][j] == player_char:
                    count = count + 1
        
        return count
    
    #returns the amount and average length of lines (longer than just 1 character) of a specified character
    def line_stats(self, player_char):
        line_lenghts = []

        #checking horizontals
        for i in range(self.__board_h):
            line_length = 0
            for j in range(self.__board_w):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                elif line_length > 0: #otherwise the line is broken, store value and reset the count (if there is a value)
                    line_lenghts.append(line_length)
                    line_length = 0

        #checking verticals
        for j in range(self.__board_w):
            line_length = 0
            for i in range(self.__board_h):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                elif line_length > 0: #otherwise the line is broken, store value and reset the count (if there is a value)
                    line_lenghts.append(line_length)
                    line_length = 0
        
        #checking / diagonals
        #diagonals starting from the leftmost collumn
        for row in range(self.__board_h):
            i = row
            j = 0
            line_length = 0
            while (i >= 0 and j < self.__board_w):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                elif line_length > 0: #otherwise the line is broken, store value and reset the count (if there is a value)
                    line_lenghts.append(line_length)
                    line_length = 0
                i = i-1
                j = j+1
        #diagonals starting from the bottom row
        for col in range(1,self.__board_w):
            i = self.__board_h-1
            j = col
            line_length = 0
            while (i >= 0 and j < self.__board_w):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                elif line_length > 0: #otherwise the line is broken, store value and reset the count (if there is a value)
                    line_lenghts.append(line_length)
                    line_length = 0
                i = i-1
                j = j+1

        #checking \ diagonals
        #diagonals starting from the rightmost collumn
        for row in range(self.__board_h):
            i = row
            j = self.__board_w-1
            line_length = 0
            while (i >= 0 and j >= 0):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                elif line_length > 0: #otherwise the line is broken, store value and reset the count (if there is a value)
                    line_lenghts.append(line_length)
                    line_length = 0
                i = i-1
                j = j-1
        #diagonals starting from the bottom row
        for col in reversed(range(self.__board_w-1)):
            i = self.__board_h-1
            j = col
            line_length=0
            while (i >= 0 and j >=0):
                if self.board[i][j] == player_char: #if it's that player's piece, line gets bigger
                    line_length = line_length + 1
                elif line_length > 0: #otherwise the line is broken, store value and reset the count (if there is a value)
                    line_lenghts.append(line_length)
                    line_length = 0
                i = i-1
                j = j-1

        line_lenghts = [i for i in line_lenghts if i != 1] #removes all "lines" of lenght 1
        n_lines =  len(line_lenghts)
        avg_line_length = 0
        if n_lines != 0:
            avg_line_length = sum(line_lenghts)/n_lines
        return n_lines, avg_line_length
    
    #returns number of pieces of a specified character
    def piece_count(self, player_char):
        count = 0
        for i in range(self.__board_h):
            for j in range(self.__board_w):
                if self.board[i][j] == player_char:
                    count = count + 1

        return count
    
    #returns a list of collumns where it would be legal to place a piece
    def legal_moves(self):
        moves = []
        for j in range(self.__board_w):
            if self.board[0][j] == self.__empty:
                moves.append(j)
        return moves
    
    #returns a new state with a piece placed in that column, or None if the action is invalid
    def action(self, col):
        if self.board[0][col] != self.__empty:
            return None
        row = 1
        for row in range(1,self.__board_h):
            if self.board[row][col] != self.__empty:
                row = row - 1
                break

        if self.to_move:
            player_char = self.p1_char
        else:
            player_char = self.p2_char

        new_board = list(map(list, self.board))
        new_board[row][col] = player_char

        return State(new_board, not self.to_move)

    #returns None if state isn't terminal. If it is terminal, returns 1 if p1 wins, 2 if p2 wins, and 3 if its a tie
    def is_terminal(self):
        
        if (self.longest_h_line(self.p1_char) >= 4 or
            self.longest_v_line(self.p1_char) >= 4 or
            self.longest_d_up_line(self.p1_char) >= 4 or
            self.longest_d_down_line(self.p1_char) >=4):
            return 1
        
        if (self.longest_h_line(self.p2_char) >= 4 or
            self.longest_v_line(self.p2_char) >= 4 or
            self.longest_d_up_line(self.p2_char) >= 4 or
            self.longest_d_down_line(self.p2_char) >=4):
            return 2
        
        #no legal moves left (board full), tie
        if self.legal_moves() == []:
            return 3
        
        return None
