"""Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""

nums = open('Problem013_numbers.txt','r')

digSum = sum([int(line.replace('\n','')) for line in nums])
print str(digSum)[:10]
