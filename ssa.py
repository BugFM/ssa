def deconstruct(secret, n, k):
    values = []
    for i in range(n):
        values.append((i+1, polynomial(i+1) + secret))
    return tuple(values)


def polynomial(k):
    return 0


def reconstruct():
    return True

print deconstruct(1234, 6, 3)


