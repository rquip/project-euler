"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sume these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Challenges: 
- Try to make one line
- What if the number is 1,000,000,000? You will need to modify your solution
"""

# Solution 1
multiples = (x for x in range(3, 1000) if x%3 == 0 or x%5 == 0)
print("Solution 1: " + str(sum(multiples)))

# Solution 2: Attempt to make one line
print("Solution 2: " + str(sum(x for x in range(3, 1000) if x%3 == 0 or x%5 == 0)))

# Solution 3: What if the number is 1,000,000,000?
