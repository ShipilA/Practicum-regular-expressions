s = input().split()
k = int(s[len(s) - 1])
s[len(s) - 1] = ''
x = s[len(s) - 2]
s[len(s) - 2] = ''
s = "".join(s)
stack = []
ok = 1;
for i in range(len(s)):
    c = s[i]
    if (c == x):
       stack.append({1 % k})
    elif (c in {'a', 'b', 'c', '1'}):
        stack.append({0})
    elif (c == '+'):
        if (len(stack) == 0):
            ok = 0
            break
        second = stack.pop()
        if (len(stack) == 0):
            ok = 0
            break
        first = stack.pop()
        stack.append(first | second)
    elif (c == '*'): #заполняем сет всеми модулями по к
        if (len(stack) == 0):
            ok = 0
            break
        t = stack.pop()
        q = {0}
        for j in range(k):
            for p in t:
                q.add(p)
                q.add((p * j) % k)
        stack.append(q)
    elif (c == '.'):#циклом заполняем всеми суммами
        if (len(stack) == 0):
            ok = 0
            break
        second = stack.pop()
        if (len(stack) == 0):
            ok = 0
            break
        first = stack.pop()
        q = set()
        for j in first:
            for t in second:
                q.add((j + t) % k)
        stack.append(q)
if (ok and len(stack) == 1):
    if (0 in stack.pop()):
        print("YES")
    else:
        print("NO")
else:
    print("ERROR")
