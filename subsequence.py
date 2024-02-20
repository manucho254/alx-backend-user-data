def isSubsequence(s: str, t: str) -> bool:
    word = ""
    
    for x in range(len(s)):
        last = 0
        for i in range(x, len(t)):
            last += i
            if s[x] == t[i]:
                word += t[i]
                break
            
        if last > len(t):
            break
        
        if word == s:
            break

    print(word)
    return word == s


isSubsequence("agd", "ahbgdc")