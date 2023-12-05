
class Stack:

	def __init__(self):
		self.stack = []

	def __str__(self):
		return str(self.stack)

	def is_empty(self):
		return self.stack == []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if len(self.stack) == 0:
			return print('None')

		item = self.stack[-1]
		del self.stack[-1]
		return item
	def is_balanced(self, n):

		listofbrac = []
		count = 0
		while count != len(n):
			if n[count] == '{' :
				listofbrac.append(n[count])
			if n[count] == '}':
				if len(listofbrac) > 1:
					listofbrac.pop()
			count = count + 1
		if len(listofbrac) == 0:
			print('The brackets ARE balanced')
		elif len(listofbrac) > 0:
			print('The brackets are NOT balanced')


	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[-1]
