def longestValidParentheses(s: str) -> int:
    opening, closing = "(", ")"
    valid = []
    length = len(s)
    longest = 0

    if length <= 1:
        return 0
    
    idx = 0
    word = ""
    while idx < length:
        sub = ""
        for x in range(idx, length - 1):
            if s[x] == opening and s[x + 1] == closing:
                sub += "()"
                break
            else:
                break
            
        if len(valid) > 0 :
            if valid[-1] == "":
                longest = max(longest, len("".join(valid)))
                valid.clear()
                
        if len(sub) > 0:
            word += sub
        else:
            valid.append(word)
            word = ""
        
        idx += 1
        
    return max(longest, len("".join(valid)))


print(longestValidParentheses("()(()"))
print(longestValidParentheses("(()"))
print(longestValidParentheses(")()())"))