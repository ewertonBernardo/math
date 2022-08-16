num = int(input("Number to show primes smaller than it:"))
smallers = [True]*(num)
#print(len(smallers))


for i in range(num):
	if(i > 0):
		#next prime
		if(smallers[i] == True):
			print(f"multiples of {i+1}")
			p = (i+1)*(i+1)-1
			#discard first multiple of p
			if(p<num and smallers[p]==True):
				smallers[p] = False
				print(p+1)

			#go through the numbers 2 by 2, 3 by 3, 5 by 5...
			p += (i+1)
			for p in range(p, num,(i+1)):
				if(p<num and smallers[p]==True):
					#discard multiple of p
					smallers[p] = False
					print(p+1)
	#number 1				
	else:
		smallers[i] = False
# view primes in list(True)
for i in range(num):
	print(f"{i+1}: "+str(smallers[i]))