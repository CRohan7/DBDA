# Q Given list of strings, sort all the strings by last character of that string. 
# Use lambda function and normal function both.

l=['az','bo','fd','op']
sort = (sorted(l, key=lambda x: x[-1]))

print(sort)