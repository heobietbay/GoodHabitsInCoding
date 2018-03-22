# Probably the second-best solution, using traditional for loop to calculate the number
def fib_loop(num):
    if num < 3:
        return 1
    a = b = 1
    for i in range(2, num):
        a, b = b, a + b

    return b


# Worst solution, too slow and repeatative
# this recursive can even lead to stack overflow when calculation num > 50
def fibR(num):
    if num < 3:
        return 1;
    return fibR(num - 1) + fibR(num - 2)


# Since we know some fix values, we used them as look up table.
# This use decorator technique
# Still not good solution
def fibR_with_look_up(num):
    if num < 18:
        return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597][num]
    return fibR_with_look_up(num - 1) + fibR_with_look_up(num - 2)


# Apply sort-of memoization technique, where calculated values are kept.
def fibR_with_dict(num, dict):
    if num in dict:
        return dict[num]
    dict[num] = fibR_with_dict(num - 1, dict) + fibR_with_dict(num - 2, dict)
    return dict[num]

# Fastest solutions
# Pure maths: using Q matrix to calculate the fibonacci number
def fib_Qmatrix(num):
    def mul(A, B):  # multiply two 2x2 matrices
        a, b, c, d = A
        e, f, g, h = B
        return a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h

    A = [1, 1, 1, 0]  # = Fibonacci matrix. We will	generate A, A ** 2, A ** 4, A ** 8, A ** 16,
                      # etc., some of which can be combined to produce matrix X.

    X = [1, 0, 0, 1]       # = identity matrix, which will later contains the answer. If you multiply an identity matrix with other matrix OM, you got back OM
    s = str(bin(num))[2:]  # x[1] = fib_Qmatrix(n). The str(bin(n))[2:] will change fib_Qmatrix number to a binary string--e.g., n = 12 --> '1100'.
    s = s[::-1]            # The s[::-1] will reverse digits in a binary string.
    for n in range(len(s)):
        if s[n] == '1':
            X = mul(X, A)  # Matrix X accumulates some of the powers of	matrix A --
        A = mul(A, A)  # e.g., X = A**12 = A**4 + A**8.
    return X[1]

print(fibR_with_dict(25, {0: 1, 1: 1, 2: 1, 3: 2}))
print(fib_loop(25))
print(fib_Qmatrix(25))
