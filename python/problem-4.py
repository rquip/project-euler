'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers

Challenges
- Convert to 1 line
- Make faster and consider timing!
'''

final_answer = 0
for x in range(100, 1000):
    for y in range(x, 1000):
        test = x * y
        if str(test) == str(test)[::-1] and test > final_answer:
            final_answer = test
print("final answer: " + str(final_answer))
