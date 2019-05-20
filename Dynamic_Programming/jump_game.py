'''
https://leetcode.com/problems/jump-game-ii/
https://leetcode.com/problems/jump-game/
'''

class Solution:
	def __init__(self):
		self.arr = [2, 3, 1, 1, 4]
		self.min = float('inf')
		self.count = 0

	def minjumps(self, start):
		# print("MIN_JUMP")
		if start >= len(self.arr)-1:
			return self.count

		for i in range(start+1, len(self.arr)):
			if start + self.arr[start] >= i:
				self.count = self.count + 1
				result = self.minjumps(i)
				self.count -= 1
				if result < self.min:
					self.min = result
		return self.min

	def minjumps_dp(self):
		cost = [float('inf')] * len(self.arr)
		cost[0] = 0

		for j in range(1, len(self.arr)):
			for i in range(j):
				if i + self.arr[i] >= j:
					if cost[i] + 1 < cost[j]:
						cost[j] = cost[i] + 1

		return cost[len(self.arr) - 1]

def main():
	obj = Solution()
	print(obj.minjumps(0))
	print(obj.minjumps_dp())

if __name__ == "__main__":
	main()