
import sieve_eratosthenes2

numbers = []
print("Enter the numbers (zero to calculate):")
while True:
	number = int(input())
	if number == 0:
		break
	else:
		numbers.append(number)


bool_primes = sieve_eratosthenes2.sieve(max(numbers))
#print(bool_primes)

primes = sieve_eratosthenes2.prime(bool_primes)
#print(primes)

factors = []

for p in primes:

	divide = True
	while divide: #for each number check (with sum) if it is divisible by the same prime
		
		cont_n = 0 #adder
		for i in range(len(numbers)):

			if(numbers[i]%p == 0 and numbers[i]!=1): 
				numbers[i] = numbers[i]/p #update value divided
				cont_n += 1


		if(cont_n == len(numbers)): #if all are divisible by the prime
			factors.append(p)
		else:
			divide = False


print("factors:")
print(factors)

mdc = 1
for f in factors:
	mdc *= f

print(f"MDC:{mdc}")
