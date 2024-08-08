import random
class Die:
    def __init__(self):
        self._value = None
    @property
    def value(self):
        return self._value
    def roll(self):
        self._value = random.randint(1,6)
        return self._value
class Player:
    def __init__(self, die, is_computer=False):
        self._is_computer = is_computer
        self._die = die
        self._counter = 10    
    @property
    def die(self):
        return self._die
    @property
    def is_computer(self):
        return self._is_computer
    @property
    def counter(self):
        return self._counter
    def increment_counter(self):
        self._counter+=1
    def decrement_counter(self):
        self._counter-=1
    def roll_the_die(self):
        return self._die.roll()
class DiceGame:
    def __init__(self, human_player, computer_player):
        self._human_player = human_player
        self._computer_player = computer_player
    def play(self):
        # welcome message
        print("========================")
        print("Welcome to the Dice Game!")
        print("========================")
        # endless loop until the counter becomes zero
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break
    def play_round(self):
        # welcome message to the round
        print("Welcome to the New Round of Dice Game")
        #input("Press any key on the keyboard to start the round")
        # roll the dice
        human_value = self.rolling_dice()[0]
        computer_value = self.rolling_dice()[1]
        
        # show the dice values 
        self.show_dice_values(human_value, computer_value)
        # printing the initial value of the counters
        self.show_counter_values()
        # checking the winner for the round
        self.check_winner(human_value, computer_value)
        # printing the counters after finishing the round
        self.show_counter_values()
        
    def rolling_dice(self):
        human_value = self._human_player.roll_the_die()
        computer_value = self._computer_player.roll_the_die()
        return (human_value,computer_value)
        
        
    def check_winner(self,human_value,computer_value):
        if human_value>computer_value:
            print("You won this round")
            self._human_player.decrement_counter()
            self._computer_player.increment_counter()
        elif computer_value>human_value:
            print("Computer won this round")
            self._human_player.increment_counter()
            self._computer_player.decrement_counter()
        else:
              print("Nobody won the round, it's a tie")
            
    def show_counter_values(self):
        print("Your counter: {}".format(self._human_player.counter))
        print("Computer counter: {}".format(self._computer_player.counter))
        
    def show_dice_values(self,human_value,computer_value):
        print("Your die: {}".format(human_value))
        print("Computer die: {}".format(computer_value))
            
    def check_game_over(self):
        if self._human_player.counter==0 or self._computer_player.counter==0:
            if self._human_player.counter == 0:
                print("Congratulations! You won the game")
            elif self._computer_player.counter == 0:
                print("Oops, computer won the game")
            return True
        
            
        
human_die = Die()
computer_die = Die()

human_player = Player(human_die)
computer_player = Player(computer_die,True)     

game = DiceGame(human_player,computer_player)
game.play()