'''
Given a file with a large number, find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

Test: The first four adjacent digits in the 1000-digit number that have the greatest product are 9x9x8x9 = 5832

Method 1:
- Read in number as input
- Remove new lines
- Loop through input per 13


STILL WORKING ON THIS. NOT WORKING NOT WORKING
'''

file = open('problem-8-textfile.txt', 'r')
number = file.read()
number = number.replace('\n','')
file.close()

maxsum = 0
incrementor = 0
temp_sum = 0
while (13 + incrementor) <= 1000: 
    for x in range(0 + incrementor, 13 + incrementor):
        temp_sum = temp_sum + int(number[x])
    if temp_sum > maxsum:
        maxsum = temp_sum
    incrementor = incrementor + 1
print("Solution: " + str(maxsum))


