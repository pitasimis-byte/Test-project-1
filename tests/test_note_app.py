import os
import tempfile
import unittest
from src.note_app import NotesManager

class TestNotesManager(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmpdir.name, "notes.json")
        self.nm = NotesManager(self.path)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_add_and_list(self):
        self.nm.add("first")
        self.nm.add("second")
        self.assertEqual(self.nm.list(), ["first", "second"])

    def test_remove(self):
        self.nm.add("a")
        self.nm.add("b")
        removed = self.nm.remove(0)
        self.assertEqual(removed, "a")
        self.assertEqual(self.nm.list(), ["b"])

    def test_persistence(self):
        self.nm.add("persist")
        # create new manager pointing at same file
        other = NotesManager(self.path)
        self.assertIn("persist", other.list())

if __name__ == '__main__':
    unittest.main()
