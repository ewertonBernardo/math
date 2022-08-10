num = int(input("Number to show primes smaller than it:"))
smallers = [True]*(num)
#print(len(smallers))


for i in range(num):
	#print(f"i:{i}")
	if(i > 0):
		
		if(smallers[i] == True):
			p = (i+1)*(i+1)-1
			if(p<num):
				smallers[p] = False

			for p in range(p, num,(i+1)):
				#print(f"p:{p}")
				if(p<num):
					smallers[p] = False
	else:
		smallers[i] = False

for i in range(num):
	print(smallers[i])