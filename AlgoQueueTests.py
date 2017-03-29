
import unittest
import AlgoQueue


class Test_AlgoQueue(unittest.TestCase):

    def setUp(self):
        self.queue = AlgoQueue.Queue()

    def test_push(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.push(1)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 1)
        self.queue.push(2)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 2)
        self.queue.push(3)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 3)
        self.queue.push(4)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 4)
        self.queue.push(5)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 5)

    def test_pop(self):
        self.test_push()
        d = self.queue.pop()
        self.assertEqual(d, 1)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 4)
        d = self.queue.pop()
        self.assertEqual(d, 2)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 3)
        d = self.queue.pop()
        self.assertEqual(d, 3)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 2)
        d = self.queue.pop()
        self.assertEqual(d, 4)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 1)
        d = self.queue.pop()
        self.assertEqual(d, 5)
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 0)

    def test_clear(self):
        self.test_push()
        self.queue.clear()
        self.assertEqual(self.queue.count(), 0)

    def test_push_objects(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.push([1,2,3])
        self.assertEqual(self.queue.count(), 1)
        self.queue.push({"a":1, "b":2, "c":3})
        self.assertEqual(self.queue.count(), 2)

    def test_pop_objects(self):
        self.test_push_objects()
        e = self.queue.pop()
        self.assertEqual(len(e), 3)
        self.assertEqual(e[0], 1)
        self.assertEqual(e[1], 2)
        self.assertEqual(e[2], 3)
        e = self.queue.pop()
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.count(), 0)
        self.assertEqual(len(e), 3)
        self.assertEqual(e["a"], 1)
        self.assertEqual(e["b"], 2)
        self.assertEqual(e["c"], 3)


if __name__ == "__main__":


    unittest.main()
