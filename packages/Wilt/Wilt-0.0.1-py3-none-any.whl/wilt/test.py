import fileinput
import pathlib
import unittest

from . import wilt


class TestWilt(unittest.TestCase):

    def test(self):
        with open(unittest.__file__) as fp:
            self.assertGreater(wilt.wilt(fp), 0)

    def test_fileinput(self):
        path = pathlib.Path(unittest.__file__).parent
        with fileinput.input(list(path.glob('*.py'))) as fp:
            self.assertGreater(wilt.wilt(fp), 0)
