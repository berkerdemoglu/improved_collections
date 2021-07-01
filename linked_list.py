from typing import Sequence, Iterator


class LinkedListNode:
	"""Represents a node that holds a value in a singly linked list."""

	def __init__(self, val: int, next=None):
		"""Initialize the value of the node and the next node."""
		self.val = val
		self.next = next

	def __str__(self):
		"""Return the string representation of the node."""
		return str(self.val)

	def __repr__(self):
		"""Return the string representation of the node."""
		return str(self.val)

	def get(self, index: int) -> 'LinkedListNode':
		"""Get the value at the n-th index."""
		if index > 0:
			if self.next is not None:
				return self.next.get(index-1)
		elif index == 0:
			return self

	def add_at_index(self, index: int, val: int, original_index: int) -> None:
		"""Add a node at the n-th index."""
		if index > 0:
			if self.next is not None:
				self.next.add_at_index(index-1, val, original_index)
			else:
				raise IndexError(f'Index {original_index} out of range')
		elif index == 0:
			prev_next = self.next
			self.next = LinkedListNode(val, prev_next)

	def add_at_tail(self, val: int) -> None:
		"""Add a value at the very end of the list."""
		if self.next is not None:
			self.next.add_at_tail(val)
		else:
			self.next = LinkedListNode(val)


class LinkedList:
	"""A singly linked list."""

	def __init__(self, vals: Sequence[int]):
		"""Initialize the linked list with a sequence of values."""
		self.root = LinkedListNode(vals[0])

		for i in range(1, len(vals)):
			self.root.add_at_tail(vals[i])

	def add_at_head(self, val: int) -> None:
		"""Add a value at the head of the list."""
		prev_root = self.root
		self.root = LinkedListNode(val, prev_root)

	def add_at_tail(self, val: int) -> None:
		"""Add a value at the tail of the list."""
		self.root.add_at_tail(val)

	def add_at_index(self, index: int, val: int) -> None:
		"""Add a value at the n-th index."""
		if index == 0:  # adding at head
			self.add_at_head(val)
		else:
			self.root.add_at_index(index, val, original_index=index)

	def delete_at_index(self, index: int) -> None:
		"""Delete a node at the n-th index."""
		if index == 0:
			prev_next = self.root.next
			self.root = prev_next
		elif index > 0:
			ele_before_to_delete = self.root.get(index-1)
			to_delete = self.root.get(index)

			if to_delete is None:
				raise IndexError(f'Index {index} out of range')

			to_replace = to_delete.next
			ele_before_to_delete.next = to_replace
		else:
			raise IndexError(f'Index {index} out of range')

	# List methods
	def __getitem__(self, index: int) -> LinkedListNode:
		"""Get a value at the n-th index."""
		item = self.root.get(index)
		if item is None:
			raise IndexError(f'Index {index} out of range')
		else:
			return item

	def __setitem__(self, index: int, val: int) -> None:
		"""Set a value at the n-th index."""
		item = self.root.get(index)
		if item is None:
			raise IndexError(f'Index {index} out of range')
		else:
			item.val = val

	def __iter__(self) -> Iterator:
		"""Return an iterator for the list."""
		self._index = 0
		return self

	def __next__(self) -> LinkedListNode:
		"""Get the next node."""
		node = self.root.get(self._index)

		if node is not None:
			self._index += 1
			return node
		else:
			raise StopIteration

	def __len__(self):
		"""Return the length of the list by looping over it."""
		length = 0
		for ele in self:
			length += 1
		return length

	# String methods
	def __str__(self):
		"""The string representation of the list."""
		s = "["
		for ele in self:
			s += str(ele.val) + ", "

		s = s[:-2]

		s += "]"
		return s

	def __repr__(self):
		return str(self)


def main():
	"""Test the linked list algorithm."""
	l = LinkedList([5, 8, 1, 2, 9, 23, 10])

	for ele in l:
		print(ele)

	print(len(l))

	try:
		print(l[100])
	except IndexError:
		print('Exception raised properly!')

	l.add_at_head(3)
	print(l.root)

	try:
		l.add_at_index(20, 0)
	except IndexError:
		print('Exception raised properly!')

	print(l)
	l.delete_at_index(6)
	print(l)

	print(l)
	l[0] = 1
	print(l)

	try:
		l[20] = 1
	except IndexError:
		print('Exception raised properly!')


if __name__ == '__main__':
	main()
