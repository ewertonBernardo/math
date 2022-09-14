
import sieve_eratosthenes2

numbers = []
while True:
	number = int(input())
	if number == 0:
		break
	else:
		numbers.append(number)


primes = sieve_eratosthenes2.sieve(max(numbers))
print(primes)



multiples = []

if(numbers[0]%2 == 0 and numbers[0]!=1):
	numbers[0] = numbers[0]/2
	multiples.append(2)
if(numbers[0]%3 == 0 and numbers[0]!=1):
	numbers[0] = numbers[0]/3
	multiples.append(3)
if(numbers[0]%5 == 0 and numbers[0]!=1):
	numbers[0] = numbers[0]/5
	multiples.append(5)


for m in multiples:
	print(m)