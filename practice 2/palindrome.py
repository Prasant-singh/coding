def palindrome(s):
    i=0
    j=len(s)-1
    while i<=j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return "Not A palindrome"
        
    return f"{s} is a palindrome"
    
    
    
s="raecar"
a=palindrome(s)
print(a)