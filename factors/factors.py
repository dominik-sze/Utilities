import profile

def sum1(n):
	""" 
	Returns sum of proper divisors of n (numbers less than n which divide evenly into n).
	Running time: O(n)
	"""
	sum = 1
	for i in range(2, n):
		if n%i==0:
			sum+=i
	return sum

def sum2(n):
	""" 
	Returns sum of proper divisors of n (numbers less than n which divide evenly into n).
	Running time: O(n) (better constant than find1(n) [namely 1/2 vs 1])
	"""
	sum = 1
	for i in range(2, int(n/2.)+1):
		if n%i==0:
			sum+=i
	return sum

def sum3(n):
	""" 
	Returns sum of proper divisors of n (numbers less than n which divide evenly into n).
	Running time: O(sqrt(n))
	"""
	import math
	sum = 1
	limit = 1
	sqrt = int(math.sqrt(n))
	if n == sqrt*sqrt:
		sum+=sqrt
		limit-=1
	for i in range(2, int(math.sqrt(n))+limit):
		if n%i==0:
			sum+=(i+n/i)
	return sum

if __name__=='__main__':
	n = 29629042
	profile.run("sum1(n)")
	profile.run("sum2(n)")
	profile.run("sum3(n)")
