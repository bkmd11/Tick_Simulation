import unittest
import unittest.mock
import tick


class TestTickSimulationCycle(unittest.TestCase):
    """A test class for TickSimulationCycle methods"""
    def test_deer_host(self):
        """Tests that deer_host adds a tick to the dictionary"""
        deer_host = tick.TickSimulationCycle()
        deer_host.populate_tick_dictionary(3)
        result = deer_host.deer_host()

        self.assertEqual(len(result), 4)

    def test_possum_host(self):
        """Tests that possum_host deletes a tick from the dictionary"""
        possum_host = tick.TickSimulationCycle()
        possum_host.populate_tick_dictionary(3)
        result = possum_host.possum_host('tick0')

        self.assertEqual(len(result), 2)

    def test_possum_host_deletes_the_right_tick(self):
        """Tests that the right tick gets deleted"""
        possum_host = tick.TickSimulationCycle()
        possum_host.populate_tick_dictionary(3)
        result = possum_host.possum_host('tick0')

        self.assertNotIn('tick0', result)

    def test_mouse_host_choice_true(self):
        """Tests that mouse_host changes tick to True"""
        mouse_host = tick.TickSimulationCycle()
        mouse_host.populate_tick_dictionary(3)
        with unittest.mock.patch('random.choice', return_value=1):
            result = mouse_host.mouse_host('tick0')

        self.assertEqual(result['tick0'], True)

    def test_mouse_host_choice_false(self):
        """Tests that mouse_host keeps the tick False"""
        mouse_host = tick.TickSimulationCycle()
        mouse_host.populate_tick_dictionary(3)
        with unittest.mock.patch('random.choice', return_value=2):
            result = mouse_host.mouse_host('tick0')

        self.assertEqual(result['tick0'], False)

    def test_feeding_season_deer_host(self):
        """Tests the a deer host gets found"""
        ticks = tick.TickSimulationCycle()
        ticks.populate_tick_dictionary(1)
        with unittest.mock.patch('random.choice', return_value='deer'):
            result = ticks.feeding_season()

        self.assertEqual(len(result), 2)

    def test_feeding_season_mouse_host(self):
        """Tests the mouse host gets found"""
        ticks = tick.TickSimulationCycle()
        ticks.populate_tick_dictionary(1)
        with unittest.mock.patch('random.choice', return_value='mouse'):
            result = ticks.feeding_season()

        self.assertEqual(len(result), 1)

    def test_feeding_season_possum_host(self):
        """Tests the possum host gets found"""
        ticks = tick.TickSimulationCycle()
        ticks.populate_tick_dictionary(1)
        with unittest.mock.patch('random.choice', return_value='possum'):
            result = ticks.feeding_season()

        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
