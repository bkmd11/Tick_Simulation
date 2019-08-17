import unittest
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

    # todo: figure out how to mock the random choice feature, or else it will fail sometimes
    def test_mouse_host(self):
        """Tests that mouse_host changes tick to True"""
        mouse_host = tick.TickSimulationCycle()
        mouse_host.populate_tick_dictionary(3)
        result = mouse_host.mouse_host('tick0')

        self.assertEqual(result['tick0'], True)

    # todo: figure out mocking random choices for feeding_season


if __name__ == '__main__':
    unittest.main()
