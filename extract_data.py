import re

# One line with list comprehension
#print(sum( [ int(n) for n in re.findall('[0-9]+',open('regex_sum_116685.txt').read()) ] ))

file42 = open('regex_sum_116685.txt')
sum = 0
for line in file42:
    nums = re.findall('[0-9]+', line)
    if len(nums) < 1: continue
    for num in nums:
        sum = sum + int(num)
print(sum)
