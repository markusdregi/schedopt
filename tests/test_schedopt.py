import unittest

import schedopt


class TestSchedopt(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(42, schedopt.get_answer_to_everything())
