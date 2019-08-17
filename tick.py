"""A simulation program for my wife's tick game experiment
"""
import datetime
import random
import logging


# todo: break each host into its own class and figure out how to use dunders to get length and dic values


class TickSimulationConstants:
    """Setting up and storing all my variables"""

    def __init__(self):
        self.tick_dictionary = {}
        self.deer_list = []
        self.possum_list = []
        self.mouse_list = []
        self.host_population_list = []

    def populate_tick_dictionary(self, number_of_ticks):
        """Generates the tick population"""
        count = 0
        for t in range(int(number_of_ticks)):
            self.tick_dictionary[f'tick{count}'] = False
            count += 1

        return self.tick_dictionary

    def deer_quantity(self, number_of_deer):
        """Sets the starting number of deer"""
        for deer in range(number_of_deer):
            self.deer_list.append('deer')

        return self.deer_list

    def possum_quantity(self, number_of_possum):
        """Sets the starting number of possum"""
        for possum in range(number_of_possum):
            self.possum_list.append('possum')

        return self.possum_list

    def mouse_quantity(self, number_of_mice):
        """Sets the starting number of mice"""
        for mouse in range(number_of_mice):
            self.mouse_list.append('mouse')

        return self.mouse_list

    def host_population(self):
        """Makes the list of possible hosts"""
        self.host_population_list = self.deer_list + self.possum_list + self.mouse_list

        return self.host_population_list

    def __str__(self):
        """The string of host values"""
        return f'Deer: {len(self.deer_list)}\nPossum: {len(self.possum_list)}\nMouse: {len(self.mouse_list)}'

    def __len__(self):
        """The length of the tick dictionary"""
        return len(self.tick_dictionary)


class TickSimulationCycle(TickSimulationConstants):
    """This is everything for the actual simulation"""
    def deer_host(self):
        """The effects of a tick being on a deer"""
        t = datetime.datetime.now()
        self.tick_dictionary[f'tick{t}'] = False

        return self.tick_dictionary

    def possum_host(self, tick):
        """The effects of a tick being on a possum"""
        del self.tick_dictionary[tick]

        return self.tick_dictionary

    def mouse_host(self, tick):
        """The effects of a tick being on a mouse"""
        r = random.choice([1, 2])
        if r == 1:
            self.tick_dictionary[tick] = True
        else:
            pass

        return self.tick_dictionary

    def feeding_season(self):
        """The run of a single cycle of feeding"""
        list_of_ticks = list(self.tick_dictionary.keys())

        for tick in list_of_ticks:
            host = random.choice(self.host_population_list)
            if host == 'deer':
                self.tick_dictionary = self.deer_host()

            elif host == 'mouse':
                self.tick_dictionary = self.mouse_host(tick)

            elif host == 'possum':
                self.tick_dictionary = self.possum_host(tick)

        return self.tick_dictionary


def main():
    logging.basicConfig(level=logging.DEBUG, filename='results.txt', format='')
    count = 0

    simulation = TickSimulationCycle()

    simulation.populate_tick_dictionary(int(number_tick))
    simulation.deer_quantity(int(number_deer))
    simulation.possum_quantity(int(number_possum))
    simulation.mouse_quantity(int(number_mouse))
    simulation.host_population()

    logging.info(str(simulation))

    while count < int(seasons):
        simulation.feeding_season()
        count += 1

        logging.info(f'Population after season {count}: {len(simulation.tick_dictionary.items())}')

    infected_ticks = len(list(filter(None, simulation.tick_dictionary.values())))

    logging.info(
        f'Total population: {len(simulation)}\nInfected ticks: {infected_ticks}\nClean ticks: {len(simulation) - infected_ticks}\n\n')


def setting_variables():
    """Sets the global variables"""
    number_of_simulations = input('How many simulations do you want to run?: ')
    number_of_deer = input('How many deer do you want?: ')
    number_of_possum = input('How many possum do you want?: ')
    number_of_mice = input('How many mice do you want?: ')
    number_of_ticks = input('How many ticks do you want?: ')
    cycles = input('How many cycles?: ')

    return number_of_simulations, number_of_deer, number_of_possum, number_of_mice, number_of_ticks, cycles


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

    print('Simulation complete, check results.txt or run again...')
