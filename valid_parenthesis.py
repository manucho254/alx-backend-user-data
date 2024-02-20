def isValid(s: str) -> bool:
    opening = ["(", "[", "{"]
    length = len(s)
    stack = []

    if length <= 1:
        return False

    stack.insert(0, s[0])
    for x in range(1, length):
        if s[x] in opening:
            stack.insert(0, s[x])
            continue
        if len(stack) > 0:
            if s[x] == ")" and stack[0] == "(":
                stack.pop(0)
                continue
            elif s[x] == "}" and stack[0] == "{":
                stack.pop(0)
                continue
            elif s[x] == "]" and stack[0] == "[":
                stack.pop(0)
                continue
            else:
                return False
        else:
            return False
            
    return len(stack) == 0
            
            
print(isValid("(])"))
print(isValid("[]])"))