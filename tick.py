"""A simulation program for my wife's tick game experiment
todo: add logging to keep track of various things throughout the life of a run
"""

import datetime
import random


# Generates the tick population
def pop_dict():
    dic = {}
    count = 0
    num_tick = input('How many ticks do you want?: ')
    for t in range(int(num_tick)):
        dic[f'tick{count}'] = False
        count += 1

    return dic


# Generates the population of hosts
# todo: could be broken up into smaller functions
def pop_host():
    list_ = []
    number_deer = input('How many deer do you want?: ')
    number_possum = input('How many possum do you want?: ')
    number_mouse = input('How many mice do you want?: ')
    for i in range(int(number_deer)):
        list_.append('deer')
    for i in range(int(number_possum)):
        list_.append('possum')
    for i in range(int(number_mouse)):
        list_.append('mouse')

    return number_deer, number_mouse, number_possum, list_


# The effects of a tick being on a deer
def deer(dic):
    t = datetime.datetime.now()
    dic[f'tick{t}'] = False

    return dic


# The effects of a tick being on a possum
def possum(tick, dic):
    del dic[tick]

    return dic


# The effects of a tick being on a mouse
def mouse(tick, dic):
    r = random.choice([1, 2])
    if r == 1:
        dic[tick] = True
    else:
        pass

    return dic


# The run of a single cycle of feeding
def feeding_season(tick_dictionary, list_of_hosts):
    key_list = list(tick_dictionary.keys())

    # todo: break this up into a couple smaller functions
    for tick in key_list:

 #       host_or_not = random.choice([1, 2, 3, 4])
#
 #       if host_or_not == 1:
  #          host = 'possum'
   #     else:
    #        host = random.choice(list_of_hosts)
        host = random.choice(list_of_hosts)
        if host == 'deer':
            tick_dictionary = deer(tick_dictionary)

        elif host == 'mouse':
            tick_dictionary = mouse(tick, tick_dictionary)

        elif host == 'possum':
            tick_dictionary = possum(tick, tick_dictionary)

    return tick_dictionary


def main():
    count = 0
    deer, mouse, possum, host_list = pop_host()
    tick_dick = pop_dict()
    number_of_seasons = input('How many feeding seasons do you want?: ')
    results = open('results.txt', 'a')
    results.write('\n\n')
    results.write(f'Deer: {deer}\nPossum: {possum}\nMouse: {mouse}\n')
    while count < int(number_of_seasons):
        tick_dick = feeding_season(tick_dick, host_list)

        count += 1
        print(f'Population after season {count}: {len(tick_dick.items())}')
        results.write(f'Population after season {count}: {len(tick_dick.items())}\n')

    tick_pop = len(tick_dick)
    infected_ticks = len(list(filter(None, tick_dick.values())))

    print(f'Total population: {tick_pop}\nInfected ticks: {infected_ticks}\nClean ticks: {tick_pop - infected_ticks}')
    results.write(f'Total population: {tick_pop}\nInfected ticks: {infected_ticks}\nClean ticks: {tick_pop - infected_ticks}')
    results.close()


if __name__ == '__main__':
    main()
