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
        result = ticks.populate_tick_dictionary(3)

        self.assertFalse(result)

    def test_deer_quantity(self):
        """Tests that the deer quantity makes the right number"""
        deer = tick.TickSimulationConstants()
        result = deer.deer_quantity(3)

        self.assertEqual(len(result), 3)



