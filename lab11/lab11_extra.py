# Extra Questions

from lab11 import *

# Q6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while True:
        yield n
        if n == 1:
            break
        elif n % 2 == 0:
            n = n //2
        else:
            n = 3 * n + 1      

# Q7
def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1, 'repeated at least 2 times'
    "*** YOUR CODE HERE ***"
    count = 1    #defined to count the repeated times
    t = iter(t)  #transfer the iterable t into an iterator
    prev = next(t)  #initial value

    while count < k:
        current = next(t)
        if prev == current:
            count += 1
        else:
            count = 1
        prev = current

    return current


# Q8
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. You can also assume that s0
    and s1 represent infinite sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0, None), next(i1, None)
    "*** YOUR CODE HERE ***"
    while e0 is not None or e1 is not None:

        if e0 == None:  # consider the case that e0 or e1 is None []
            t = e1
            e1 = next(i1, None)
        elif e1 == None:
            t = e0
            e0 = next(i0,None)

        else:  # consier the case neither of e0 or e1 is None
            if e0< e1:
                t= e0
                e0 = next(i0,None)
            elif e0 == e1:
                t = e0
                e0, e1 = next(i0, None), next(i1, None)
            elif e0 > e1:
                t= e1
                e1 = next(i1, None)

        yield t

# Q9
def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def generator(n):
        k = 0
        while True:
            yield m * k +n
            k += 1

    return [generator(n) for n in range(m)]  # list of generators


# Q10
def zip_generator(*iterables):
    """
    Takes in any number of iterables and zips them together.
    Returns a generator that outputs a series of lists, each
    containing the nth items of each iterable.
    >>> z = zip_generator([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    "*** YOUR CODE HERE ***"
    num = min([len(element) for element in iterables])  # number of lists[]
    length = len(iterables)   # length of each list

    for i in range(num):
            yield [element[i] for element in iterables]  # combine the ith number of each element in iterables.
            i += 1
    
    #official solution
    """
    iterator = iter(zip(*iterables))
    for _ in range(len(list(zip(*iterables)))):
        yield list(next(iterator))

    """

