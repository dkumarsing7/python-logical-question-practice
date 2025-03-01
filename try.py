string = 'xyjalajracecarxjalajudeepakapeed'

def palindrome(string):
    reversed = string[::-1]
    if string==reversed:
        return True 
def find_longest(string):
    n = len(string)
    longest=''
    for i in range(n):
        for j in range(i+1,n+1):
            if palindrome(string[i:j]) and len(string[i:j]) > len(longest):
                longest=string[i:j]
    return longest
                
print(find_longest(string))
    