"""A simulation program for my wife's tick game experiment. Designed for setting the rules for a game of "tag"
to teach children about lyme disease and the life cycle of ticks.
Three different "host" options will have three different side effects on the ticks.
Deer hosts will allow a new tick to be created
Possum host will remove one tick from the game/simulation
and a mouse host will give a 50/50 chance of becoming infected with lyme.

The main purpose is to help her decide starting values for each role for a summer class she is teaching about ticks.
"""
import datetime
import random
import logging


class TickSimulationConstants:
    """Setting up and storing all my variables"""
    def __init__(self, number_of_ticks, number_of_deer, number_of_possum, number_of_mice):
        self.tick_dictionary = {f'tick{tick}': False for tick in range(number_of_ticks)}
        self.deer_list = ['deer' for deer in range(number_of_deer)]
        self.possum_list = ['possum' for possum in range(number_of_possum)]
        self.mouse_list = ['mouse' for mouse in range(number_of_mice)]
        self.host_population_list = self.deer_list + self.possum_list + self.mouse_list

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
        r = random.choice(['infect', 'not infect'])
        if r == 'infect':
            self.tick_dictionary[tick] = True

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

    simulation = TickSimulationCycle(
        number_of_ticks,
        number_of_deer,
        number_of_possum,
        number_of_mice
    )

    logging.info(str(simulation))

    while count < number_of_cycles:
        simulation.feeding_season()
        count += 1

        logging.info(f'Population after season {count}: {len(simulation.tick_dictionary.items())}')

    infected_ticks = [tick for tick in simulation.tick_dictionary if simulation.tick_dictionary[tick]]

    logging.info(
        f'Total population: {len(simulation)}\nInfected ticks: {len(infected_ticks)}\nClean ticks: {len(simulation) - len(infected_ticks)}\n\n'
    )


def read_int():
    """A function for converting strings of numbers to integers"""
    while True:
        text = input()
        try:
            value = int(text)
            break
        except ValueError:
            print('Must be a valid integer, please enter again.')

    return value


if __name__ == '__main__':
    print('How many simulations do you want to run?: ')
    number_of_simulations = read_int()
    print('How many deer do you want?: ')
    number_of_deer = read_int()
    print('How many possum do you want?: ')
    number_of_possum = read_int()
    print('How many mice do you want?: ')
    number_of_mice = read_int()
    print('How many ticks do you want?: ')
    number_of_ticks = read_int()
    print('How many cycles?: ')
    number_of_cycles = read_int()

    for i in range(number_of_cycles):
        main()

    print('Simulation complete, check results.txt or run again...')
