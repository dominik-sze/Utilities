import profile

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
	sieve[0] = False
	sieve[1] = False
	for i in range(3, int(upper_limit**.5)+1, 2):
		if sieve[i]:
			for j in range(i*i, upper_limit, 2*i):
				sieve[j] = False
	return [2] + [p for p in range(3, n, 2) if sieve[p]]

def eratosthenes_sieve3(upper_limit):
	"""
	Returns a list of primes < n
	"""
	sieve = [True]*upper_limit
	for i in range(3, int(upper_limit**0.5)+1, 2):
		if sieve[i]:
			sieve[i*i::2*i] = [False]*int(((n-i*i-1)/(2*i)+1))
	return [2] + [i for i in range(3, n, 2) if sieve[i]]

if __name__=='__main__':
	n = 2000000
	profile.run("eratosthenes_sieve1(n)")
	profile.run("eratosthenes_sieve2(n)")
	profile.run("eratosthenes_sieve3(n)")
