
def sieve(num):
	smallers = [True]*(num)

	for i in range(num):
		if(i > 0):
			#next prime
			if(smallers[i] == True):
				#print(f"multiples of {i+1}")
				p = (i+1)*(i+1)-1 #p how to index
				if(p<num and smallers[p]==True):
				#discard first multiple of p
					smallers[p] = False
				#	print(p+1)

				#go through the numbers 2 by 2, 3 by 3, 5 by 5...
				p += (i+1) #index of next multiple
				for p in range(p, num,(i+1)):
					if(p<num and smallers[p]==True):
						#discard multiple of p
						smallers[p] = False
				#		print(p+1)
		#number 1				
		else:
			smallers[i] = False
	return smallers	


def prime(smallers):
	primes = []
	
	for i in range(len(smallers)):
		if (smallers[i] == True):
			primes.append(i+1) #append prime
	
	return primes


#print(prime(sieve(20)))