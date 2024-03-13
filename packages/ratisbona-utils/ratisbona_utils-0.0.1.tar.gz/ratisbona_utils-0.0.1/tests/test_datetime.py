import unittest
from time import sleep

from ratisbona_utils.datetime import Stopwatch


class MyTestCase(unittest.TestCase):

    def test_spending_time_must_advance_clock(self):
        with Stopwatch() as stopwatch:
            sleep(0.1)
        self.assertGreater(stopwatch.time_elapsed_millis, 90)
        print(stopwatch)

    def test_suspending_the_clock_must_not_advance_time(self):
        with Stopwatch() as stopwatch:
            sleep(0.1)
            stopwatch.stop()
            sleep(1.0)
            stopwatch.start()
            sleep(0.1)
        self.assertGreater(stopwatch.time_elapsed_millis, 180)
        self.assertLess(stopwatch.time_elapsed_millis, 220)


if __name__ == '__main__':
    unittest.main()
