# brute force

# def vParenthesis(s):
#     while "()" in s or "[]" in s or "{}" in s :
#         s = s.replace("()","").replace("[]",'').replace("{}",'')

#     return len(s)==0

# string = "[()]{}{[()()]()}"
# print(vParenthesis(string))


def vParenthesis(s):
    stack = []
    openingBrackets = '({['
    closingBrackets = ')}]'

    for i in s:
        if i in openingBrackets:
            stack.append(i)

        elif i in closingBrackets:
            if not stack:
                return False
            top = stack.pop()
            if openingBrackets.index(top) != closingBrackets.index(i):
                return False
            
    return len(s)==0

string = "[()]{}{[()()]()}"
print(vParenthesis(string))


