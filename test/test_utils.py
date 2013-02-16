import os
import shutil
import unittest
import tempfile
from groundstation import utils


class TestUtilsLeafDirs(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmpdir, "foo", "bar", "baz"))
        os.makedirs(os.path.join(self.tmpdir, "foo", "borp"))
        os.makedirs(os.path.join(self.tmpdir, "foo", "test", "test", "test"))

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_find_leaf_dirs(self):
        leaves = utils.find_leaf_dirs(self.tmpdir)

        self.assertIn(os.path.join(self.tmpdir, "foo", "bar", "baz"), leaves)
        self.assertIn(os.path.join(self.tmpdir, "foo", "borp"), leaves)
        self.assertIn(os.path.join(self.tmpdir, "foo", "test", "test", "test"), leaves)

        self.assertNotIn(os.path.join(self.tmpdir, "foo", "bar"), leaves)
        self.assertNotIn(os.path.join(self.tmpdir, "foo"), leaves)
        self.assertNotIn(os.path.join(self.tmpdir, "foo", "test", "test"), leaves)
