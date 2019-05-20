'''
https://leetcode.com/problems/fibonacci-number/
'''
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        def fib_dp(N):
            if N==0 or N==1:
                return N
            result = [0] * (N+1)
            print result
            result [0] = 0
            result [1] = 1
            for i in range(2, N+1):
                print (i)
                result[i] = result[i-1] + result[i-2]
            return result[N]
        
        def fib_rec(N):
        	if N == 0 or N == 1:
        		return N
        	return self.fib(N-1) + self.fib(N-2)

        return fib_dp(N)
    
        # if N == 0 or N == 1:
        #     return N
        # # return self.fib(N-1) + self.fib(N-2)
        