import profile
import unittest
import optparse
import sys


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
	if n == sqrt*sqrt and n!=1:
		sum+=sqrt
		limit-=1
	for i in range(2, int(math.sqrt(n))+limit):
		if n%i==0:
			sum+=(i+n/i)
	return sum

def sum_factors_prime(number, primes):
	n = number
	sum = 1
	p = primes[0]
	i = 0
	l = len(primes)
	while p*p<=n and n>1 and i<l:
		p = primes[i]
		i+=1
		if n%p==0:
			j=p*p
			n=n/p
			while n%p==0:
				j = j*p
				n = n/p
			sum = sum*(j-1)/(p-1)
	if n>1:
		sum*=n+1
	return sum-number

class FactorsTest(unittest.TestCase):
	def test_1(self):
		n = 1
		self.assertEqual(1, sum1(n))
		self.assertEqual(1, sum2(n))
		self.assertEqual(1, sum3(n))

	def test_2(self):
		n = 2
		self.assertEqual(1, sum1(n))
		self.assertEqual(1, sum2(n))
		self.assertEqual(1, sum3(n))

	def test_1(self):
		n = 3
		self.assertEqual(1, sum1(n))
		self.assertEqual(1, sum2(n))
		self.assertEqual(1, sum3(n))

	def test_4(self):
		n = 4
		self.assertEqual(3, sum1(n))
		self.assertEqual(3, sum2(n))
		self.assertEqual(3, sum3(n))

	def test_prime_29(self):
		n = 29
		self.assertEqual(1, sum1(n))
		self.assertEqual(1, sum2(n))
		self.assertEqual(1, sum3(n))
	
	def test_prime_20029(self):
		n = 20029
		self.assertEqual(1, sum1(n))
		self.assertEqual(1, sum2(n))
		self.assertEqual(1, sum3(n))
	
	
if __name__=='__main__':
	sys.path.append("../prime")
	import prime

	parser = optparse.OptionParser('python %prog [-p ] [-v V]')
	parser.add_option('-p', dest='profiler', action='store_true', help='run profiler instead of unittests (default parameter for function call is 29629042)')
	parser.add_option('-v', dest='v', type='int', help='set input parameter for functions called by profiler', default=296290423744)
	
	parser.print_help()
	(options, args) = parser.parse_args()
	
	if options.profiler == True or options.v!=None:
		n = options.v
		#profile.run("sum1(n)")
		#profile.run("sum2(n)")
		profile.run("sum3(n)")
		profile.run("sum_factors_prime(n, prime.eratosthenes_sieve2(int(n**0.5)))")
	else: 
		unittest.main()

