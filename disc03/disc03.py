'''discussion 3'''

#Question 3.1 define a function tree_max(t) that returns the largest number in a tree
def tree_max(t):
	"""return the max of a tree

	>>> t = tree(1, [tree(3,[tree(4), tree(5), tree(6)]), tree(2)])
	>>> tree_max(t)
	6
	"""
	if is_leaf(t):
		return label(t)

	num_max = label(t)
	for b in branches(t):
		if num_max <= tree_max(b):
			num_max = tree_max(b)   #find the maximum number in the branches

	return num_max


#Question 3.2  defines a function that returns the height of a tree.
def height(t):
	"""return the height of a tree

	>>> t = tree(1, [tree(3,[tree(4), tree(5), tree(6)]), tree(2)])
	>>> height(t)
	2
	>>> t = tree(1, [tree(2,[tree(3,[tree(4)])])])
	>>> height(t)
	3
	"""
	if is_leaf(t):
		return 0
	
	max_height = 0
	for b in branches(t):
		if max_height < height(b): 
			max_height = height(b) # find the branches with the largest height
		
	max_height += 1

	return max_height
	

#Question 3.3 define a function that squares every value in the tree t.
def square_tree(t):
	"""return a tree with the sqaure of every element in t
	>>> t = tree(1, [tree(3,[tree(4), tree(5), tree(6)]), tree(2)])
	>>> square_tree(t)
	[1, [9, [16], [25], [36]], [4]]

	>>> t = tree(2)
	>>> square_tree(t)
	[4]
	"""

	if is_leaf(t):
		return tree(label(t) **2)
	else:
		bs = [square_tree(b) for b in branches(t)]
		return tree(label(t) **2, bs)


#Question 3.4  return a funtion to return the path
def find_path(t, x):
	"""
	>>> t = tree(2, [tree(7,[tree(3), tree(6,[tree(5), tree(11)])]), tree(15)])
	>>> find_path(t,5)
	[2, 7, 6, 5]
	>>> find_path(t, 10) # returns None
	"""
	if label(t) == x:
		return [x]
	
	else:
		bs = [find_path(b,x) for b in branches(t)]
		for path in bs:
			if path:
				return [label(t)] + path


#Question 3.5  return a tree with first K level of a tree
def prune(t, k):
	"""
	>>> t = tree(2, [tree(7,[tree(3), tree(6,[tree(5), tree(11)])]), tree(15)])
	>>> prune(t, 2)
	[2, [7, [3], [6]], [15]]

	"""

	if k == 0 or is_leaf(t):
		return tree(label(t))

	else:
		bs = [prune(b, k-1) for b in branches(t)]
		return tree(label(t), bs)
		






# Tree constructor and selectors
def tree(root_label, branches =[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [root_label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)