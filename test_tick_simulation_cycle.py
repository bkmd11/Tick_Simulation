import unittest
import unittest.mock
import tick


class TestTickSimulationCycle(unittest.TestCase):
    """A test class for TickSimulationCycle methods"""
    def test_deer_host(self):
        """Tests that deer_host adds a tick to the dictionary"""
        result = tick.TickSimulationCycle(3, 3, 3, 3)
        result.deer_host()

        self.assertEqual(len(result.tick_dictionary), 4)

    def test_possum_host(self):
        """Tests that possum_host deletes a tick from the dictionary"""
        result = tick.TickSimulationCycle(3, 3, 3, 3)
        result.possum_host('tick0')

        self.assertEqual(len(result.tick_dictionary), 2)

    def test_possum_host_deletes_the_right_tick(self):
        """Tests that the right tick gets deleted"""
        result = tick.TickSimulationCycle(3, 3, 3, 3)
        result.possum_host('tick0')

        self.assertNotIn('tick0', result.tick_dictionary)

    def test_mouse_host_choice_true(self):
        """Tests that mouse_host changes tick to True"""
        result = tick.TickSimulationCycle(3, 3, 3, 3)
        with unittest.mock.patch('random.choice', return_value='infect'):
            result.mouse_host('tick0')

        self.assertEqual(result.tick_dictionary['tick0'], True)

    def test_mouse_host_choice_false(self):
        """Tests that mouse_host keeps the tick False"""
        result = tick.TickSimulationCycle(3, 3, 3, 3)
        with unittest.mock.patch('random.choice', return_value='not infect'):
            result.mouse_host('tick0')

        self.assertEqual(result.tick_dictionary['tick0'], False)

    def test_feeding_season_deer_host(self):
        """Tests the a deer host gets found"""
        result = tick.TickSimulationCycle(3, 3, 3, 3)
        with unittest.mock.patch('random.choice', return_value='deer'):
            result.feeding_season()

        self.assertEqual(len(result.tick_dictionary), 4)

    def test_feeding_season_mouse_host(self):
        """Tests the mouse host gets found"""
        result = tick.TickSimulationCycle(3, 3, 3, 3)
        with unittest.mock.patch('random.choice', return_value='mouse'):
            result.feeding_season()

        self.assertEqual(len(result.tick_dictionary), 3)

    def test_feeding_season_possum_host(self):
        """Tests the possum host gets found"""
        result = tick.TickSimulationCycle(3, 3, 3, 3)
        with unittest.mock.patch('random.choice', return_value='possum'):
            result.feeding_season()

        self.assertEqual(len(result.tick_dictionary), 2)


if __name__ == '__main__':
    unittest.main()
