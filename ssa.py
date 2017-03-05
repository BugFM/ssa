# s = secret, n = total number of pieces, k = minimum required
def deconstruct(secret, n, k):
    values = []
    for i in range(n):
        values.append((i+1, polynomial(i+1, k, secret)))
    return tuple(values)


def return_coefficients(k):
    # k-1 random values.
    return [166, 94]


def polynomial(d, k, secret):
    coefficients = return_coefficients(k)
    for i in range(len(coefficients)):
        secret += coefficients[i] * d**(i+1)
    return secret


def reconstruct():
    # lagrange basis polynomials
    return True


# wiki sample
print deconstruct(1234, 6, 3)


