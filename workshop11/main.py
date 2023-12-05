from stacks import Stack
file = open('evens.txt', 'r')
all_lines = ''
all_lines = file.read()


s = Stack()
# s.pop()
s.is_balanced(all_lines)