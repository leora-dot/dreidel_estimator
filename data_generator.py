import game_simulator as gs

class Data_Generator():

    def __init__(self, num_players_list, num_gelt_list, num_simulations):

        self.num_players_list = num_players_list
        self.num_gelt_list = num_gelt_list
        self.num_simulations = num_simulations
        self.data = []

    def generate_data(self):

        num_configurations_total = len(self.num_gelt_list) * len(self.num_players_list)
        num_configurations_complete = 0

        for num_players in self.num_players_list:
            for num_gelt in self.num_gelt_list:

                self.game_simulator = gs.Game_Simulator(num_players, num_gelt)
                game_lengths = self.game_simulator.get_game_lengths(self.num_simulations)

                self.data.append((num_players, num_gelt, game_lengths))

                num_configurations_complete += 1

                if (num_configurations_complete % 10 == 0) or (num_configurations_complete == num_configurations_total):
                    print("{}/{} Configurations Complete".format(num_configurations_complete, num_configurations_total))

        return self.data
