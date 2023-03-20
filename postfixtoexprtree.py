from binarytree import *
from infixtopostfix import *

class PostfixToExprTree:
	def __init__(self, postfix):
		self.postfix = postfix
		self.top = -1
		self.array = []

	def isEmpty(self):
		return True if self.top == -1 else False

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	def push(self, op):
		self.top += 1
		self.array.append(op)

	def isOperand(self, ch):
		return ch.isalnum()

	def postfixtoexprtree(self):
		for i in range(len(self.postfix)):
			if self.isOperand(postfix[i]):
				self.push(Node(postfix[i]))
			else:
				right = self.pop()
				left = self.pop()
				new_node = Node(postfix[i])
				new_node.left = left
				new_node.right = right
				self.push(new_node)

		root = self.pop()

		return root

if __name__ == '__main__':
	exp = "1*a+b+0"
	obj = InfixToPostfix(len(exp))

	postfix = obj.infixtopostfix(exp)
	print("")
	print("Postfix expression: " + str(postfix))

	posttotree = PostfixToExprTree(postfix)
	root = posttotree.postfixtoexprtree()

	tree = BinaryTree(root)
	print(tree.inorder())

	new_tree = BinaryTree( simplify(tree.root) )
	print(new_tree.inorder())