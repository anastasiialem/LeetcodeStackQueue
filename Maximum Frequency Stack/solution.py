"""Module Maximum Frequency Stack"""
class Node:
    """
    class Node
    """
    def __init__(self,data=None,fr=0):
        """
        Function init 
        :param self: self param
        :param data: value
        """
        self.data = data
        self.next=None
        self.frequance=fr
class FreqStack:
    """
    Class FreqStack
    >>> freqStack=FreqStack()
    >>> freqStack.push(5)
    >>> freqStack.push(7)
    >>> freqStack.push(5)
    >>> freqStack.push(7)
    >>> freqStack.push(4)
    >>> freqStack.push(5)
    >>> freqStack.pop()
    5
    >>> freqStack.pop()
    7
    >>> freqStack.pop()
    5
    >>> freqStack.pop()
    4
    >>> freqStack.pop()
    7
    >>> freqStack.pop()
    5
    """
    def __init__(self):
        """
        Function __init__
        :param self: self param
        """
        self.deq=None
        self.freq={}
    def push(self, val: int) -> None:
        """
        Function push
        :param self: self param
        :param val: value to push
        """
        nod0=Node(val)
        nod0.next=self.deq
        self.deq=nod0
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
    def frequancy(self):
        """
        Returns nodes frequancy
        :param head: head to start
        """
        return max(self.freq.values())
    def pop(self) -> int:
        """
        Function pop
        :param self: self param
        """
        if self.deq is None or self.deq.data is None:
            return None
        ll=self.frequancy()
        if self.freq[self.deq.data]==ll:
            nod=self.deq
            self.deq=self.deq.next
            self.freq[nod.data]-=1
            if self.freq[nod.data]==0:
                del self.freq[nod.data]
            return nod.data
        prob=self.deq
        while prob.next is not None:
            if self.freq[prob.next.data]==ll:
                nod=prob.next
                prob.next=prob.next.next
                self.freq[nod.data] -= 1
                if self.freq[nod.data] == 0:
                    del self.freq[nod.data]
                return nod.data
            prob=prob.next
        return None

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
