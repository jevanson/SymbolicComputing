class InfixToPostfix:
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []
		self.output = []
		self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

	def isEmpty(self):
		return True if self.top == -1 else False

	def peek(self):
		return self.array[-1]

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	def push(self, op):
		self.top += 1
		self.array.append(op)

	# A utility function to check is the given character
	# is operand
	def isOperand(self, ch):
		return ch.isalnum()

	# Check if the precedence of operator is strictly
	# less than top of stack or not
	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False

	# The main function that
	# converts given infix expression
	# to postfix expression
	def infixtopostfix(self, exp):

		# Iterate over the expression for conversion
		for i in exp:
			
			# If the character is an operand,
			# add it to output
			if self.isOperand(i):
				self.output.append(i)

			# If the character is an '(', push it to stack
			elif i == '(':
				self.push(i)

			# If the scanned character is an ')', pop and
			# output from the stack until and '(' is found
			elif i == ')':
				while((not self.isEmpty()) and
					self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()

			# An operator is encountered
			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)

		# Pop all the operator from the stack
		while not self.isEmpty():
			self.output.append(self.pop())

		for ch in self.output:
			print(ch, end="")

		return self.output


# Driver code
if __name__ == '__main__':
	exp = "a+b*(c^d-e)^(f+g*h)-i"
	obj = InfixToPostfix(len(exp))

	# Function call
	result = obj.infixtopostfix(exp)
	print()
	print("Postfix expression: " + str(result))