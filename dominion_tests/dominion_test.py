
import unittest
import mox

class DominionTest(unittest.TestCase):
    def setUp(self):
        super(DominionTest, self).setUp()
        self.mocker = mox.Mox()

    def tearDown(self):
        self.mocker.UnsetStubs()
        super(DominionTest, self).tearDown()
