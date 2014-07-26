import profile
import unittest

def eratosthenes_sieve1(upper_limit):
	"""
	Returns a list of primes < n
	"""

	sieve = [True]*upper_limit
	sieve[0] = False
	sieve[1] = False
	for i in range(2, upper_limit):
		if sieve[i]:
			for j in range(i+i, upper_limit, i):
				sieve[j] = False

	primes = []
	for i, v in enumerate(sieve):
		if v==True:
			primes.append(i)
	return primes

def eratosthenes_sieve2(upper_limit):
	"""
	Returns a list of primes < n
	"""
	sieve = [True]*upper_limit
	for i in range(3, int(upper_limit**0.5)+1, 2):
		if sieve[i]:
			sieve[i*i::2*i] = [False]*int(((upper_limit-i*i-1)/(2*i)+1))
	return [2] + [i for i in range(3, upper_limit, 2) if sieve[i]]

class PrimesTest(unittest.TestCase):
	def setUp(self):
		self.__primes = []
		try:
			with open('primes.txt') as fp:
				for line in fp:
					line = line.rstrip()
					self.__primes.extend([int(x) for x in line.split(' ')])
		except IOError as e:
			print('I/O error ({}): {}'.format(e.errno, e.strerror))

	def test_sieve(self):
		last = self.__primes[-1]
		result = eratosthenes_sieve2(last+1)
		
		for i,v in enumerate(result):
			self.assertEqual(self.__primes[i], v)


if __name__=='__main__':
	n = 2000000
	profile.run("eratosthenes_sieve1(n)")
	profile.run("eratosthenes_sieve2(n)")

	unittest.main()
