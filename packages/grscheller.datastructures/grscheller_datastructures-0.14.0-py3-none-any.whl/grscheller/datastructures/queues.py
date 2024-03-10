# Copyright 2023-2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Queue based datastructures.

* stateful queue data structures with amortized O(1) pushes and pops
* obtaining length (number of elements) of a queue is an O(1) operation
* implemented with Python List based circular array in a "has-a" relationship
* these data structures will resize themselves as needed
* these queues are O(1) indexible, convenient but ignorable feature
* Python's `None` is not stored in these data structures as a value

Types of Queues:

* class **FIFOQueue**: First In, First Out Queue
* class **LIFOQueue**: Last In, First Out Queue
* class **DoubleQueue**: Double Ended Queue
"""

from __future__ import annotations

__all__ = ['DoubleQueue', 'FIFOQueue', 'LIFOQueue']
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

from typing import Any, Callable
from .core.fp import FP
from grscheller.circular_array import CircularArray

class QueueBase():
    """Abstract base class for stateful queue-based data structures

    * primarily for DRY implementation inheritance of queue type classes
    * derived classes used will resize themselves as needed
    * each queue object "has-a" (contains) a circular array to store its data
    * None is not stored as a value on Queue data structures
    """
    __slots__ = '_ca',

    def __init__(self, *ds):
        """Construct a queue data structure. Cull None values."""
        self._ca = CircularArray()
        for d in ds:
            if d is not None:
                self._ca.pushR(d)

    def __iter__(self):
        """Iterator yielding data currently stored in queue. Data yielded in
        natural FIFO order.
        """
        cached = self._ca.copy()
        for pos in range(len(cached)):
            yield cached[pos]

    def __reversed__(self):
        """Reverse iterate over the current state of the queue."""
        cached = self._ca.copy()
        for pos in range(len(cached)-1, -1, -1):
            yield cached[pos]

    def __repr__(self):
        return f'{self.__class__.__name__}(' + ', '.join(map(repr, self)) + ')'

    def __bool__(self):
        """Returns true if queue is not empty."""
        return len(self._ca) > 0

    def __len__(self):
        """Returns current number of values in queue."""
        return len(self._ca)

    def __eq__(self, other):
        """Returns True if all the data stored in both compare as equal.
        Worst case is O(n) behavior for the true case.
        """
        if not isinstance(other, type(self)):
            return False
        return self._ca == other._ca

    def map(self, f: Callable[[Any], Any]) -> None:
        """Apply function over the queue's contents. Suppress any None values
        returned by f.
        """
        self._ca = QueueBase(*map(f, self))._ca

    def reverse(self):
        """Reverse the elements in the Queue"""
        self._ca = self._ca.reverse()

    def __getitem__(self, index: int) -> Any:
        cnt = len(self)
        if -cnt <= index < cnt:
            return self._ca[index]
        else:
            return None

    def __setitem__(self, index: int, value):
        typePath = 'grscheller.datastructures.queues.'
        queueType = lambda queue: str(type(queue)).split(typePath)[-1].partition("'")[0]

        cnt = len(self)
        if -cnt <= index < cnt:
            if value is not None:
                self._ca[index] = value
            else:
                msg = f'None values are not allowed in {queueType(self)} queues.'
                raise ValueError(msg)
        else:
            if cnt > 0:
                msg1 = f'Out of bounds: '
                msg2 = f'index = {index} not from {-cnt} to {cnt-1} '
                msg3 = f'while setting value from a {queueType(self)}.'
                raise IndexError(msg1 + msg2 + msg3)
            else:
                msg0 = f'Trying to set value from an empty {queueType(self)}.'
                raise IndexError(msg0)

class FIFOQueue(QueueBase, FP):
    """Stateful single sided FIFO data structure. Will resize itself as needed. `None`
    represents the absence of a value and ignored if pushed onto the queue.
    """
    __slots__ = ()

    def __str__(self):
        return "<< " + " < ".join(map(str, self)) + " <<"

    def copy(self) -> FIFOQueue:
        """Return shallow copy of the FIFOQueue in O(n) time & space complexity."""
        fifoqueue = FIFOQueue()
        fifoqueue._ca = self._ca.copy()
        return fifoqueue

    def push(self, *ds: Any) -> None:
        """Push data on rear of the FIFOQueue & no return value."""
        for d in ds:
            if d != None:
                self._ca.pushR(d)

    def pop(self) -> Any:
        """Pop data off front of the FIFOQueue."""
        return self._ca.popL()

    def peakLastIn(self) -> Any:
        """Return last element pushed to the FIFOQueue without consuming it"""
        if self._ca:
            return self._ca[-1]
        else:
            return None

    def peakNextOut(self) -> Any:
        """Return next element ready to pop from the FIFOQueue."""
        if self._ca:
            return self._ca[0]
        else:
            return None

class LIFOQueue(QueueBase, FP):
    """Stateful single sided LIFO data structure. Will resize itself as needed. `None`
    represents the absence of a value and ignored if pushed onto the queue.
    """
    __slots__ = ()

    def __str__(self):
        return "|| " + " > ".join(map(str, self)) + " ><"

    def copy(self) -> LIFOQueue:
        """Return shallow copy of the FIFOQueue in O(n) time & space complexity."""
        lifoqueue = LIFOQueue()
        lifoqueue._ca = self._ca.copy()
        return lifoqueue

    def push(self, *ds: Any) -> None:
        """Push data on rear of the LIFOQueue & no return value."""
        for d in ds:
            if d != None:
                self._ca.pushR(d)

    def pop(self) -> Any:
        """Pop data off rear of the LIFOQueue."""
        return self._ca.popR()

    def peak(self) -> Any:
        """Return last element pushed to the LIFOQueue without consuming it."""
        if self._ca:
            return self._ca[-1]
        else:
            return None

class DoubleQueue(QueueBase, FP):
    """Stateful double sided queue datastructure. Will resize itself as needed. `None`
    represents the absence of a value and ignored if pushed onto the queue.
    """
    __slots__ = ()

    def __str__(self):
        return ">< " + " | ".join(map(str, self)) + " ><"

    def copy(self) -> DoubleQueue:
        """Return shallow copy of the DoubleQueue in O(n) time & space complexity."""
        dqueue = DoubleQueue()
        dqueue._ca = self._ca.copy()
        return dqueue

    def pushR(self, *ds: Any) -> None:
        """Push data left to right onto rear of the DoubleQueue."""
        for d in ds:
            if d != None:
                self._ca.pushR(d)

    def pushL(self, *ds: Any) -> None:
        """Push data left to right onto front of DoubleQueue."""
        for d in ds:
            if d != None:
                self._ca.pushL(d)

    def popR(self) -> Any:
        """Pop data off rear of the DoubleQueue."""
        return self._ca.popR()

    def popL(self) -> Any:
        """Pop data off front of the DoubleQueue."""
        return self._ca.popL()

    def peakR(self) -> Any:
        """Return right-most element of the DoubleQueue if it exists."""
        if self._ca:
            return self._ca[-1]
        else:
            return None

    def peakL(self) -> Any:
        """Return left-most element of the DoubleQueue if it exists."""
        if self._ca:
            return self._ca[0]
        else:
            return None
