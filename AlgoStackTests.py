
import unittest
import AlgoStack


class Test_AlgoStack(unittest.TestCase):

    def setUp(self):
        self.stack = AlgoStack.Stack()

    def test_push(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 1)
        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 2)
        self.stack.push(3)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 3)
        self.stack.push(4)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 4)
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 5)

    def test_pop(self):
        self.test_push()
        d = self.stack.pop()
        self.assertEqual(d, 5)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 4)
        d = self.stack.pop()
        self.assertEqual(d, 4)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 3)
        d = self.stack.pop()
        self.assertEqual(d, 3)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 2)
        d = self.stack.pop()
        self.assertEqual(d, 2)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 1)
        d = self.stack.pop()
        self.assertEqual(d, 1)
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.count(), 0)

    def test_clear(self):
        self.test_push()
        self.stack.clear()
        self.assertEqual(self.stack.count(), 0)

    def test_push_objects(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push([1,2,3])
        self.assertEqual(self.stack.count(), 1)
        self.stack.push({"a":1, "b":2, "c":3})
        self.assertEqual(self.stack.count(), 2)

    def test_pop_objects(self):
        self.test_push_objects()
        e = self.stack.pop()
        self.assertEqual(self.stack.count(), 1)
        self.assertEqual(len(e), 3)
        self.assertEqual(e["a"], 1)
        self.assertEqual(e["b"], 2)
        self.assertEqual(e["c"], 3)
        e = self.stack.pop()
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(len(e), 3)
        self.assertEqual(e[0], 1)
        self.assertEqual(e[1], 2)
        self.assertEqual(e[2], 3)


if __name__ == "__main__":


    unittest.main()
