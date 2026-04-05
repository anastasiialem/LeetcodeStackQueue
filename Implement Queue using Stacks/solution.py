"""Module Implement Queue using Stacks"""
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
class Stack:
    """
    class Stack
    >>> stack=Stack()
    >>> stack.is_empty()
    True
    """
    def __init__(self):
        """
        Fuction __init__
        :param self: self param
        >>> stack=Stack()
        >>> stack.is_empty()
        True
        """
        self.stack=Node()
    def is_empty(self):
        """
        Function is  empty
        :param self: self param
        >>> stack=Stack()
        >>> stack.is_empty()
        True
        """
        if self.stack.data is None:
            return True
        return False
    def __len__(self):
        """
        Function  __len__
        :param self: self param
        >>> stack=Stack()
        >>> len(stack)
        0
        """
        if self.stack.data is None:
            return 0
        i=0
        nod=self.stack
        while nod.next is not None:
            i+=1
            nod=nod.next
        return i
    def push(self,x):
        """
        Function push
        :param self: self param
        :param x: element to push
        >>> stack=Stack()
        >>> stack.push(1)
        >>> len(stack)
        1
        """
        nod=Node(x)
        nod.next=self.stack
        self.stack=nod
    def pop(self) -> int:
        """
        Fuction pop
        :param self: self param
        >>> stack=Stack()
        >>> stack.push(1)
        >>> len(stack)
        1
        >>> stack.pop()
        1
        >>> len(stack)
        0
        """
        if not self.is_empty():
            nod=self.stack
            self.stack=self.stack.next
            return nod.data
        return None
    def peek(self):
        """
        Function peek
        :param self: self param
        >>> stack=Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.peek()
        2
        """
        if not self.is_empty():
            return self.stack.data
        return None

class MyQueue:
    """
    class my queue
    >>> obj=MyQueue()
    >>> obj.push(1)
    >>> obj.push(2)
    >>> obj.peek()
    1
    >>> obj.pop()
    1
    >>> obj.empty()
    False
    """
    def __init__(self):
        """
        Function __init__
        :param self: self param
        >>> obj=MyQueue()
        """
        self.queue=Stack()
    def push(self, x: int) -> None:
        """
        Function push
        :param self: self param
        :param x: element to push
        """
        st0=self.queue
        st=Stack()
        st.push(x)
        st1=Stack()
        while not st0.is_empty():
            st1.push(st0.pop())
        while not st1.is_empty():
            st.push(st1.pop())
        self.queue=st
    def pop(self) -> int:
        """
        Fuction pop
        :param self: self param
        """
        return self.queue.pop()
    def peek(self) -> int:
        """
        Function peek
        :param self: self param
        """
        if not self.empty():
            return self.queue.peek()
        return None
    def empty(self) -> bool:
        """
        Function is  empty
        :param self: self param
        """
        return self.queue.is_empty()

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
