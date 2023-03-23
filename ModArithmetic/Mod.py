class Mod:
	def __init__(self, x, n):
		self.x = x
		self.n = n
		self.r = x % n

	def isCongruent(self, m):
		if self.r == m.r:
			return True
		else:
			return False

if __name__ == "__main__":
	a = Mod(2,10)
	b = Mod(12,10)
	c = Mod(3,10)

	print(a.isCongruent(b))
	print(a.isCongruent(c))