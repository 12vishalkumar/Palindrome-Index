import math
import os
import random
import re
import sys
# Complete the 'palindromeIndex' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
def is_palindrome(s):
    return s == s[::-1]
def palindromeIndex(s):
    # Write your code here
    i = 0
    j = len(s) - 1
    while((i < j) and (s[i] == s[j])):
        i += 1
        j -= 1
    if(i == j):
        return 0
    if is_palindrome(s[i+1:j+1]):
        return i
    if is_palindrome(s[i:j]):
        return j
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        fptr.write(str(result) + '\n')
    fptr.close()