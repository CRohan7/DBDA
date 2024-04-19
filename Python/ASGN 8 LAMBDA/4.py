# Q Given list of employees. This list may contain repetitions. Find all unique employee names 
# and print them as per order of second character in that name. Use lambda function and normal 
# function both.

l=[ 'rwhan' , 'mzhan' , 'hr' , 'mohan','mohan' ]
l=set(l)
print( sorted(l , key=( lambda x:x[1] )))








