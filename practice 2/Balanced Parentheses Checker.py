p="{[()]}"

def paranthesis(p):
    i=0
    j=len(p)-1
    while i<=j:
        if p[i] == '(' and p[j] == ')':
            i += 1
            j -= 1
        elif p[i] == '{' and p[j] == '}':
            i += 1
            j -= 1
        elif p[i] == '[' and p[j] == ']':
            i += 1
            j -= 1
        else:
            return False
    return True

print(paranthesis(p))