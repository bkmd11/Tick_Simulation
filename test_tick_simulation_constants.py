import unittest
import tick


class TestTickSimulationConstants(unittest.TestCase):
    """Tests for my tick simulation class"""
    def test_populate_tick_dictionary_adds_ticks(self):
        """Testing that populate_tick_dictionary adds the correct number of false ticks"""
        result = tick.TickSimulationConstants(3, 3, 3, 3)

        self.assertEqual(result.tick_dictionary, {'tick0': False, 'tick1': False, 'tick2': False})

    def test_all_ticks_are_made_false(self):
        """Tests that none of the ticks are made true"""
        result = tick.TickSimulationConstants(3, 3, 3, 3)

        self.assertNotEqual(result.tick_dictionary, {'tick0': True})

    def test_deer_quantity(self):
        """Tests that the deer quantity makes the right number"""
        result = tick.TickSimulationConstants(3 ,3, 3, 3)

        self.assertEqual(len(result.deer_list), 3)

    def test_possum_quantity(self):
        """Tests that the possum quantity works"""
        result = tick.TickSimulationConstants(3, 3, 3, 3)

        self.assertEqual(len(result), 3)

    def test_mouse_quantity(self):
        """Tests that the mouse quantity works"""
        result = tick.TickSimulationConstants(3, 3, 3, 3)

        self.assertEqual(len(result.mouse_list), 3)

    def test_host_population_list(self):
        """Tests that host_population makes a list of the right length"""
        result = tick.TickSimulationConstants(2, 2, 2, 2)

        self.assertEqual(len(result.host_population_list), 6)

    def test_host_population_list_strings(self):
        """Tests that host_population makes a list with the right strings"""
        result = tick.TickSimulationConstants(2, 2, 2, 2)

        self.assertListEqual(result.host_population_list, ['deer', 'deer', 'possum', 'possum', 'mouse', 'mouse'])


if __name__ == '__main__':
    unittest.main()
