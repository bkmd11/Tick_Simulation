import unittest
import tick


class TestTickSimulationConstants(unittest.TestCase):
    """Tests for my tick simulation class"""
    def test_populate_tick_dictionary_adds_ticks(self):
        """Testing that populate_tick_dictionary adds the correct number of false ticks"""
        ticks = tick.TickSimulationConstants()
        result = ticks.populate_tick_dictionary(3)

        self.assertEqual(result, {'tick0': False, 'tick1': False, 'tick2': False})

    def test_all_ticks_are_made_false(self):
        """Tests that none of the ticks are made true"""
        ticks = tick.TickSimulationConstants()
        result = ticks.populate_tick_dictionary(1)

        self.assertNotEqual(result, {'tick0': True})

    def test_deer_quantity(self):
        """Tests that the deer quantity makes the right number"""
        deer = tick.TickSimulationConstants()
        result = deer.deer_quantity(3)

        self.assertEqual(len(result), 3)

    def test_possum_quantity(self):
        """Tests that the possum quantity works"""
        possum = tick.TickSimulationConstants()
        possum.possum_quantity(3)
        result = possum.possum_list

        self.assertEqual(len(result), 3)

    def test_mouse_quantity(self):
        """Tests that the mouse quantity works"""
        mouse = tick.TickSimulationConstants()
        result = mouse.mouse_quantity(3)

        self.assertEqual(len(result), 3)

    ####################################################
    ### These are becoming integration tests ###########
    ### Could use setup here to eliminate redundancy ###
    ####################################################
    def test_host_population_list(self):
        """Tests that host_population makes a list of the right length"""
        host_pop = tick.TickSimulationConstants()
        host_pop.mouse_quantity(2)
        host_pop.deer_quantity(2)
        host_pop.possum_quantity(2)
        result = host_pop.host_population()

        self.assertEqual(len(result), 6)

    def test_host_population_list_strings(self):
        """Tests that host_population makes a list with the right strings"""
        host_pop = tick.TickSimulationConstants()
        host_pop.mouse_quantity(2)
        host_pop.deer_quantity(2)
        host_pop.possum_quantity(2)
        result = host_pop.host_population()
        result.sort()

        self.assertListEqual(result, ['deer', 'deer', 'mouse', 'mouse',  'possum', 'possum'])


if __name__ == '__main__':
    unittest.main()
