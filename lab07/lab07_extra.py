from lab07 import *

# Q6
def cumulative_sum(t):
    """Mutates t where each node's root becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        pass
    for b in t.branches:
        cumulative_sum(b)
    t.label = t.label + sum([b.label for b in t.branches]) 
    

# Q7
def reverse_other(t):
    """Reverse the entries of every other level of the tree using mutation.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(5, [Tree(7), Tree(8)]), Tree(6)]), Tree(3)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5, [Tree(8), Tree(7)]), Tree(6)]), Tree(2)])
    """
    "*** YOUR CODE HERE ***" #official solution
    def reverse_helper(t, need_reverse):
        if t.is_leaf():
            return
        new_labs = [child.label for child in t.branches][::-1]
        for i in range(len(t.branches)):
            child = t.branches[i]
            if need_reverse:
                child.label = new_labs[i]
            reverse_helper(child, not need_reverse)

    reverse_helper(t, True)

# Q8
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return
    if isinstance(link.first, Link):
        deep_map_mut(fn, link.first)
    else:
        link.first = fn(link.first)
    
    deep_map_mut(fn, link.rest)




# Q9
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    links = []
    while link is not Link.empty:
        if link in links:
            return True
        links.append(link)
        link = link.rest
        
    return False


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
