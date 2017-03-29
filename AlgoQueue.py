
class Element(object):
    """
    Used to hold a data item in the Queue.
    """

    def __init__(self, data, prev):
        """
        Construct a new Element for the Queue.
        :param data: the data to add to the Queue
        :param prev: the previous Element in the Queue
        """
        self.data = data
        self.prev = prev


class Queue(object):
    """
    Implements a Queue.
    """

    def __init__(self):
        """
        Construct a new Queue.
        """
        self._in = None
        self._out = None
        self._cnt = 0

    def clear(self):
        """
        Clear the contents of the Queue.
        """
        self._in = None
        self._out = None
        self._cnt = 0

    def count(self):
        """
        Get the number of items in the Queue.
        :return: the number of items in the Queue
        """
        return self._cnt

    def is_empty(self):
        """
        Test if the Queue is empty.
        :return: True=Queue is empty, False=Queue has Elements
        """
        return self._out is None

    def pop(self):
        """
        Pop an Element from the Queue and return the data that it contains.
        :return: the data from the out Element (None if no out Element)
        """
        d = None
        if self._out is not None:
            d = self._out.data
            self._out = self._out.prev
            self._cnt -= 1
        if self._out is None:
            self._in = None
        return d

    def push(self, data=None):
        """
        Push the provided data into the Queue.
        :param data: the data to push into the Queue
        """
        t = Element(data, None)
        if self._in is None:
            self._in = t
            self._out = self._in
        else:
            self._in.prev = t
            self._in = t
        self._cnt += 1