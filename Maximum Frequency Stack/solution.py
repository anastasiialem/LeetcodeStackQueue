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
    def push(self, val: int) -> None:
        """
        Function push
        :param self: self param
        :param val: value to push
        """
        nod=self.deq
        nod0=Node(val)
        nod0.next=nod
        self.deq=nod0
    @staticmethod
    def frequancy(head):
        """
        Returns nodes frequancy
        :param head: head to start
        """
        new_head=Node()
        hd=new_head
        while head is not None:
            prob=hd
            k=0
            while prob.next is not None:
                if prob.next.data==head.data:
                    prob.next.frequance+=1
                    k=1
                    break
                prob=prob.next
            if k==0:
                prob.next=Node(head.data,1)
            head=head.next
            k=0
        ll=Node()
        i=0
        prob=hd.next
        while prob is not None:
            if prob.frequance>i:
                i=prob.frequance
                ll=Node(prob.data)
            prob=prob.next
        return ll.data
    def pop(self) -> int:
        """
        Function pop
        :param self: self param
        """
        if self.deq is None or self.deq.data is None:
            return None
        ll=self.frequancy(self.deq)
        if self.deq.data==ll:
            nod=self.deq
            self.deq=self.deq.next
            return nod.data
        prob=self.deq
        while prob.next is not None:
            if prob.next.data==ll:
                nod=prob.next
                prob.next=prob.next.next
                return nod.data
            prob=prob.next
        return None
        # head=self.deq
        # prob=head
        # nod=Node()
        # while prob.next is not None:
        #     if prob.next.data==ll:
        #         nod=Node(prob.next.data)
        #         prob.next=prob.next.next
        #         break
        #     prob=prob.next
        # return nod.data

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
