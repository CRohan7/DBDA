# 12. Write a Python function that checks whether a passed string is a palindrome or not. 
# Note: A palindrome is a word, phrase, or sequence that reads the
# same backward as forward, e.g., madam or nurses run.

def check(s:str):
    news=s[::-1]
    print(news)

    if s==news:
        print("Palindrome!")
    else:
        print("Not Palindrome!")



st=input("Enter String: ")
check(st)

