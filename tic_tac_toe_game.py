import random
class Move:
    def __init__(self, value):
        self._value = value 
    @property
    def value(self):
        return self._value
    def is_valid(self):
        if isinstance(self._value, int) and self._value in range(1,10):
            return True
        return False
    def get_row(self):
        if self._value in range(1,4):
            return 0  # First row
        elif self._value in range(4,7):
            return 1  # Second row
        else:
            return 2  # Third row
    def get_column(self):
        if self._value in [1,4,7]:
            return 0  # First column
        elif self._value in [2,5,8]:
            return 1  # Second column
        else:
            return 2  # Third column
    
class Player:
    
    PLAYER_MARKER = 'X'
    COMPUTER_MARKER = 'O'
    
    def __init__(self, is_computer = False): 
        self._is_computer = is_computer
        if is_computer == False:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER 
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @ property
    def marker(self):
        return self._marker
    
    def get_move(self):
        if self._is_computer == False:
            return self.get_human_move()
        else:
            return self.get_computer_move()
    
    def get_human_move(self):
        while True:
            user_move = int(input("Please enter your move (1-9): "))
            move = Move(user_move)
            if move.is_valid():
                break
            else:
                print("Please enter a integer between 1 and 9.")
        return move
                
    def get_computer_move(self):
        random_choice = random.randint(1,9)
        move = Move(random_choice)
        print("Computer Move (1-9): {}".format(move.value))
        return move
        
    
class Board:
    
    EMPTY_CELL = 0
    def __init__(self):
        self.game_board = [[0,0,0],
                           [0,0,0],
                           [0,0,0]]
        
    def print_boards(self):
        print("\nPositions:")
        self.print_board_with_positions()
        
        print("\nBoard: ")
        for row in self.game_board:
            print("|",end = "")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |",end="")
                else:
                    print(f" {column} |",end="")
            print("")
    
    def print_board_with_positions(self):
        print("| 1 | 2 | 3 | \n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
        
    def submit_move(self, player, move):
        row = move.get_row()
        column = move.get_column()
        value = self.game_board[row][column]
        
        if value == Board.EMPTY_CELL:
            self.game_board[row][column] = player.marker
        else:
            print("This place is already occupied. Choose another one")
            
    def check_is_game_over(self, player, last_move):
        return ((self.check_row(player, last_move)) 
                or (self.check_column(player, last_move)) 
                or (self.check_diagonal(player)) 
                or (self.check_anti_diagonal(player)))
  
    def check_row(self, player, last_move):
        row = last_move.get_row()
        board_row = self.game_board[row]
        return board_row.count(player.marker) == 3
    
    def check_column(self, player, last_move):
        marker_count = 0
        column_index = last_move.get_column()
        for row in self.game_board:
            if row[column_index] == player.marker:
                marker_count+=1
        return (marker_count == 3)
    
    def check_diagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                marker_count += 1
        return (marker_count == 3)
    
    def check_anti_diagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                marker_count += 1
        return (marker_count == 3)
    
    def check_tie(self):
        for row in self.game_board:
            if Board.EMPTY_CELL in row:
                return False 
        return True
    
    def reset_game_board(self):
        for row in range(3):
            for column in range(3):
                self.board[row][column] = Board.EMPTY_CELL
            
            
class TicTacToeGame:
    
    def start(self):
        print("===========================")
        print("Welcome to Tic Tac Toe Game")
        print("===========================")
        
        # defining the instances 
        board = Board()
        human_player = Player()
        computer_player = Player(True)
        
        # showing the game board to the user 
        board.print_boards()
        
        while True:    # To ask the user if he wants to play again
            while True:   # Main logic of the game - Get move, check tie , check game over
                human_move = human_player.get_move()
                board.submit_move(human_player, human_move)
                board.print_boards()
                
                if board.check_is_game_over(human_player, human_move):
                    print("Wow, you won the game")
                    break
                elif board.check_tie():
                        print("It's a Tie ")
                        break
                
                computer_move = computer_player.get_move()
                board.submit_move(computer_player, computer_move)
                board.print_boards()

                if board.check_is_game_over(computer_player, computer_move):
                    print("Oops, computer won the game!")
                    break
                elif board.check_tie():
                    print("It's a Tie ")
                    break
                
            play_again = input("Do you want to play again? Enter 'Y' for yes and 'N' for no").upper()
            if play_again == 'N':
                print("Bye, Bis bald")
                break
            elif play_again == 'Y':
                self.start_new_round(board)
            else:
                print("You have entered some another character so I will assume that you want to play again")
                self.start_new_round(board)
    
    def start_new_round(self, board):
        print("=========")
        print("NEW ROUND")
        print("=========")
        board.reset_game_board()
        board.print_boards()

game = TicTacToeGame()
game.start()