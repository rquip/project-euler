'''
The prime factors of 13195 are 5, 7, 13 and 29

What is the largest prime factor of the number 600851475143?

Status: TOO SLOW
'''

largest_prime = 0
for x in range(2, 600851475144):
    if 600851475143%x == 0:
        for y in range(1, x+1):
            if x%y == 0 and (y != 1 and x != y):
                break
            elif x == y:
                largest_prime = x
print("Largest prime: " + str(largest_prime))
            

