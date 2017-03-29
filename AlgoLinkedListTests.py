
import unittest
import AlgoLinkedList


class Test_LinkedList(unittest.TestCase):

    def setUp(self):
        pass

    def test_list_new(self):
        s = (1, 2, 3, 4, 5, 6)
        self.llist = AlgoLinkedList.LinkedList(s)
        # test initial length
        self.assertEqual(self.llist.count(), 6)

    def test_list_at(self):
        self.test_list_new()
        # test at
        n = self.llist.at(0)
        self.assertEqual(n.data, 1)
        n = self.llist.at(1)
        self.assertEqual(n.data, 2)
        n = self.llist.at(2)
        self.assertEqual(n.data, 3)
        n = self.llist.at(3)
        self.assertEqual(n.data, 4)
        n = self.llist.at(4)
        self.assertEqual(n.data, 5)
        n = self.llist.at(5)
        self.assertEqual(n.data, 6)

    def test_list_iterator(self):
        self.test_list_new()
        # test iterator
        i = self.llist.__iter__()
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 1)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 2)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 3)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 4)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 5)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 6)
        self.assertFalse(i.has_more())

    def test_list_append(self):
        self.test_list_new()
        # append 3 more nodes
        self.llist.append(AlgoLinkedList.Node(7))
        self.llist.append(AlgoLinkedList.Node(8))
        self.llist.append(AlgoLinkedList.Node(9))
        # test new length
        self.assertEqual(self.llist.count(), 9)
        # test iterator
        i = self.llist.__iter__()
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 1)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 2)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 3)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 4)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 5)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 6)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 7)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 8)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 9)
        self.assertFalse(i.has_more())

    def test_list_insert(self):
        self.test_list_new()
        # insert 3 more nodes
        self.llist.insert(0, AlgoLinkedList.Node(7))
        self.llist.insert(1, AlgoLinkedList.Node(8))
        self.llist.insert(2, AlgoLinkedList.Node(9))
        # test new length
        self.assertEqual(self.llist.count(), 9)
        # test iterator
        i = self.llist.__iter__()
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 7)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 8)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 9)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 1)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 2)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 3)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 4)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 5)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 6)
        self.assertFalse(i.has_more())

    def test_list_extend(self):
        self.test_list_new()
        # extend with 3 more nodes
        e = (7, 8, 9)
        self.llist.extend(e)
        # test iterator
        i = self.llist.__iter__()
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 1)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 2)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 3)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 4)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 5)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 6)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 7)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 8)
        self.assertTrue(i.has_more())
        n = i.next()
        self.assertEqual(n.data, 9)
        self.assertFalse(i.has_more())

    def test_list_indexing(self):
        self.test_list_new()
        # test indexing
        n = self.llist[0]
        self.assertEqual(n.data, 1)
        n = self.llist[1]
        self.assertEqual(n.data, 2)
        n = self.llist[2]
        self.assertEqual(n.data, 3)
        n = self.llist[3]
        self.assertEqual(n.data, 4)
        n = self.llist[4]
        self.assertEqual(n.data, 5)
        n = self.llist[5]
        self.assertEqual(n.data, 6)

    def test_list_pop(self):
        self.test_list_new()
        # test pop
        n = self.llist.take()
        self.assertEqual(n.data, 6)
        self.assertEqual(self.llist.count(), 5)
        n = self.llist.take()
        self.assertEqual(n.data, 5)
        self.assertEqual(self.llist.count(), 4)
        n = self.llist.take()
        self.assertEqual(n.data, 4)
        self.assertEqual(self.llist.count(), 3)
        n = self.llist.take()
        self.assertEqual(n.data, 3)
        self.assertEqual(self.llist.count(), 2)
        n = self.llist.take()
        self.assertEqual(n.data, 2)
        self.assertEqual(self.llist.count(), 1)
        n = self.llist.take()
        self.assertEqual(n.data, 1)
        self.assertEqual(self.llist.count(), 0)

    def test_list_reverse(self):
        self.test_list_new()
        # test reverse
        self.llist.reverse()
        self.assertEqual(self.llist.count(), 6)
        # test indexing
        n = self.llist[0]
        self.assertEqual(n.data, 6)
        n = self.llist[1]
        self.assertEqual(n.data, 5)
        n = self.llist[2]
        self.assertEqual(n.data, 4)
        n = self.llist[3]
        self.assertEqual(n.data, 3)
        n = self.llist[4]
        self.assertEqual(n.data, 2)
        n = self.llist[5]
        self.assertEqual(n.data, 1)

    def test_list_clear(self):
        self.test_list_new()
        # test clear
        self.llist.clear()
        self.assertEqual(self.llist.count(), 0)

    def test_stack_push(self):
        self.stack = AlgoLinkedList.Stack()
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

    def test_stack_pop(self):
        self.test_stack_push()
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

    def test_stack_clear(self):
        self.test_stack_push()
        self.stack.clear()
        self.assertEqual(self.stack.count(), 0)

    def test_stack_push_objects(self):
        self.stack = AlgoLinkedList.Stack()
        self.assertTrue(self.stack.is_empty())
        self.stack.push([1,2,3])
        self.assertEqual(self.stack.count(), 1)
        self.stack.push({"a":1, "b":2, "c":3})
        self.assertEqual(self.stack.count(), 2)

    def test_stack_pop_objects(self):
        self.test_stack_push_objects()
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

    def test_queue_push(self):
        self.queue = AlgoLinkedList.Queue()
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

    def test_queue_pop(self):
        self.test_queue_push()
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

    def test_queue_clear(self):
        self.test_queue_push()
        self.queue.clear()
        self.assertEqual(self.queue.count(), 0)

    def test_queue_push_objects(self):
        self.queue = AlgoLinkedList.Queue()
        self.assertTrue(self.queue.is_empty())
        self.queue.push([1,2,3])
        self.assertEqual(self.queue.count(), 1)
        self.queue.push({"a":1, "b":2, "c":3})
        self.assertEqual(self.queue.count(), 2)

    def test_queue_pop_objects(self):
        self.test_queue_push_objects()
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
