import profile

def find1(num):
	sum = 1
	for i in range(2, num):
		if num%i==0:
			sum+=i
	print(sum)

def find2(num):
	sum = 1
	for i in range(2, int(num/2.)+1):
		if num%i==0:
			sum+=i
	print(sum)

def find3(num):
	import math
	sum = 1
	limit = 1
	sqrt = int(math.sqrt(num))
	if num == sqrt*sqrt:
		sum+=sqrt
		limit-=1
	for i in range(2, int(math.sqrt(num))+limit):
		if num%i==0:
			sum+=(i+num/i)
	print(int(sum))

if __name__=='__main__':
	num = 29629042
	profile.run("find1(num)")
	profile.run("find2(num)")
	profile.run("find3(num)")
