class Node:
	def __init__(self, prev = None, next = None, data = 0):
		self.prev = prev
		self.next = next
		self.data = data
	def __str__(self):
		return str(self.data)
	def delete(self):
		self.prev.next = self.next
		self.next.prev = self.prev

# 2.1
"""Remove duplicates from an unsorted linked list."""
# Let n be the length of the list
# O(n) time, O(n) space

def removeDups(head):
	d = {}
	cur = head
	while cur:
		if cur.data in d:
			d[cur.data] += 1
		else:
			d[cur.data] = 1
		cur = cur.next
	cur = head
	while cur:
		if d[cur.data] >= 1:
			d[cur.data] = 0
		else:
			if cur.prev:
				cur.prev.next = cur.next
			if cur.next:
				cur.next.prev = cur.prev
		cur = cur.next




# 2.2
"""Find the kth to last element of a singly linked list"""
# Let n be the length of the list
# O(n) time, O(1) space

def kToLast(head, k):
	first = head
	result = head
	for i in range(k):
		if not first:
			return "Insufficient elements!"
		first = first.next
	while first:
		first = first.next
		result = result.next
	return result


# 2.3
"""Delete a node in a linked list.  It won't be the first or last."""
# Let n be the number of elements in the list past the given node
# O(n) time, O(1) space

def deleteMiddle(node):
	while node.next and node.next.next:
		node.data = node.next.data
		node = node.next
	node.data = node.next.data
	node.next = None



# 2.4
"""Partition a linked list around a value x such that all nodes strictly less than x come before all nodes greater equal x"""
# Let n be the number of elements in the list
# O(n) time, O(1) space

def partition(head, x):
	part = head #everything left of part will remain strictly smaller than x
	while part and part.data < x:
		part = part.next
	cur = part
	while cur:
		if cur.data < x:
			part.data, cur.data = cur.data, part.data
			part = part.next
		cur = cur.next
	return head


# 2.5 
"""Sum two numbers where the digits, starting with the 1's place, are stored as the nodes of a list."""

# Let n be the number of elements in the larger list
# O(n) time, O(1) space
# Note the sumListsHelper function below!

def sumLists(first, second):
	return sumListsHelper(first, second, 0)

def sumListsHelper(first, second, carry):
	if not first and not second and carry == 0:
		return None
	sum = carry
	if first:
		sum += first.data
		first = first.next
	if second:
		sum += second.data
		second = second.next
	result = sum % 10
	print "Result is " + str(result)
	carry = sum//10
	myNode = Node(data = result)
	myNode.next = sumListsHelper(first, second, carry)
	return myNode


# 2.6
"""Implement a function to check if a linked list is a palindrome"""
# Let n be the number of elements in the list
# O(n) time, O(n) space

def palindrome(head):
	seen = {}
	while head:
		if head.data not in seen:
			seen[head.data] = True
		else:
			seen[head.data] = not seen[head.data]
		head = head.next
	numOdd = 0
	for element in seen:
		if seen[element]:
			numOdd += 1
		if numOdd >= 2:
			return False 
	return True

# 2.7
"""Given two singly linked lists, determine if they intersect, by reference not by value.  If so, return the intersecting node."""
# Let a and b be the number of elements in the lists
# O(a+b) time, O(1) space

def intersection(head_a, head_b):
	if not head_a or not head_b:
		return "No intersection."
	length_a = 1
	a = head_a
	length_b = 1
	b = head_b
	while a.next:
		length_a += 1
		a = a.next
	while b.next:
		length_b += 1
		b = b.next
	print length_a
	print length_b
	if a != b:
		return "No intersection."
	a = head_a
	b = head_b
	if length_a < length_b:
		a, length_a, b, length_b = b, length_b, a, length_a
	while length_a > length_b:
		a = a.next
		length_a -= 1
	while a != b:
		a = a.next
		b = b.next
	return a



# 2.8
"""Given a circular linked list (one which contains a loop), implement an algorithm that returns the node at the beginning of the loop."""
# Let n be the number of distinct nodes in the list
# O(n) time, O(1) space

def loopDetection(head):
	#first get in the loop
	faster = head
	slower = head
	while True:
		slower = slower.next
		faster = faster.next.next
		if faster == slower:
			break
	#find the length of the loop
	length  = 0
	while True:
		length += 1
		slower = slower.next
		faster = faster.next.next
		if faster == slower:
			break
	faster = head
	slower = head
	#give faster a head start
	for i in range(length):
		faster = faster.next
	while(faster != slower):
		faster = faster.next
		slower = slower.next
	return faster



