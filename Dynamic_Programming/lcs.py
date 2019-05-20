
class Solution:
	def __init__(self, str1, str2):
		self.str1 = str1
		self.str2 = str2

	def lcs(self, i, j):
		if i >= len(self.str1) or j >= len(self.str2) :
			return 0
		if self.str1[i] == self.str2[j]:
			return 1 + self.lcs(i+1, j+1)
		else:
			return max(self.lcs(i, j+1), self.lcs(i+1, j))


	def lcs_dp(self):
		T = []
		for i in range (len(self.str1) + 1):
			temp  = []
			for j in range(len(self.str2) + 1):
				temp.append(0)
			T.append(temp)
		# print T

		for i in range(1, len(self.str1) + 1):
			for j in range(1, len(self.str2) + 1):
				if self.str1[i-1] == self.str2[j-1]:
					T[i][j] = T[i-1][j-1] + 1
				else:
					T[i][j] = max(T[i-1][j], T[i][j-1])

		return T[len(self.str1)][len(self.str2)]
	

def main():
	str1 = "ABCDEPH"
	str2 = "AXDFEYHR"
	obj = Solution(str1, str2)
	print(obj.lcs(0, 0))
	print(obj.lcs_dp())

if __name__ == "__main__":
	main()
