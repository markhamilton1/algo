import AlgoQueue


class Node(object):
    """
    Used to hold the data used by the BinaryTree class.
    """

    def __init__(self, data=None):
        """
        Construct a Node for a BinaryTree object.
        :param data: the data to put into the node
        """
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def clear(self):
        """
        Clear the links in the Node.
        """
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree(object):
    """
    Implements an ordered binary tree.
    """

    def __init__(self):
        """
        Construct a BinaryTree.
        """
        self._root = None

    def breadth_first_traverse(self, proc):
        """
        Perform a breadth first traversal of the tree applying the proc to each node.
        :param proc: a function pointer to apply to each node
        """
        q = AlgoQueue.Queue()
        if self._root is not None:
            q.push(self._root)
        while not q.is_empty():
            node = q.pop()
            proc(node.data)
            if node.left is not None:
                q.push(node.left)
            if node.right is not None:
                q.push(node.right)

    def clear(self):
        """
        Clear the binary tree.
        """
        self._root = None

    def count(self):
        """
        Determine the number of nodes in the tree.
        :return: the node count
        """

        def walk_tree(root):
            if root is None:
                return 0
            cnt = 1 + walk_tree(root.left) + walk_tree(root.right)
            return cnt

        cnt = walk_tree(self._root)
        return cnt

    def delete(self, data):
        """
        Search for a node containing the specified data and delete that node.
        :param data: the data to search for
        """
        if data is not None:
            fnode = self.find(data)
            if fnode is not None and fnode[0] == 0:
                self.remove_node(fnode[1])

    def depth_first_traverse(self, order, proc):
        """
        Perform a depth first traversal of the tree applying the proc to each node.
        :param order: 0=pre order, 1=in order, 2=post order
        :param proc: a function pointer to apply to each node
        """

        def traverse(node, order, proc):
            if order == 0:
                proc(node.data)
            if node.left is not None:
                traverse(node.left, order, proc)
            if order == 1:
                proc(node.data)
            if node.right is not None:
                traverse(node.right, order, proc)
            if order == 2:
                proc(node.data)

        if self._root is not None:
            traverse(self._root, order, proc)

    def find(self, data, root=None):
        """
        Find the node with the provided data or the node that would be its logical parent.
        :param data: the data to look for
        :param root: the starting root node
        :return: None=invalid root, (0=equals|1=greater|-1=less, node)
        """

        def search(root, data):
            if root.data == data:
                return 0, root
            if root.data > data:
                if root.left is None:
                    return 1, root
                return search(root.left, data)
            if root.right is None:
                return -1, root
            return search(root.right, data)

        if root is None:
            if self._root is None:
                return None
            return search(self._root, data)
        return search(root, data)

    def insert(self, data):
        """
        Insert the provided data into the tree (overwrite if already there).
        :param data: the data to insert
        """
        if data is not None:
            fnode = self.find(data)
            if fnode is None:
                self._root = Node(data)
            else:
                if fnode[0] == 1:
                    n = Node(data)
                    fnode[1].left = n
                    n.parent = fnode[1]
                elif fnode[0] == -1:
                    n = Node(data)
                    fnode[1].right = n
                    n.parent = fnode[1]
                else:
                    fnode[1].data = data

    def is_empty(self):
        """
        Test if the tree is empty.
        :return bool:   True=tree is empty, False=tree is not empty
        """
        return self._root is None

    def max_depth(self):
        """
        Get the maximum depth of the current tree.
        :return Int: the maximum depth of a leaf not in the tree
        """

        def walk_tree(root, depth):
            mxd = 0
            if root:
                depth += 1
                if root.left is not None:
                    mxd = walk_tree(root.left, depth)
                if root.right is not None:
                    mxd = walk_tree(root.right, depth)
                if depth > mxd:
                    mxd = depth
            return mxd

        mxd = walk_tree(self._root, 0)
        return mxd

    def optimal_depth(self):
        """
        Calculate the optimal depth of the tree for the number of elements it has.
        :return Int: the optimal depth for the current tree
        """
        cnt = self.count()
        olvl = 0
        while cnt > 0:
            olvl += 1
            cnt /= 2
        return olvl

    def remove_node(self, node):
        """
        Remove the specified node from the tree.
        :param node: the node to remove
        """
        if node.left is None:
            if node.parent is None:
                self._root = node.right
            else:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
        elif node.right is None:
            if node.parent is None:
                self._root = node.left
            else:
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
        elif node.left.right is None:
            node.left.right = node.right
            if node.parent is None:
                self._root = node.left
            elif node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        elif node.right.left is None:
            node.right.left = node.left
            if node.parent is None:
                self._root = node.right
            elif node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        else:
            if node.parent is None:
                sfnode = self.find(node.data, node.left)
                sfnode[1].right = node.right
                self._root = node.left
            elif node.parent.left == node:
                node.parent.left = node.left
                sfnode = self.find(node.data, node.left)
                sfnode[1].right = node.right
            elif node.parent.right == node:
                node.parent.right = node.left
                sfnode = self.find(node.data, node.left)
                sfnode[1].right = node.right
