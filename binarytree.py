class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self, root):
		self.root = root

	def inorder(self):
		current = self.root
		stack = []
		result = []
     
		while True:
			if current is not None:
				stack.append(current)        
				current = current.left
			elif(stack):
				current = stack.pop()
				result.append(current.value)
				current = current.right
			else:
				break
      
		return result

def simplify(node):
	if node:
		new_left = simplify(node.left)
		new_right = simplify(node.right)

		new_node = Node(node.value)
		new_node.left = new_left
		new_node.right = new_right

		"""
			1. left and right are constants
			2. operator is addition/subtraction, and left or right are 0
			3. operator is multiplication, and left or right is 1
			4. operator is multiplication, and left or right is 0
			5. operator is division, and divisor is 1
		"""
		"""if new_left and new_left.value == "1" and new_node.value == "*":
			new_node = new_right
		elif new_right and new_right.value == "1" and new_node.value == "*":
			new_node = new_left
		elif new_left and new_left.value == "0" and new_node.value == "+":
			new_node = new_right
		elif new_right and new_right.value == "0" and new_node.value == "+":
			new_node = new_left"""

		return new_node

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	tree = BinaryTree(root)
	print(tree.inorder())