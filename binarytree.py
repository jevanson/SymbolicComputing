class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def inorder(root):
	current = root
	stack = [] # initialize stack
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

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)

	arr = inorder(root)

	print(arr)