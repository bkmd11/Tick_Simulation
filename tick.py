"""A simulation program for my wife's tick game experiment
todo: add logging to keep track of various things throughout the life of a run
"""
import datetime
import random


# This is setting up and storing all of my variables
class TickSimulationConstants:

    def __init__(self, tick_dic, host_population_list, deer, possum, mouse):
        self.tick_dic = tick_dic
        self.host_population_list = host_population_list
        self.deer = deer
        self.possum = possum
        self.mouse = mouse

    # Generates the tick population
    def pop_dict(self, number_of_ticks):
        count = 0
        for t in range(int(number_of_ticks)):
            self.tick_dic[f'tick{count}'] = False
            count += 1

        return self.tick_dic

    # Sets the starting number of deer
    def deer_quantity(self):
        deer_list = []
        for i in range(int(self.deer)):
            deer_list.append('deer')

        return deer_list

    # Sets the starting number of possum
    def possum_quantity(self):
        possum_list = []
        for i in range(int(self.possum)):
            possum_list.append('possum')

        return possum_list

    # Sets the starting number of mice
    def mouse_quantity(self):
        mouse_list = []
        for i in range(int(self.mouse)):
            mouse_list.append('mouse')

        return mouse_list

    # Makes the list of possible hosts
    def pop_host(self):
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
        self.tick_dic[f'tick{t}'] = False

        return self.tick_dic

    # The effects of a tick being on a possum
    def possum_host(self, tick):
        del self.tick_dic[tick]

        return self.tick_dic

    # The effects of a tick being on a mouse
    def mouse_host(self, tick):
        r = random.choice([1, 2])
        if r == 1:
            self.tick_dic[tick] = True
        else:
            pass

        return self.tick_dic

    # The run of a single cycle of feeding
    def feeding_season(self, tick_dic, list_of_hosts):
        key_list = list(tick_dic.keys())

        for tick in key_list:
            host = random.choice(list_of_hosts)
            if host == 'deer':
                tick_dic = self.deer_host()

            elif host == 'mouse':
                tick_dic = self.mouse_host(tick)

            elif host == 'possum':
                tick_dic = self.possum_host(tick)

        return tick_dic


def main():
    count = 0

    simulation = TickSimulationCycle({}, [], int(number_deer), int(number_possum), int(number_mouse))

    tick_dictionary = simulation.pop_dict(number_tick)
    host_list = simulation.pop_host()

    results = open('results.txt', 'a')
    results.write('\n\n')
    results.write(f'Deer: {simulation.deer}\nPossum: {simulation.possum}\nMouse: {simulation.mouse}\n')

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


if __name__ == '__main__':
    simulations = input('How many simulations do you want to run?: ')
    number_deer = input('How many deer do you want?: ')
    number_possum = input('How many possum do you want?: ')
    number_mouse = input('How many mice do you want?: ')
    number_tick = input('How many ticks do you want?: ')
    seasons = input('How many cycles?: ')

    for i in range(int(simulations)):
        main()



