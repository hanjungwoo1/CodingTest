def isPalindrome2(x):
    if x==x[::-1]:
        return True
def solution2(s):
    MAX=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPalindrome2(s[i:j]):
                if MAX<len(s[i:j]):
                    MAX=len(s[i:j])
    return MAX