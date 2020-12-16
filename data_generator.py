import game_simulator as gs

class Data_Generator():

    def __init__(self, num_players_list, num_gelt_list, num_simulations):

        self.num_players_list = num_players_list
        self.num_gelt_list = num_gelt_list
        self.num_simulations = num_simulations
        self.data = []

    def generate_data(self):

        for num_players in self.num_players_list:
            for num_gelt in self.num_gelt_list:

                self.game_simulator = gs.Game_Simulator(num_players, num_gelt)
                game_lengths = self.game_simulator.get_game_lengths(self.num_simulations)

                self.data.append((num_players, num_gelt, game_lengths))

        return self.data
