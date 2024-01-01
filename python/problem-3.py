'''
The prime factors of 13195 are 5, 7, 13 and 29

What is the largest prime factor of the number 600851475143?

What is left: To fully understand algorithm.

Challenges: Try to write as one line
'''

N = 13195
p = 2
while N >= p*p:
    if N%p == 0:
        print(str(p) + " * ")
        N = N/p
    else:
        p = p + 1
print(str(N))

            

