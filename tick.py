"""A simulation program for my wife's tick game experiment
todo: add logging to keep track of various things throughout the life of a run
"""
import datetime
import random


# This is setting up and storing all of my variables
class TickSimulationConstants:

    def __init__(self, tick_dictionary, host_population_list, number_of_deer, number_of_possum, number_of_mice):
        self.tick_dictionary = tick_dictionary
        self.host_population_list = host_population_list
        self.number_of_deer = number_of_deer
        self.number_of_possum = number_of_possum
        self.number_of_mice = number_of_mice

    # Generates the tick population
    def populate_tick_dictionary(self, number_of_ticks):
        count = 0
        for t in range(int(number_of_ticks)):
            self.tick_dictionary[f'tick{count}'] = False
            count += 1

        return self.tick_dictionary

    # Sets the starting number of deer
    def deer_quantity(self):
        deer_list = []
        for deer in range(int(self.number_of_deer)):
            deer_list.append('deer')

        return deer_list

    # Sets the starting number of possum
    def possum_quantity(self):
        possum_list = []
        for possum in range(int(self.number_of_possum)):
            possum_list.append('possum')

        return possum_list

    # Sets the starting number of mice
    def mouse_quantity(self):
        mouse_list = []
        for mouse in range(int(self.number_of_mice)):
            mouse_list.append('mouse')

        return mouse_list

    # Makes the list of possible hosts
    def host_population(self):
        deer_list = self.deer_quantity()
        possum_list = self.possum_quantity()
        mouse_list = self.mouse_quantity()

        self.host_population_list = deer_list + possum_list + mouse_list

        return self.host_population_list


# This is the everything for the actual simulation
# All of the variables set up in TickSimulationConstants can be accessed here
class TickSimulationCycle(TickSimulationConstants):
    # The effects of a tick being on a deer
    def deer_host(self):
        t = datetime.datetime.now()
        self.tick_dictionary[f'tick{t}'] = False

        return self.tick_dictionary

    # The effects of a tick being on a possum
    def possum_host(self, tick):
        del self.tick_dictionary[tick]

        return self.tick_dictionary

    # The effects of a tick being on a mouse
    def mouse_host(self, tick):
        r = random.choice([1, 2])
        if r == 1:
            self.tick_dictionary[tick] = True
        else:
            pass

        return self.tick_dictionary

    # The run of a single cycle of feeding
    def feeding_season(self, tick_dictionary, list_of_hosts):
        list_of_ticks = list(tick_dictionary.keys())

        for tick in list_of_ticks:
            host = random.choice(list_of_hosts)
            if host == 'deer':
                tick_dictionary = self.deer_host()

            elif host == 'mouse':
                tick_dictionary = self.mouse_host(tick)

            elif host == 'possum':
                tick_dictionary = self.possum_host(tick)

        return tick_dictionary


def main():
    count = 0

    simulation = TickSimulationCycle({}, [], int(number_deer), int(number_possum), int(number_mouse))

    tick_dictionary = simulation.populate_tick_dictionary(number_tick)
    host_list = simulation.host_population()

    results = open('results.txt', 'a')
    results.write('\n\n')
    results.write(f'Deer: {simulation.number_of_deer}\nPossum: {simulation.number_of_possum}\nMouse: {simulation.number_of_mice}\n')

    while count < int(seasons):
        tick_dictionary = simulation.feeding_season(tick_dictionary, host_list)

        count += 1
        print(f'Population after season {count}: {len(tick_dictionary.items())}')
        results.write(f'Population after season {count}: {len(tick_dictionary.items())}\n')

    tick_pop = len(tick_dictionary)
    infected_ticks = len(list(filter(None, tick_dictionary.values())))

    print(f'Total population: {tick_pop}\nInfected ticks: {infected_ticks}\nClean ticks: {tick_pop - infected_ticks}')
    results.write(
        f'Total population: {tick_pop}\nInfected ticks: {infected_ticks}\nClean ticks: {tick_pop - infected_ticks}')
    results.close()


# Sets the global variables
def setting_variables():
    simulations = input('How many simulations do you want to run?: ')
    number_deer = input('How many deer do you want?: ')
    number_possum = input('How many possum do you want?: ')
    number_mouse = input('How many mice do you want?: ')
    number_tick = input('How many ticks do you want?: ')
    seasons = input('How many cycles?: ')

    return simulations, number_deer, number_possum, number_mouse, number_tick, seasons


if __name__ == '__main__':
    simulations, number_deer, number_possum, number_mouse, number_tick, seasons = setting_variables()

    try:
        int(simulations)
        int(number_deer)
        int(number_possum)
        int(number_mouse)
        int(seasons)
    except ValueError:
        print('Must be an integer, please retry')
        simulations, number_deer, number_possum, number_mouse, number_tick, seasons = setting_variables()

    for i in range(int(simulations)):
        main()



