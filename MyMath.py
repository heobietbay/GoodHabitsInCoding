def power(num,p):
    s = str(bin(p))[2:]
    s = s[::-1]
    X = 1
    A = num
    for n in range(len(s)):
        if s[n] == '1':
            X = X*A
        A = A*A
    return X

print(power(2,5))