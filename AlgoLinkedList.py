import types


class Node(object):
    """
    Used to hold the data used by the LinkedList class.
    """

    def __init__(self, data=None, prev=None, next=None):
        """
        Construct a Node for a LinkedList object.
        :param data: the data to put in the node
        :param Node prev:   the previous Node
        :param Node next:   the next Node
        """
        self.data = data
        self.prev = prev
        self.next = next

    def is_linked(self):
        """
        Test if the Node has links.
        :return bool:    True=has links, False=does not have links
        """
        return self.prev is not None or self.next is not None


class LinkedListIterator:
    """
    Used to iterate a LinkedList object.
    """

    def __init__(self, llist):
        """
        Construct a LinkedListIterator.
        :param LinkedList llist: the LinkedList to iterate
        """
        self._llist = llist
        self._currentNode = llist.first()

    def has_more(self):
        """
        Test if there are more Nodes for the iterator.
        :return bool: True=there is at least one more Node, False=there is not another Node
        """
        return self._currentNode is not None

    def next(self):
        """
        Get the next Node from the iterator.
        :return Node: the next Node
        """
        if self._currentNode is not None:
            node = self._currentNode
            if node is not None:
                self._currentNode = node.next
            else:
                self._currentNode = None
            return node
        raise StopIteration()


class LinkedList(object):
    """
    Implements a linked list.
    """

    def __init__(self, s=None):
        """
        Construct a LinkedList.
        :param list s: a sequence to initialize the LinkedList with
        """
        self._root = None
        self._tail = None
        self._cnt = 0
        if s is not None:
            self.extend(s)

    def __getitem__(self, key):
        """
        Get the item at the provided index.
        :param int key: the key at which to get the object
        :return Node:   the object at the index
        """
        if isinstance(key, slice):
            raise TypeError, "Not currently supported!"
        elif isinstance(key, int):
            return self.at(key)
        raise TypeError, "Invalid argument type!"

    def __iter__(self):
        """
        Allocate an iterator for this LinkedList.
        :return LinkedListIterator: a LinkedListIterator
        """
        return LinkedListIterator(self)

    def append(self, node):
        """
        Append a Node to the LinkedList.
        :param Node node: the Node to append
        """
        if node is not None and not node.is_linked():
            if self._tail is None:
                self._root = node
                self._tail = node
            else:
                node.prev = self._tail
                self._tail.next = node
                self._tail = node
            self._cnt += 1
        else:
            raise ValueError, "Invalid Node! Must not be None and must not be linked."

    def at(self, idx):
        """
        Get the Node at the provided index.
        :param int idx: the index of the Node to get
        :return Node:   the Node (None if nothing at that index)
        """
        if idx < 0:
            t = self._tail
            idx += 1
            while t is not None and idx < 0:
                t = t.prev
                idx += 1
        else:
            t = self._root
            while t is not None and idx > 0:
                t = t.next
                idx -= 1
        return t

    def clear(self):
        """
        Clear the LinkedList.
        """
        self._root = None
        self._tail = None
        self._cnt = 0

    def count(self):
        """
        Get the number of Nodes in the LinkedList.
        :return int:    the count
        """
        return self._cnt

    def extend(self, s):
        """
        Extend the LinkedList by adding the objects in the sequence.
        :param list s:   the sequence of objects to add
        """
        if s is not None:
            if isinstance(s, types.ListType):
                for t in s:
                    self.append(Node(t))
            elif isinstance(s, types.TupleType):
                for t in s:
                    self.append(Node(t))
            else:
                raise TypeError

    def first(self):
        """
        Get the first Node in the LinkedList.
        :return Node:    the first Node
        """
        return self._root

    def insert(self, idx, node):
        """
        Insert the provided Node into the LinkedList at the specified index.
        :param int idx:     the index at which to insert the Node
        :param Node node:   the Node to insert
        """
        if node is not None and not node.is_linked():
            t = self.at(idx)
            if t is None:
                if idx == 0 or idx == -1:
                    self._root = node
                    self._tail = node
                else:
                    raise IndexError
            else:
                if t.prev is None:
                    self._root = node
                else:
                    t.prev.next = node
                node.next = t
                node.prev = t.prev
                t.prev = node
            self._cnt += 1
        else:
            raise ValueError, "Invalid Node! Must not be None and must not be linked."

    def is_empty(self):
        """
        Test if the list is empty.
        :return bool:    True=list is empty, False=list is not empty
        """
        return self._root is None

    def last(self):
        """
        Get the last Node in the LinkedList.
        :return Node:    the last Node
        """
        return self._tail

    def take(self, idx=-1):
        """
        Take the Node at the index out of the LinkedList.
        :param int idx: the index to use
        :return Node:    the Node (None if not found)
        """
        t = self.at(idx)
        self.remove(t)
        return t

    def remove(self, node):
        """
        Remove the Node from the LinkedList.
        :param Node node:    the Node to remove
        """
        if node is not None:
            if node.prev is None:
                self._root = node.next
            else:
                node.prev.next = node.next
            if node.next is None:
                self._tail = node.prev
            else:
                node.next.prev = node.prev
            self._cnt -= 1
            node.prev = None
            node.next = None

    def reverse(self):
        """
        Reverse the order of the Nodes in the LinkedList.
        """
        # n is the next Node to process
        # p is the last Node processed
        # t is the Node following the next Node (i.e. memory)
        # get the root Node as a starting point
        n = self._root
        # set the tail Node
        self._tail = n
        # initialize the processed list to None
        p = None
        # while there is another Node to process...
        while n is not None:
            # remember the Node that follows the current one
            t = n.next
            # set the next reference of the current Node to the previous processed Node
            # this is why we needed to save the next Node to t, or it would have been lost
            n.next = p
            # if ther was a previous Node...
            if p is not None:
                # set the prev reference of the previous Node to the current Node
                p.prev = n
            # set the prev reference of the current Node to None
            n.prev = None
            # set the previous processed variable to the current Node
            p = n
            # set the root of the LinkedList to the current Node
            self._root = p
            # set the following Node to be the next Node to process
            n = t


class Stack(LinkedList):
    """
    Implements a Stack.
    """

    def __init__(self):
        """
        Construct a new Stack.
        """
        LinkedList.__init__(self)

    def clear(self):
        """
        Clear the contents of the Stack.
        """
        LinkedList.clear(self)

    def count(self):
        """
        Get the number of items on the Stack.
        :return int:    the number of items on the Stack
        """
        return LinkedList.count(self)

    def is_empty(self):
        """
        Test if the Stack is empty.
        :return bool:    True=Stack is empty, False=Stack has Elements
        """
        return LinkedList.is_empty(self)

    def pop(self):
        """
        Pop the top Element off the Stack and return the data that it contains.
        :return:    the data from the top Element (None if no top Element)
        """
        n = LinkedList.take(self)
        if n is not None:
            return n.data
        return None

    def push(self, data=None):
        """
        Push the provided data onto the Stack.
        :param data:    the data to push onto the Stack
        """
        LinkedList.append(self, Node(data))


class Queue(LinkedList):
    """
    Implements a Queue.
    """

    def __init__(self):
        """
        Construct a new Queue.
        """
        LinkedList.__init__(self)

    def clear(self):
        """
        Clear the contents of the Queue.
        """
        LinkedList.clear(self)

    def count(self):
        """
        Get the number of items in the Queue.
        :return int:    the number of items in the Queue
        """
        return LinkedList.count(self)

    def is_empty(self):
        """
        Test if the Queue is empty.
        :return bool:    True=Queue is empty, False=Queue has Elements
        """
        return LinkedList.is_empty(self)

    def pop(self):
        """
        Pop an Element from the Queue and return the data that it contains.
        :return:    the data from the out Element (None if no out Element)
        """
        n = LinkedList.take(self, 0)
        if n is not None:
            return n.data
        return None

    def push(self, data=None):
        """
        Push the provided data into the Queue.
        :param data:    the data to push into the Queue
        """
        LinkedList.append(self, Node(data))