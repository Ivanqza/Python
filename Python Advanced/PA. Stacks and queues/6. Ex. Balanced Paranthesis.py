expression = input()

stack = []
balanced = True
for paren in expression:
    if paren in '[{(':
        stack.append(paren)
    elif paren in ']})':
        if len(stack) == 0:
            balanced = False
            break

        opening_paren = stack.pop()
        if paren == ']' and opening_paren == '[':
            continue
        elif paren == '}' and opening_paren == '{':
            continue
        elif paren == ')' and opening_paren == '(':
            continue
        else:
            balanced = False
            break

if balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')