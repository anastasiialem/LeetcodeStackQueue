"""Module Implement Stack using Queues"""
class Node:
    """
    class Node
    """
    def __init__(self,data=None):
        """
        Function init 
        :param self: self param
        :param data: value
        """
        self.data = data
        self.next=None
class Queues:
    """
    class Queues
    >>> que=Queues()
    >>> que.is_empty()
    True
    """
    def __init__(self):
        """
        Fuction __init__
        :param self: self param
        >>> que=Queues()
        >>> que.is_empty()
        True
        """
        self.que=Node()
    def is_empty(self):
        """
        Function is  empty
        :param self: self param
        >>> que=Queues()
        >>> que.is_empty()
        True
        """
        if self.que is None:
            return True
        if self.que.data is None:
            return True
        return False
    def __len__(self):
        """
        Function  __len__
        :param self: self param
        >>> que=Queues()
        >>> len(que)
        0
        """
        if self.que is None:
            return 0
        if self.que.data is None:
            return 0
        i=1
        nod=self.que
        while nod.next is not None:
            i+=1
            nod=nod.next
        return i
    def push(self,x):
        """
        Function push
        :param self: self param
        :param x: element to push
        >>> que=Queues()
        >>> que.push(1)
        >>> len(que)
        1
        """
        head=self.que
        nod=head
        if head.data is None:
            self.que=Node(x)
        else:
            while nod.next is not None:
                nod=nod.next
            nod.next=Node(x)
            self.que=head
    def pop(self) -> int:
        """
        Fuction pop
        :param self: self param
        >>> que=Queues()
        >>> que.push(1)
        >>> len(que)
        1
        >>> que.pop()
        1
        >>> len(que)
        0
        """
        if not self.is_empty():
            nod=self.que
            self.que=self.que.next
            return nod.data
        return None
    def peek(self):
        """
        Function peek
        :param self: self param
        >>> que=Queues()
        >>> que.push(1)
        >>> que.push(2)
        >>> que.peek()
        1
        """
        if not self.is_empty():
            return self.que.data
        return None
class MyStack:
    """
    class my queue
    >>> obj=MyStack()
    >>> obj.push(1)
    >>> obj.push(2)
    >>> obj.top()
    2
    >>> obj.pop()
    2
    >>> obj.empty()
    False
    """
    def __init__(self):
        """
        Function __init__
        :param self: self param
        >>> obj=MyStack()
        """
        self.stack=Queues()
    def push(self, x: int) -> None:
        """
        Function push
        :param self: self param
        :param x: element to push
        """
        q=Queues()
        q.push(x)
        q0=self.stack
        q1=Queues()
        while not q0.is_empty():
            q1.push(q0.pop())
        while not q1.is_empty():
            q.push(q1.pop())
        self.stack=q
    def pop(self) -> int:
        """
        Fuction pop
        :param self: self param
        """
        return self.stack.pop()
    def top(self) -> int:
        """
        Function top
        :param self: self param
        """
        if not self.empty():
            return self.stack.peek()
        return None
    def empty(self) -> bool:
        """
        Function is  empty
        :param self: self param
        """
        return self.stack.is_empty()

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
