import random

class Game_Simulator():

    def __init__(self, num_players, num_gelt):

        self.num_gelt_total = num_gelt
        self.num_players = num_players

        self.players = list(range(self.num_players)) #EACH PLAYER GETS A NUMBER
        self.num_gelt_per_player = [1 for player in self.players] #ONE GELT PER PLAYER
        self.num_gelt_pot = self.num_gelt_total - num_players #REMAINDER GO IN POT

        self.game_lengths = []

    def turn(self):

        dreidel_spin = random.randint(1, 4)

        if dreidel_spin == 1: #SHIN

            if self.num_gelt_per_player[self.current_player_index] > 0:

                self.num_gelt_per_player[self.current_player_index] -= 1
                self.num_gelt_pot +=1

        elif dreidel_spin == 2: #HAY

            half_pot = self.num_gelt_pot //2

            self.num_gelt_per_player[self.current_player_index] += half_pot
            self.num_gelt_pot -= half_pot

        elif dreidel_spin == 3: #GIMMEL

            self.num_gelt_per_player[self.current_player_index] += self.num_gelt_pot
            self.num_gelt_pot = 0

        else: #NUN
            pass

    def simulate_game(self):

        num_turns = 0
        is_game_over = False

        while not is_game_over:

            self.current_player_index = num_turns % self.num_players
            self.turn()

            if self.num_gelt_per_player[self.current_player_index] == self.num_gelt_total:
                self.game_lengths.append(num_turns + 1)
                is_game_over = True

            else:
                num_turns += 1

    def get_game_lengths(self, num_simulations):

        for i in range(num_simulations):
            self.simulate_game()

        return self.game_lengths
