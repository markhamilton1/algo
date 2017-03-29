
class Element(object):
    """
    Used to hold a data item on the Stack.
    """

    def __init__(self, data, next):
        """
        Construct a new Element for the Stack.
        :param data: the data to push onto the Stack
        :param next: the next Element on the stack
        """
        self.data = data
        self.next = next


class Stack(object):
    """
    Implements a Stack.
    """

    def __init__(self):
        """
        Construct a new Stack.
        """
        self._top = None
        self._cnt = 0

    def clear(self):
        """
        Clear the contents of the Stack.
        """
        self._top = None
        self._cnt = 0

    def count(self):
        """
        Get the number of items on the Stack.
        :return:    the number of items in the Stack
        """
        return self._cnt

    def is_empty(self):
        """
        Test if the Stack is empty.
        :return: True=Stack is empty, False=Stack has Elements
        """
        return self._top is None

    def pop(self):
        """
        Pop the top Element off the Stack and return the data that it contains.
        :return: the data from the top Element (None if no top Element)
        """
        d = None
        if self._top is not None:
            d = self._top.data
            self._top = self._top.next
            self._cnt -= 1
        return d

    def push(self, data=None):
        """
        Push the provided data onto the Stack.
        :param data: the data to push onto the Stack
        """
        t = self._top
        self._top = Element(data, t)
        self._cnt += 1