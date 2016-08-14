import unittest
import boggle

class TestBoggle(unittest.TestCase):
    def test_Is_This_Thing_On(self):
        self.assertEqual(1, boggle.check())
