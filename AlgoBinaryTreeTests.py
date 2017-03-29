
import unittest
import AlgoBinaryTree


class Test_BinaryTree(unittest.TestCase):

    def setUp(self):
        pass

    def test_tree_new(self):
        self.btree = AlgoBinaryTree.BinaryTree()
        self.assertIsNotNone(self.btree)
        self.assertTrue(self.btree.is_empty())
        self.assertEqual(0, self.btree.optimal_depth())

    def test_tree_insert(self):
        self.test_tree_new()
        self.btree.insert(11)
        self.assertEqual(1, self.btree.optimal_depth())
        self.btree.insert(6)
        self.assertEqual(2, self.btree.optimal_depth())
        self.btree.insert(8)
        self.assertEqual(2, self.btree.optimal_depth())
        self.btree.insert(7)
        self.assertEqual(3, self.btree.optimal_depth())
        self.btree.insert(19)
        self.assertEqual(3, self.btree.optimal_depth())
        self.btree.insert(4)
        self.assertEqual(3, self.btree.optimal_depth())
        self.btree.insert(10)
        self.assertEqual(3, self.btree.optimal_depth())
        self.btree.insert(5)
        self.assertEqual(4, self.btree.optimal_depth())
        self.btree.insert(17)
        self.assertEqual(4, self.btree.optimal_depth())
        self.btree.insert(43)
        self.assertEqual(4, self.btree.optimal_depth())
        self.btree.insert(49)
        self.assertEqual(4, self.btree.optimal_depth())
        self.btree.insert(31)
        self.assertEqual(4, self.btree.optimal_depth())
        self.btree.insert(1)
        self.assertEqual(4, self.btree.optimal_depth())
        self.assertEqual(13, self.btree.count())
        self.assertEqual(4, self.btree.max_depth())
        self.assertEqual(4, self.btree.optimal_depth())

    def test_tree_preorder_traversal(self):

        def proc(d):
            data.append(d)

        self.test_tree_insert()
        data = []
        self.btree.depth_first_traverse(0, proc)
        t = (11, 6, 4, 1, 5, 8, 7, 10, 19, 17, 43, 31, 49)
        self.assertTupleEqual(t, tuple(data))

    def test_tree_inorder_traversal(self):

        def proc(d):
            data.append(d)

        self.test_tree_insert()
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 4, 5, 6, 7, 8, 10, 11, 17, 19, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))


    def test_tree_postorder_traversal(self):

        def proc(d):
            data.append(d)

        self.test_tree_insert()
        data = []
        self.btree.depth_first_traverse(2, proc)
        t = (1, 5, 4, 7, 10, 8, 6, 17, 31, 49, 43, 19, 11)
        self.assertTupleEqual(t, tuple(data))

    def test_tree_breadth_first_traversal(self):

        def proc(d):
            data.append(d)

        self.test_tree_insert()
        data = []
        self.btree.breadth_first_traverse(proc)
        t = (11, 6, 19, 4, 8, 17, 43, 1, 5, 7, 10, 31, 49)
        self.assertTupleEqual(t, tuple(data))

    def test_tree_delete(self):

        def proc(d):
            data.append(d)

        self.test_tree_insert()
        self.btree.delete(1)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (4, 5, 6, 7, 8, 10, 11, 17, 19, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))

        self.test_tree_insert()
        self.btree.delete(4)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 5, 6, 7, 8, 10, 11, 17, 19, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))

        self.test_tree_insert()
        self.btree.delete(10)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 4, 5, 6, 7, 8, 11, 17, 19, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))

        self.test_tree_insert()
        self.btree.delete(8)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 4, 5, 6, 7, 10, 11, 17, 19, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))

        self.test_tree_insert()
        self.btree.delete(17)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 4, 5, 6, 7, 8, 10, 11, 19, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))

        self.test_tree_insert()
        self.btree.delete(19)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 4, 5, 6, 7, 8, 10, 11, 17, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))

        self.test_tree_insert()
        self.btree.delete(43)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 4, 5, 6, 7, 8, 10, 11, 17, 19, 31, 49)
        self.assertTupleEqual(t, tuple(data))

        self.test_tree_insert()
        self.btree.delete(6)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 4, 5, 7, 8, 10, 11, 17, 19, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))

        self.test_tree_insert()
        self.btree.delete(11)
        data = []
        self.btree.depth_first_traverse(1, proc)
        t = (1, 4, 5, 6, 7, 8, 10, 17, 19, 31, 43, 49)
        self.assertTupleEqual(t, tuple(data))

if __name__ == "__main__":


    unittest.main()
