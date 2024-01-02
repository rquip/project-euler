'''
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Example: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder

Challenge:
- Condense code
- Make it faster
'''

x = 20
done = True
test_range = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
while True:
    for y in range(11,21):
        if x%y != 0:
            x = x + 20
            break
        elif x%y == 0 and y == 20:
            print(x)
            exit()
