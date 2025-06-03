class Solution:
    def isValid(self, s: str) -> bool:
        stack = []    
        for i in s:
            peek = stack[-1] if stack else None
            if i == "(":
                stack.append(i)
            elif i == "[":
                stack.append(i)
            elif i == "{":
                stack.append(i)
            elif i == ")" and peek == "(":
                stack.pop()
            elif i == "]" and peek == "[":
                stack.pop()
            elif i == "}" and peek == "{":
                stack.pop()
        empty = not bool(stack)
        return empty
            
sol = Solution()    
s = "()[]\\{\}"
print(sol.isValid(s))           